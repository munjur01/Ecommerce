from django.contrib import admin
from store.models import ContactInfo

# Register your models here.
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone', 'subject')
admin.site.register(ContactInfo, ContactInfoAdmin)