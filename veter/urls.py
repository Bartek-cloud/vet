from django.urls import path

from veter.views import CreateEventView, RecEventFormWag,CreatePetView,EditPetView

urlpatterns = [
    path('pet/edit/<int:pet_id>', EditPetView.as_view(), name='petedit'),
    #path('event/createrecepcjonist/<slug:calendar_slug>', RecepCreateEventView.as_view(), name='rec_calendar_create_event'),
    ]
