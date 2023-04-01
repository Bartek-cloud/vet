from coderedcms.blocks import BaseBlock
from django.forms import ModelForm
from django.views.generic.detail import SingleObjectMixin

from wagtail import blocks
from wagtail.blocks import ChooserBlock
from wagtail.contrib.routable_page.models import RoutablePage
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from veter.models import Visit
from coderedcms.blocks import CardBlock, GridBlock, HeroBlock, CONTENT_STREAMBLOCKS, CardGridBlock, LAYOUT_STREAMBLOCKS
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks
from schedule.models import Calendar

#@register_snippet(Calendar)

class BuyCalendarandHour(blocks.StructBlock):
    #template_name = "schedule/calendar.html"
    #template = "schelude/fullcalendar.html"
    calendar = blocks.StreamBlock(
        [
            #('calendar', SnippetChooserBlock('schedule.Calendar')),
            ('calendar', SnippetChooserBlock('schedule_wagtail.CalendarSnippet')),
        ],
        required=True,
        label='Countries and Regions',
    )
    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request)
    #     context["calendar_slug"] = "calendar_slug"#self.kwargs.get("calendar_slug")
    #     return context
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["calendar_slug"] = value['calendar'][0].value.slug#self.kwargs.get("calendar_slug")
        return context
    class Meta:
        # icon = 'user'
        # form_classname = 'person-block struct-block'
        template = "schedule_wagtail/fullcalendar.html"
        #template = "schelude/aaa.html"
        label = 'Calendarssss'
