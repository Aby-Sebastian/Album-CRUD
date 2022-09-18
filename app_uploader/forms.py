from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
	alt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alt text for image'}))

	class Meta:
		model = Album
		fields = ['image', 'alt']
		
