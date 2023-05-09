from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from schedule.models import Calendar

#from schedule_wagtail.views import CreateEventView
from schedule_wagtail.views import CreateEventView
from veter.forms import EventFormWag, RecEventFormWag
from veter.models import Visit


class vetCreateEventView(CreateEventView):
    #template_name = "schedule_wagtail/create_event.html"
    """
    Widok do dodawania nowego wydarzenia.
    """
    model = Visit
    template_name = 'schedule_wagtail/event_create.html'
    form_class = EventFormWag

    def form_valid(self, form):
        event = form.save(commit=False)
        event.creator = self.request.user
        event.calendar = get_object_or_404(Calendar, slug=self.kwargs["calendar_slug"])
        event.save()
        return HttpResponseRedirect("/wizyta/")


class vetRecepCreateEventView(CreateEventView):
    #template_name = "schedule_wagtail/create_event.html"
    """
    Widok do dodawania nowego wydarzenia.
    """
    model = Visit
    template_name = 'schedule_wagtail/event_create.html'
    form_class = RecEventFormWag

    def form_valid(self, form):
        event = form.save(commit=False)
      #  event.creator = self.request.user
        event.calendar = get_object_or_404(Calendar, slug=self.kwargs["calendar_slug"])
        event.save()
        return HttpResponseRedirect("/recepcjonista/")
