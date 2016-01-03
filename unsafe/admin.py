from django.contrib import admin

# Register your models here.
from .models import UnsafeUser


class UnsafeUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'password')

admin.site.register(UnsafeUser, UnsafeUserAdmin)
