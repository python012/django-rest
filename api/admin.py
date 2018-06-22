from django.contrib import admin
from api.models import Event, Guest


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'attendees_limit', 'address', 'start_time']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']



admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

