from django.urls import path

from veter.views import CreateEventView, RecEventFormWag,CreatePetView,EditPetView

urlpatterns = [
    path('pet/edit/<int:pk>', EditPetView.as_view(), name='EditPetView'),
    ]
