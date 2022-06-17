from .models import Session
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('date', 'time',)
        widgets = {"date": DateInput()}
