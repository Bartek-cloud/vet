from schedule.views import *

from schedule_wagtail.forms import EventFormWag


class CalendarView(CalendarView):
    template_name = "schedule_wagtail/calendar.html"

class FullCalendarView(FullCalendarView):
    template_name = "schedule_wagtail/fullcalendar.html"

class CalendarByPeriodsView(CalendarByPeriodsView):
    template_name = "schedule_wagtail/calendar_by_period.html"

class OccurrenceView(OccurrenceView):
    template_name = "schedule_wagtail/occurrence.html"

class OccurrencePreview(OccurrencePreview):
    template_name = "schedule_wagtail/occurrence.html"

class EditOccurrenceView(EditOccurrenceView):
    template_name = "schedule_wagtail/edit_occurrence.html"

class CreateOccurrenceView(CreateOccurrenceView):
    template_name = "schedule_wagtail/edit_occurrence.html"

class CancelOccurrenceView(CancelOccurrenceView):
    template_name = "schedule_wagtail/cancel_occurrence.html"

class EventView(EventView):
    template_name = "schedule_wagtail/event.html"

class EditEventView(EditEventView):
    template_name = "schedule_wagtail/create_event.html"

class CreateEventView(CreateEventView):
    #template_name = "schedule_wagtail/create_event.html"
    """
    Widok do dodawania nowego wydarzenia.
    """
    model = Event
    template_name = 'schedule_wagtail/event_create.html'
    form_class = EventFormWag

    def form_valid(self, form):
        form.save()
        return redirect('schedule:index')

class DeleteEventView(DeleteEventView):
    template_name = "schedule_wagtail/delete_event.html"

from django.shortcuts import render, redirect

# Create your views here.
