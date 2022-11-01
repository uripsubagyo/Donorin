from django import forms
from datetime import datetime

def date_validator(tanggal):
	current = int(datetime.now().strftime("%j"))
	inp = int(tanggal.strftime("%j"))
	if inp <= current: raise forms.ValidationError("Masukkan tanggal yang akan datang")

loc = [
    ('prov', 'PMI Provinsi DKI Jakarta'),
    ('jakut', 'PMI Kota Jakarta Utara'),
    ('jakpus', 'PMI Kota Jakarta Pusat'),
    ('jaktim', 'PMI Kota Jakarta Timur'),
    ('jakbar', 'PMI Kota Jakarta Barat'),
    ('jaksel', 'PMI Kota Jakarta Selatan'),
]

class JadwalForm(forms.Form):
    tanggal = forms.DateField(validators=[date_validator], widget=forms.DateTimeInput(attrs={'type':'date','class':'form-control'}))
    lokasi = forms.ChoiceField(choices=loc, widget=forms.Select(attrs={'class': 'form-control'}))