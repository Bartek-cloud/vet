from .block import *

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

