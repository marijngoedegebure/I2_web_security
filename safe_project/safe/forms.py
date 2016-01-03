from django.forms import ModelForm
from message_module.models import Message

class SafeMessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['text']
