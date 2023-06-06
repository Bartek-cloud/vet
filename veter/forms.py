
import datetime
from coderedcms.wagtail_flexible_forms.blocks import DateTimePickerInput, DatePickerInput
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError
from django.db.models import TextField
from schedule.forms import SpanForm, EventForm
from schedule.models import Event, Occurrence
from django.forms import Form, ModelForm, DateField, widgets, SplitDateTimeWidget
from django import forms
from schedule.widgets import ColorInput
#from datetimewidget.widgets import DateTimeWidget
from wagtail.users.forms import User

from schedule_wagtail.models import EventSnippet
from veter.models import Visit, Pet
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django import forms
from schedule.models import Event
from material import Layout, Row, Fieldset
#from material import TextField, DateTimePickerInput, SubmitButton


class EventFormWag(forms.ModelForm):
    """
    Formularz do tworzenia nowego wydarzenia.
    """
    class Meta:
        model = Visit
        fields = ['title', 'description','animal']
    layout = Layout(
        Row('title'),
     #   Row('start', 'end'),
        Row('description'),
     #   Row('cost'),
     #   Row('vet'),
        Row('animal'),
        #SubmitButton('Zapisz')
    )

    fieldsets = (
        Fieldset('Dodaj nowe wydarzenie', 'title', 'start', 'end', 'description','cost','vet','animal'),
    )

    def __init__(self, *args, **kwargs):
        super(EventFormWag, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Tytuł wizyty',
            'class': 'form-control'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Opis wizyty',
            'class': 'form-control'
        })
        self.fields['animal'].widget.attrs.update({
            'class': 'form-select'
        })


    def clean(self):
        cleaned_data = super().clean()

        # Walidacja pól formularza
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        if start > end:
            self.add_error('start', 'data początkowa jest wcześniejsza od końcowej')
        if start + datetime.timedelta(minutes=120) < end:
            self.add_error('end', 'za długi czas trwania')

class RecEventFormWag(forms.ModelForm):

    class Meta:
        model = Visit
        fields = ['creator','animal','vet','title', 'start', 'end', 'description']
        widgets = {
            #'title': TextField(),
            'start': DateTimePicker(
             # formatowanie daty i czasu wg. własnego uznania
        ),
            'end': DateTimePicker(),
            #'end': DateTimePickerInput(date_format='%Y-%m-%d %H:%M'),
            #'description': TextField()
        }

    layout = Layout(
        Row('vet'),
        Row('animal'),
        Row('creator'),
        Row('title'),
        Row('start', 'end'),
        Row('description'),
   #     Row('cost'),

        #SubmitButton('Zapisz')
    )
    fieldsets = (
        Fieldset('Dodaj nowe wydarzenie','creator', 'title', 'start', 'end', 'description','cost','vet','animal'),
    )
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name','species','age','isfemale', 'Client']


    layout = Layout(
        Row('name'),
        Row('species'),
        Row('age'),
        Row('isfemale'),
        Row('Client'),

        #SubmitButton('Zapisz')
    )
    fieldsets = (
        Fieldset('name','species', 'age', 'isfemale', 'Client'),
    )
class ClientForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = ['','','','', '']
        exclude=[]


    # layout = Layout(
    #     Row('name'),
    #     Row('species'),
    #     Row('age'),
    #     Row('isfemale'),
    #     Row('Client'),
    #
    #     #SubmitButton('Zapisz')
    # )
    # fieldsets = (
    #     Fieldset('name','species', 'age', 'isfemale', 'Client'),
    # )
class OccurrenceForm(SpanForm):
    class Meta:
        model = Occurrence
        exclude = ("original_start", "original_end", "event", "cancelled")


class EventAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Visit
        widgets = {"color_event": ColorInput}
