from coderedcms.blocks import BaseBlock, LAYOUT_STREAMBLOCKS
from coderedcms.models import CoderedWebPage

from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from schedule_wagtail.blocks import LAYOUT_STREAMBLOCKS_CALENDAR
from veter.models import Visit
from website.models import FormPage



class CalendarPageClient(CoderedWebPage):

    body = StreamField(
        LAYOUT_STREAMBLOCKS_CALENDAR, null=True, blank=True, use_json_field=True
    )
    template = "coderedcms/pages/form_page.html"

    class Meta:
        verbose_name = "CalendarPageClient"


class CalendarPageReceptionist(CoderedWebPage):

    body = StreamField(
        LAYOUT_STREAMBLOCKS_CALENDAR, null=True, blank=True, use_json_field=True
    )
    template = "coderedcms/pages/form_page.html"

    class Meta:
        verbose_name = "CalendarPageReceptionist"


class CalendarPageVet(CoderedWebPage):

    body = StreamField(
        LAYOUT_STREAMBLOCKS_CALENDAR, null=True, blank=True, use_json_field=True
    )
    template = "coderedcms/pages/form_page.html"

    class Meta:
        verbose_name = "CalendarPageVet"
