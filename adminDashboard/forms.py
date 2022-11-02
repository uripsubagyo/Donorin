from django import forms
from django.forms import ModelForm
from adminDashboard.models import hasilScreening

class ScreeningForm(ModelForm):
    class Meta:
        model = hasilScreening
        fields = ('namaDonor', 'suhuTubuh', 'tekananDarah', 'kadarHemo', 'beratBadan')