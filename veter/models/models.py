from django.contrib.auth.models import AbstractUser, User
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.modeladmin.options import ModelAdminGroup, modeladmin_register, ModelAdmin
from wagtail.models import PreviewableMixin
from wagtail.snippets.models import register_snippet




class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.DecimalField(decimal_places=2,max_digits=6,null=True, blank=True)
    isfemale = models.BooleanField()
    Client = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
   # def clients(self):
    #   Clients.objects.filter(self)
    def results(self):
       return Result.objects.filter(Pet=self)
    def Visits(self):
       return Visit.objects.filter(Pet=self)
    def Treatments(self):
       return Treatment.objects.filter(Pet=self)
    description = models.CharField(max_length=1000,null=True, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('species'),
        FieldPanel('age'),
        FieldPanel('gender'),
    ]

    def __str__(self):
        return self.name


class Result(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)
    pet = models.ForeignKey(to=Pet,on_delete=models.SET_NULL,null=True, blank=True)
    panels = [
        FieldPanel('date'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


class Visit(models.Model):#,event
    type = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=255)
    cost = models.DecimalField(decimal_places=2,max_digits=10)
    date = models.DateTimeField()
    vet = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True, blank=True)
    animal = models.ForeignKey(to=Pet,on_delete=models.SET_NULL,null=True, blank=True)
    panels = [
        FieldPanel('type'),
        FieldPanel('description'),
        FieldPanel('cost'),
        FieldPanel('date'),
    ]

    def __str__(self):
        return self.type


class Treatment(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)
    pet = models.ForeignKey(to=Pet, on_delete=models.SET_NULL, null=True, blank=True)
    panels = [
        FieldPanel('date'),
        FieldPanel('text'),
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


class DataBaseAdmin(ModelAdminGroup):
    menu_label = "Database"
    menu_icon = "fa-database"
    menu_order = 200
    items = (
        PetAdmin,
        TreatmentAdmin,
        ResultAdmin,
        VisitAdmin,

    )


modeladmin_register(DataBaseAdmin)
