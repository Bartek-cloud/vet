from coderedcms.models import CoderedWebPage
from django.forms import ModelForm
from schedule.models import Calendar
from schedule.views import CalendarByPeriodsView
from wagtail import blocks
from wagtail.admin.panels import StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from schedule_wagtail.blocks import LAYOUT_STREAMBLOCKS_CALENDAR
from veter.blocks import PetCardGrid, LAYOUT_STREAMBLOCKS_CALENDAR_CARDGRID
from veter.models import Pet, Visit

from website.models import FormPage
# CARD_GRID_BLOCKS=[
#     ('petcardgrid', PetCardGrid())]
#LAYOUT_STREAMBLOCKS_CALENDAR_CARDGRID = LAYOUT_STREAMBLOCKS_CALENDAR + CARD_GRID_BLOCKS


@register_snippet
class RecepjonistPage(Page):
    template = "veter/pages/visitpages.html"

    class Meta:
        verbose_name = "RecepjonistPage"
        #model = Visit

@register_snippet
class VetPage(Page):
    template = "veter/pages/vetpages.html"

    class Meta:
        verbose_name = "VetPage"
        #model = Visit

class CalendarPageClient(CoderedWebPage):

    body = StreamField(

        LAYOUT_STREAMBLOCKS_CALENDAR_CARDGRID, null=True, blank=True, use_json_field=True
    )
    template = "coderedcms/pages/form_page.html"

    class Meta:
        verbose_name = "CalendarPageClient"


class CalendarPageReceptionist(CoderedWebPage):

    body = StreamField(
        LAYOUT_STREAMBLOCKS_CALENDAR_CARDGRID, null=True, blank=True, use_json_field=True
    )
    template = "coderedcms/pages/form_page.html"

    class Meta:
        verbose_name = "CalendarPageReceptionist"


class CalendarPageVet(CoderedWebPage):

    body = StreamField(
        LAYOUT_STREAMBLOCKS_CALENDAR_CARDGRID, null=True, blank=True, use_json_field=True
    )
    template = "veter/pages/vetpages.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['pets'] = Pet.objects.all()
        context['visits'] = Visit.objects.all()
        return context
    class Meta:
        verbose_name = "CalendarPageVet"
