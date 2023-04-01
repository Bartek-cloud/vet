from django.forms import ModelForm
from schedule.models import Calendar
from schedule.views import CalendarByPeriodsView
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from veter.models import Visit
from website.models import FormPage



@register_snippet
class RecepjonistPage(Page):
    template = "veter/pages/visitpages.html"

    class Meta:
        verbose_name = "Recepc"
        #model = Visit

@register_snippet
class VetPage(Page):
    template = "veter/pages/visitpages.html"

    class Meta:
        verbose_name = "Wet"
        #model = Visit
