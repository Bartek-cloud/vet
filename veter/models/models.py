from django.contrib.auth.models import AbstractUser, User
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from schedule.models import Event
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.modeladmin.options import ModelAdminGroup, modeladmin_register, ModelAdmin
from wagtail.models import PreviewableMixin, Orderable, Page
from wagtail.snippets.models import register_snippet


class Pet(ClusterableModel):
    name = models.CharField(max_length=255,verbose_name = 'imię')
    species = models.CharField(max_length=255,verbose_name = 'gatunek')
    age = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True,verbose_name = 'wiek')
    isfemale = models.BooleanField(default=True,verbose_name = 'Samica')
    Client = models.ForeignKey(to=User, on_delete=models.CASCADE,
                               limit_choices_to={'groups__name': 'Klienci'},verbose_name = 'Klient')
    description = models.CharField(max_length=1000, null=True, blank=True,verbose_name = 'opis')
    panels = [
        MultiFieldPanel([
        FieldPanel('name'),
        FieldPanel('Client'),
        ]),
        MultiFieldPanel([
        FieldPanel('species'),
        FieldPanel('age'),
        FieldPanel('isfemale'),
        ], heading='podstawowe informacje'),
        InlinePanel("Result", label="Wynik"),
        InlinePanel("Pet", label="Wizyta"),
       # InlinePanel("Visit"),#, label="Wizyta"),
        InlinePanel("Treatment", label="Kuracja"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zwierzę'
        verbose_name_plural = 'Zwierzęta'

class Result(Orderable):
    date = models.DecimalField(null=True, blank=True,verbose_name = 'dane',max_digits=10,decimal_places=2)
    text = models.CharField(max_length=255,verbose_name = 'opis')
    pet = ParentalKey(to=Pet, on_delete=models.SET_NULL, null=True, blank=True, related_name="Result")
    panels = [
        FieldPanel('date'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text
    class Meta:
        verbose_name = 'Wynik'
        verbose_name_plural = 'Wyniki'

class Visit(Orderable, Event):
  #  cost = models.DecimalField(decimal_places=2, max_digits=10,verbose_name = 'Koszt')
    vet = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,
                            limit_choices_to={'groups__name': 'Weterynarze'}, related_name="vet",verbose_name = 'Weterynarz')
    animal = ParentalKey(to=Pet, on_delete=models.CASCADE, related_name="Pet",verbose_name = 'Zwierzę')#limit_choices_to={'Client': 'id__creator'},)
    panels = [
        MultiFieldPanel([
        FieldPanel('start'),
        FieldPanel('end'),
        ], heading='czas'),
        MultiFieldPanel([
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('vet'),
        FieldPanel('animal'),
    #    FieldPanel('cost'),
        ]  , heading='opisy wizyty'),
        # FieldPanel('creator'),
        # MultiFieldPanel([
        # FieldPanel('rule'),
        # FieldPanel('end_recurring_period'),
        #  ], heading='zasady powórzenia'),
        # MultiFieldPanel([
        # #FieldPanel('calendar',heading="kalendarz"),
        # FieldPanel('color_event',heading="kolor"),
        #      ], heading = 'ustawienia wyświetlania w kalendarzu'),
    ]
    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'

class Treatment(models.Model):
    date = models.DateTimeField(null=True, blank=True,verbose_name = 'data')
    text = models.CharField(max_length=255,verbose_name = 'opis')
    pet = ParentalKey(to=Pet, on_delete=models.SET_NULL, null=True, blank=True, related_name="Treatment")
    panels = [
        FieldPanel('date'),
        FieldPanel('text'),
        FieldPanel('pet'),
    ]

    def __str__(self):
        return self.text
    class Meta:
        verbose_name = 'Kuracja'
        verbose_name_plural = 'Kuracje'


class UserAdmin(ModelAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name',)
    list_filter = ("groups",)
    search_fields = ('first_name', 'last_name')





class TreatmentAdmin(ModelAdmin):
    model = Treatment
    list_display = ("date", "pet","text")


class ResultAdmin(ModelAdmin):
    model = Result
    list_display = ("date", "pet", "text")


class VisitAdmin(ModelAdmin):
    model = Visit
    list_display = ("start", "end", 'title', 'vet', 'animal')


class PetAdmin(ModelAdmin):
    model = Pet
    list_display = ("name", "Client", 'species', 'age', 'isfemale')


class DataBaseAdmin(ModelAdminGroup):
    menu_label = "Baza danych"
    menu_icon = "fa-database"
    menu_order = 200
    items = (
        PetAdmin,
        TreatmentAdmin,
        ResultAdmin,
        VisitAdmin,
    )


modeladmin_register(DataBaseAdmin)
