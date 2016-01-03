from django.forms import ModelForm
from message_module.models import Message
from unsafe.models import UnsafeUser


class UnSafeMessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['text']


class UnSafeUserForm(ModelForm):

    class Meta:
        model = UnsafeUser
        fields = ['username', 'password', 'is_admin']
