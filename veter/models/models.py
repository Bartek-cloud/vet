from django.contrib.auth.models import AbstractUser, User
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from schedule.models import Event
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.modeladmin.options import ModelAdminGroup, modeladmin_register, ModelAdmin
from wagtail.models import PreviewableMixin, Orderable, Page
from wagtail.snippets.models import register_snippet


class Pet(ClusterableModel):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    isfemale = models.BooleanField(default=True)
    Client = models.ForeignKey(to=User, on_delete=models.CASCADE,
                               limit_choices_to={'groups__name': 'Clients'})
    description = models.CharField(max_length=1000, null=True, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('species'),
        FieldPanel('age'),
        FieldPanel('isfemale'),
        FieldPanel('Client'),
        InlinePanel("Result", label="Result"),
        InlinePanel("Visit", label="Visit"),
        InlinePanel("Treatment", label="Treatment"),
    ]

    def __str__(self):
        return self.name


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


class Visit(Orderable, Event):
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    vet = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,
                            limit_choices_to={'groups__name': 'Clients'}, related_name="vet")
    animal = ParentalKey(to=Pet, on_delete=models.CASCADE, related_name="Visit")
    panels = [
        FieldPanel('start'),
        FieldPanel('end'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('creator'),
        FieldPanel('created_on'),
        FieldPanel('updated_on'),
        FieldPanel('rule'),
        FieldPanel('end_recurring_period'),
        FieldPanel('calendar'),
        FieldPanel('color_event'),
        FieldPanel('vet'),
        FieldPanel('animal'),
        FieldPanel('Client'),
    ]


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
