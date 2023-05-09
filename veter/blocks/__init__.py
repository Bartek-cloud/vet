from schedule_wagtail.blocks import BuyCalendarandHour, ViewCalendarandHour, recBuyCalendarandHour
from .cardgrid import *
from coderedcms.blocks import HeroBlock, GridBlock, CardGridBlock, CardBlock
from coderedcms.blocks import CONTENT_STREAMBLOCKS


CALENDAR_STREAMBLOCKS = [
    ('CalendarBuy', BuyCalendarandHour()),
    ('recCalendarBuy', recBuyCalendarandHour()),
    ('CalendarView', ViewCalendarandHour()),
]
CARD_GRID_BLOCKS=[
    ('petcardgrid', PetCardGrid()),
    ('visitcardgrid', VisitCardGrid()),
    ('clientcardgrid', ClientCardGrid()),
]
# this defines final set of content blocks in the entire project!
CONTENT_STREAMBLOCKS = \
    CONTENT_STREAMBLOCKS \
    + CALENDAR_STREAMBLOCKS \
    + CARD_GRID_BLOCKS

LAYOUT_STREAMBLOCKS_CALENDAR_CARDGRID = [
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
