from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.views import View
from django.views.generic import CreateView, UpdateView
from schedule.models import Calendar

#from schedule_wagtail.views import CreateEventView
from schedule_wagtail.views import CreateEventView
from veter.forms import EventFormWag, RecEventFormWag, PetForm, ClientForm
from veter.models import Visit, Pet


class vetCreateEventView(CreateEventView):
    #template_name = "schedule_wagtail/create_event.html"
    """
    Widok do dodawania nowego wydarzenia.
    """
    model = Visit#{% extends "coderedcms/pages/form_page.html" %}
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




class CreatePetView(CreateView):
    #template_name = "schedule_wagtail/create_event.html"
    """
    Widok do dodawania nowego wydarzenia.
    """
    model = Pet#{% extends "coderedcms/pages/form_page.html" %}
    template_name = 'schedule_wagtail/event_create.html'
    form_class = PetForm


class EditPetView(UpdateView):
    # template_name = "schedule_wagtail/create_event.html"
    """
    Widok do dodawania nowego wydarzenia.
    """
    model = Pet  # {% extends "coderedcms/pages/form_page.html" %}
    template_name = 'schedule_wagtail/event_create.html'
    form_class = PetForm


class EditEventView(UpdateView):

    model = User
    template_name = 'veter/forms/sawaccount.html'
    form_class = ClientForm

class EditClientsView(UpdateView):

    model = User
    template_name = 'veter/forms/sawaccount.html'
    form_class = ClientForm

    def form_valid(self, form):
        event = form.save(commit=False)
        event.creator = self.request.user
        event.calendar = get_object_or_404(Calendar, slug=self.kwargs["calendar_slug"])
        event.save()
        return HttpResponseRedirect("/wizyta/")
