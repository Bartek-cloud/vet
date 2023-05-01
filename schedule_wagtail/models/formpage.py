from coderedcms.wagtail_flexible_forms.blocks import DateTimePickerInput
from datetimewidget.widgets import DateTimeWidget
from django import forms
from django.db.models import TextField
from schedule.models import Event
from material import Layout, Row, Fieldset
from wagtail.admin.filters import DateRangePickerWidget


class EventForm(forms.ModelForm):
    """
    Formularz do tworzenia nowego wydarzenia.
    """

    class Meta:
        model = Event
        fields = ['title', 'start', 'end', 'description']
        # widgets = {
        #     'title': TextField(),
        #     'start': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        #     'end': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        #     'description': TextField()
        # }

    layout = Layout(
        Row('title'),
        Row('start', 'end'),
        Row('description'),
      #  SubmitButton('Zapisz')
    )

    fieldsets = (
        Fieldset('Dodaj nowe wydarzenie', 'title', 'start', 'end', 'description'),
    )

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Tytuł wydarzenia'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Opis wydarzenia'
        })
