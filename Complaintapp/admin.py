from django.contrib import admin
from Complaintapp.models import ComplaintInfo,WardenInfo

# Register your models here.
class WardenAdmin(admin.ModelAdmin):
    fields=['name','year','reg_no', 'block','room_no','complaintbox','email']
    search_fields=['room_no','reg_no','block']
    list_display=['name','year','reg_no','room_no','block','complaintbox','email']
admin.site.register(ComplaintInfo,WardenAdmin)
admin.site.register(WardenInfo)