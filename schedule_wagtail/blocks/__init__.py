from coderedcms.blocks import HeroBlock, GridBlock, CardGridBlock, CardBlock
from coderedcms.blocks import CONTENT_STREAMBLOCKS
from .block import *

CALENDAR_STREAMBLOCKS = [
    ('CalendarBuy', BuyCalendarandHour()),
    ('CalendarView', ViewCalendarandHour()),
]

# this defines final set of content blocks in the entire project!
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

