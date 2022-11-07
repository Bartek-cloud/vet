from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=255)
    panels = [
        FieldPanel('name'),
        FieldPanel('species'),
        FieldPanel('age'),
        FieldPanel('gender'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Visit(models.Model):
    type = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=255)
    cost = models.DecimalField()
    date = models.DateTimeField()
    panels = [
        FieldPanel('type'),
        FieldPanel('description'),
        FieldPanel('cost'),
        FieldPanel('date'),
    ]

    def __str__(self):
        return self.type


class Client(AbstractUser):
    pass


class Vet(AbstractUser):
    pass


class Receptionist(AbstractUser):
    pass


@register_snippet
class Result(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('date'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


@register_snippet
class Leczenie(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('date'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text
