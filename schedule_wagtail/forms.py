from schedule.forms import SpanForm, EventForm
from schedule.models import Event, Occurrence

from django import forms
from schedule.widgets import ColorInput

from veter.models import Visit


class EventFormVisit(EventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    end_recurring_period = forms.DateTimeField(
        label=_("End recurring period"),
        help_text=_("This date is ignored for one time only events."),
        required=False,
    )

    class Meta:
        model = Visit
        exclude = ("creator", "created_on", "calendar")


class OccurrenceForm(SpanForm):
    class Meta:
        model = Occurrence
        exclude = ("original_start", "original_end", "event", "cancelled")


class EventAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Visit
        widgets = {"color_event": ColorInput}
