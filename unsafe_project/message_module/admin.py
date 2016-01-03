from django.contrib import admin

# Register your models here.
from message_module.models import Message


class MessageAdmin(admin.ModelAdmin):

    list_display = ('text', 'user')

admin.site.register(Message, MessageAdmin)
