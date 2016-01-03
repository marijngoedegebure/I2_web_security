from django import forms
from django.forms import ModelForm
from message_module.models import Message
from unsafe.models import UnsafeUser


class UnSafeMessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['text']


class UnsafeUserCreateForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    plaintext_password = forms.CharField(label='Password', max_length=100)
