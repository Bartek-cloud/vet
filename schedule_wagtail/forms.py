
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
from schedule_wagtail.models import EventSnippet
from veter.models import Visit
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django import forms
from schedule.models import Event
from material import Layout, Row, Fieldset
#from material import TextField, DateTimePickerInput, SubmitButton

#not working go veter
class EventFormWag(forms.ModelForm):
    """
    Formularz do tworzenia nowego wydarzenia.
    """

    class Meta:
        model = EventSnippet
       # fields = ['title', 'start', 'end', 'description']
        fields = ['title', 'description', 'start', 'end']
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
        Row('start', 'end'),
        Row('title'),
        Row('description'),
        #SubmitButton('Zapisz')
    )

    fieldsets = (
        Fieldset('Dodaj nowe wydarzenie', 'title', 'description','start', 'end'),
        #Fieldset('Dodaj nowe wydarzenie', 'title', 'start', 'end', 'description'),
    )

    def __init__(self, *args, **kwargs):
        super(EventFormWag, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Tytuł wydarzenia'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Opis wydarzenia'
        })

    def clean(self):
        cleaned_data = super().clean()

        # Walidacja pól formularza
        # start = cleaned_data.get("start")
        # end = cleaned_data.get("end")
        # if start > end:
        #     self.add_error('start', 'data początkowa jest wcześniejsza od końcowej')
        # if start + datetime.timedelta(minutes=120) < end:
        #     self.add_error('end', 'za długi czas trwania')

class RecEventFormWag(forms.ModelForm):
    class Meta:
        model = EventSnippet
        fields = ['creator','title', 'start', 'end', 'description']
        widgets = {
            #'title': TextField(),
            #'start': DateTimePicker( ),
             # formatowanie daty i czasu wg. własnego uznania

           # 'end': DateTimePicker(),
            #'end': DateTimePickerInput(date_format='%Y-%m-%d %H:%M'),
            #'description': TextField()
        }

    layout = Layout(
        Row('creator'),
        Row('title'),
        Row('start', 'end'),
        Row('description'),
        #SubmitButton('Zapisz')
    )

    fieldsets = (
        Fieldset('Dodaj nowe wydarzenie','creator', 'title', 'start', 'end', 'description'),
    )
    def __init__(self, *args, **kwargs):
        super(RecEventFormWag, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Tytuł wydarzenia'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Opis wydarzenia'
        })
# class EventFormVisit(EventForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     end_recurring_period = forms.DateTimeField(
#         label=_("End recurring period"),
#         help_text=_("This date is ignored for one time only events."),
#         required=False,
#     )
#
#     class Meta:
#         model = Visit
#         exclude = ("creator", "created_on", "calendar")
#

class OccurrenceForm(SpanForm):
    class Meta:
        model = Occurrence
        exclude = ("original_start", "original_end", "event", "cancelled")


class EventAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Visit
        widgets = {"color_event": ColorInput}
