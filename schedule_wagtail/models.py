from django.db import models

# Create your models here.
from schedule.models import Event
from wagtail.admin.panels import FieldPanel
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from schedule.models import Event
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.modeladmin.options import ModelAdminGroup, modeladmin_register, ModelAdmin
from wagtail.models import PreviewableMixin, Orderable, Page
from wagtail.snippets.models import register_snippet

from veter.models import Pet


@register_snippet
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
        FieldPanel('cost'),
        FieldPanel('creator'),
        FieldPanel('rule'),
        FieldPanel('end_recurring_period'),
        FieldPanel('calendar'),
        FieldPanel('color_event'),
        FieldPanel('vet'),
        FieldPanel('animal'),
        #FieldPanel('Client'),
    ]
