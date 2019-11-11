from django.contrib import admin

# Register your models here.
from .models import APISettings, WebHook, UISettings, EnvironmentPorts

admin.site.site_header = "CELLULANT QA HUB"
admin.site.site_title = "API Settings"
admin.site.index_title = "Tingg"
admin.AdminSite.index_title = "Tingg API Settings"


class APISettingsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'display_name',)

    # columns to be displayed on listing view

    list_display = ('display_name', 'unique_name', 'url', 'port', 'path', 'description',)


class WebHookAdmin(admin.ModelAdmin):
    search_fields = ('id', 'status_code', 'status', 'description')

    # columns to be displayed on listing view

    list_display = ('status', 'status_code', 'url', 'description')


class UISettingsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'display_name',)
    list_display = ('display_name', 'unique_name', 'encoded_url', 'description',)


class EnvironmentAdmin(admin.ModelAdmin):
    search_fields = ('id', 'display_name',)
    list_display = ('display_name', 'unique_name', 'port', 'description',)


admin.site.register(APISettings, APISettingsAdmin)
admin.site.register(WebHook, WebHookAdmin)
admin.site.register(UISettings, UISettingsAdmin)
admin.site.register(EnvironmentPorts, EnvironmentAdmin)
