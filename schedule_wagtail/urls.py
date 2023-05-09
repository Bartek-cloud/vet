from django.urls import re_path, path
from django.views.generic.list import ListView

from schedule.feeds import CalendarICalendar, UpcomingEventsFeed
from schedule.models import Calendar
from schedule.periods import Day, Month, Week, Year
from schedule_wagtail.views import (
    CalendarByPeriodsView,
    CalendarView,
    CancelOccurrenceView,
    CreateEventView,
    CreateOccurrenceView,
    DeleteEventView,
    EditEventView,
    EditOccurrenceView,
    EventView,
    FullCalendarView,
    OccurrencePreview,
    OccurrenceView,
    api_move_or_resize_by_code,
    api_occurrences,
    api_select_create, RecepCreateEventView,
)
from veter.views import vetCreateEventView, vetRecepCreateEventView

urlpatterns = [
    path('calendar', ListView.as_view(model=Calendar), name='calendar_list'),
    #path('', ListView.as_view(model=Calendar), name='calendar_list'),
    path('calendar/year/<slug:calendar_slug>', CalendarByPeriodsView.as_view(template_name='schedule/calendar_year.html'), name='year_calendar', kwargs={'period': Year}),
    path('calendar/tri_month/<slug:calendar_slug>', CalendarByPeriodsView.as_view(template_name='schedule/calendar_tri_month.html'), name='tri_month_calendar', kwargs={'period': Month}),
    path('calendar/compact_month/<slug:calendar_slug>', CalendarByPeriodsView.as_view(template_name='schedule/calendar_compact_month.html'), name='compact_calendar', kwargs={'period': Month}),
    path('calendar/month/<slug:calendar_slug>', CalendarByPeriodsView.as_view(template_name='schedule/calendar_month.html'), name='month_calendar', kwargs={'period': Month}),
    path('calendar/week/<slug:calendar_slug>', CalendarByPeriodsView.as_view(template_name='schedule/calendar_week.html'), name='week_calendar', kwargs={'period': Week}),
    path('calendar/daily/<slug:calendar_slug>', CalendarByPeriodsView.as_view(template_name='schedule/calendar_day.html'), name='day_calendar', kwargs={'period': Day}),
    path('calendar/<slug:calendar_slug>', CalendarView.as_view(), name='calendar_home'),
    path('fullcalendar/<slug:calendar_slug>', FullCalendarView.as_view(), name='fullcalendar'),
    # Event Urls
    path('event/create/<slug:calendar_slug>', vetCreateEventView.as_view(), name='calendar_create_event'),
    path('event/createrecepcjonist/<slug:calendar_slug>', vetRecepCreateEventView.as_view(), name='rec_calendar_create_event'),
    path('event/edit/<slug:calendar_slug>/<int:event_id>', EditEventView.as_view(), name='edit_event'),
    path('event/<int:event_id>', EventView.as_view(), name='event'),
    path('event/delete/<int:event_id>', DeleteEventView.as_view(), name='delete_event'),
    # urls for already persisted occurrences
    path('occurrence/<int:event_id>/<int:occurrence_id>', OccurrenceView.as_view(), name='occurrence'),
    path('occurrence/cancel/<int:event_id>/<int:occurrence_id>', CancelOccurrenceView.as_view(), name='cancel_occurrence'),
    path('occurrence/edit/<int:event_id>/<int:occurrence_id>', EditOccurrenceView.as_view(), name='edit_occurrence'),
    # urls for unpersisted occurrences
    path('occurrence/<int:event_id>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>', OccurrencePreview.as_view(), name='occurrence_by_date'),
    path('occurrence/cancel/<int:event_id>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>', CancelOccurrenceView.as_view(), name='cancel_occurrence_by_date'),
    path('occurrence/edit/<int:event_id>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>', CreateOccurrenceView.as_view(), name='edit_occurrence_by_date'),
    # feed urls
    path('feed/calendar/upcoming/<int:calendar_id>', UpcomingEventsFeed(), name='upcoming_events_feed'),
    path('ical/calendar/<path:cal>', CalendarICalendar(), name='calendar_ical'),
    # api urls
    path('api/occurrences', api_occurrences, name='api_occurrences'),

    path('api/move_or_resize', api_move_or_resize_by_code, name='api_move_or_resize'),
    path('api/select_create', api_select_create, name='api_select_create'),
    path('', ListView.as_view(queryset=Calendar.objects.all()), name='')
]
