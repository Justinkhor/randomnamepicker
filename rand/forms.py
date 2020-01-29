from django import forms

from .models import Trial

class TrialForm(forms.ModelForm):
    class Meta:
        model = Trial
        labels = {
        "text": ""
            }
        fields = ('text',)
