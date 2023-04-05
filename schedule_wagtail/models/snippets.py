from coderedcms.models import CoderedWebPage
from schedule.models import Calendar, Event, Occurrence
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet

from schedule_wagtail.blocks import LAYOUT_STREAMBLOCKS_CALENDAR


@register_snippet
class CalendarSnippet(Calendar):
    class Meta:
        proxy = True
# LAYOUT_STREAMBLOCKSCALENDAR= LAYOUT_STREAMBLOCKS+


@register_snippet
class EventSnippet(Event):
    class Meta:
        proxy = True


@register_snippet
class OccurrenceSnippet(Occurrence):
    class Meta:
        proxy = True
