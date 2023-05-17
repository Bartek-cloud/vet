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
                               limit_choices_to={'groups__name': 'Clients'},verbose_name = 'Klient')
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
        InlinePanel("Visit", label="Wizyta"),
        InlinePanel("Treatment", label="Kuracja"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zwierzę'
        verbose_name_plural = 'Zwierzęta'

class Result(Orderable):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)
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
    cost = models.DecimalField(decimal_places=2, max_digits=10,verbose_name = 'Koszt')
    vet = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,
                            limit_choices_to={'groups__name': 'Vet'}, related_name="vet",verbose_name = 'Weterynarz')
    animal = ParentalKey(to=Pet, on_delete=models.CASCADE, related_name="Visit",verbose_name = 'Zwierze')
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
        FieldPanel('cost'),
        ]  , heading='opisy wizyty'),
        # FieldPanel('creator'),
        # MultiFieldPanel([
        # FieldPanel('rule'),
        # FieldPanel('end_recurring_period'),
        #  ], heading='zasady powórzenia'),
        MultiFieldPanel([
        #FieldPanel('calendar',heading="kalendarz"),
        FieldPanel('color_event',heading="kolor"),
             ], heading = 'ustawienia wyświetlania w kalendarzu'),
    ]
    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'

class Treatment(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)
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

class PetAdmin(ModelAdmin):
    model = Pet


class TreatmentAdmin(ModelAdmin):
    model = Treatment


class ResultAdmin(ModelAdmin):
    model = Result


class VisitAdmin(ModelAdmin):
    model = Visit


class UserAdmin(ModelAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name',)
    list_filter = ("groups",)
    search_fields = ('first_name', 'last_name')


class DataBaseAdmin(ModelAdminGroup):
    menu_label = "Database"
    menu_icon = "fa-database"
    menu_order = 200
    items = (
        PetAdmin,
        TreatmentAdmin,
        ResultAdmin,
        VisitAdmin,
        UserAdmin,

    )


modeladmin_register(DataBaseAdmin)

# def clients(self):
#   Clients.objects.filter(self)
#  @property
#   def results(self):
#       return Result.objects.filter(Pet=self)
#
#   def Visits(self):
#       return Visit.objects.filter(Pet=self)
#
#   def Treatments(self):
#       return Treatment.objects.filter(Pet=self)
