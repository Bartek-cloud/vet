from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks
from schedule.models import Calendar


class BuyCalendarandHour(blocks.StructBlock):
    calendar = blocks.StreamBlock(
        [
            ('calendar', SnippetChooserBlock('schedule_wagtail.CalendarSnippet')),
        ],
        required=True,
        label='Countries and Regions',
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["calendar_slug"] = value['calendar'][0].value.slug#self.kwargs.get("calendar_slug")
        return context

    class Meta:
        template = "schedule_wagtail/fullcalendar.html"
        label = 'Calendar'

class recBuyCalendarandHour(blocks.StructBlock):
    calendar = blocks.StreamBlock(
        [
            ('calendar', SnippetChooserBlock('schedule_wagtail.CalendarSnippet')),
        ],
        required=True,
        label='Countries and Regions',
    )
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["calendar_slug"] = value['calendar'][0].value.slug#self.kwargs.get("calendar_slug")
        return context
    class Meta:
        template = "schedule_wagtail/fullcalendarrecp.html"
        label = 'recCalendarsvisit'

class ViewCalendarandHour(blocks.StructBlock):
    calendar = blocks.StreamBlock(
        [
            ('calendar', SnippetChooserBlock('schedule_wagtail.CalendarSnippet')),
        ],
        required=True,
        label='Countries and Regions',
    )
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context["calendar_slug"] = value['calendar'][0].value.slug#self.kwargs.get("calendar_slug")
        context["calendar_id"] = value['calendar'][0].value.id
        return context
    class Meta:
        template = "schedule_wagtail/calendar.html"
        label = 'Calendarviev'
