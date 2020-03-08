from django.contrib import admin
from .models import ContactForm
from django.contrib import admin





class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name','email','timestamp')


admin.site.register(ContactForm, ContactFormAdmin)
