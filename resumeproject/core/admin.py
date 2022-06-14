from django.contrib import admin
from core.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','sub','message']
admin.site.register(Contact,ContactAdmin)    