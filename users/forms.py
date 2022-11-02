from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserAccount

class RegistrationFormRelawan(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = UserAccount
		fields = ('email', 'username', 'password1', 'password2', 'nama', 'nomor_telepon', 'golongan_darah', 'jenis_kelamin', 'tanggal_lahir', 'provinsi', 'kota')

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = UserAccount.objects.exclude(pk=self.instance.pk).get(email=email)
		except UserAccount.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % email)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			user = UserAccount.objects.exclude(pk=self.instance.pk).get(username=username)
		except UserAccount.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)



class LoginForm(forms.ModelForm):
	password = forms.CharField(label='password', widget = forms.PasswordInput())

	class Meta:
		model = UserAccount
		fields = ("email", 'password')
	
	def clean(self):
		if(self.is_valid()):
			email = self.cleaned_data[email]
			password = self.cleaned_data['password']
			if not authenticate(email = email, password = password):
				raise forms.ValidationError("invalid")