from coderedcms.blocks import BaseBlock
from django.forms import ModelForm
from django.views.generic.detail import SingleObjectMixin

from wagtail import blocks
from wagtail.contrib.routable_page.models import RoutablePage
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from veter.models import Visit
from coderedcms.blocks import CardBlock, GridBlock, HeroBlock, CONTENT_STREAMBLOCKS, CardGridBlock, LAYOUT_STREAMBLOCKS

from wagtail.core import blocks

class BuyCalendarandHour(blocks.StructBlock):
    #template_name = "schedule/calendar.html"
    #template = "schelude/fullcalendar.html"
    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request)
    #     context["calendar_slug"] = "calendar_slug"#self.kwargs.get("calendar_slug")
    #     return context
    def get_form_context(self, value, prefix='', errors=None):
        context = super().get_form_context(value, prefix=prefix, errors=errors)
        context["calendar_slug"] = "calendar_slug"#self.kwargs.get("calendar_slug")
        return context
    class Meta:
        # icon = 'user'
        # form_classname = 'person-block struct-block'
        template = "schelude/fullcalendar.html"
        #template = "schelude/aaa.html"
        label = 'Calendar'

CALENDAR_STREAMBLOCKS = [
    ('Calendar', BuyCalendarandHour()),
]

# this defines final set of content blocks in the entire project!
# when adding new cjkcms-compatible apps, you can add their content blocks here
CONTENT_STREAMBLOCKS = \
    CONTENT_STREAMBLOCKS \
    + CALENDAR_STREAMBLOCKS \

LAYOUT_STREAMBLOCKS_CALENDAR = [
    ('hero', HeroBlock([
        ('row', GridBlock(CONTENT_STREAMBLOCKS)),
        ('cardgrid', CardGridBlock([
            ('card', CardBlock()),
        ])),
        ('html', blocks.RawHTMLBlock(icon='code', form_classname='monospace', label='HTML')),
    ])),
    ('row', GridBlock(CONTENT_STREAMBLOCKS)),
    ('cardgrid', CardGridBlock([
        ('card', CardBlock()),
    ])),
    ('html', blocks.RawHTMLBlock(icon='code', form_classname='monospace', label='HTML')),
]

