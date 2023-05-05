from django import forms
from . import models


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = models.ContactMessage
        fields = ("name", "email", "message")
