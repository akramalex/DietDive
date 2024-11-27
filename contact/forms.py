from django import forms
from .models import Contact

""" ContactForm is a ModelForm for the Contact model,
allowing users to submit their name, email, and message through a form."""


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
