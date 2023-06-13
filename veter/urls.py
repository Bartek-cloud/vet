from django.urls import path

from veter.views import CreateEventView, RecEventFormWag, CreatePetView, EditPetView, EditClientsView

urlpatterns = [
    path('pet/edit/<int:pk>', EditPetView.as_view(), name='EditPetView'),
    path('client/edit/<int:pk>', EditClientsView.as_view(), name='EditClientsView'),

    ]
