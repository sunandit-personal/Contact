from django.contrib import admin
from .models import Contact


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'CRT_DT', 'is_active', 'is_deleted',)
    search_fields = ['first_name', 'last_name', 'phone', 'email']


admin.site.register(Contact, ContactInfoAdmin)