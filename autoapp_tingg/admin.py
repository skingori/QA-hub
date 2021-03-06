from django.contrib import admin

# Register your models here.
from .models import APISettings, WebHook, UISettings, JSONSimulator, MockingData, TestrailDetails

admin.site.site_header = "CELLULANT QA HUB"
admin.site.site_title = "API Settings"
admin.site.index_title = "Tingg"
admin.AdminSite.index_title = "Tingg API Settings"


class APISettingsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'display_name',)

    # columns to be displayed on listing view

    list_display = ('status', 'display_name', 'unique_name', 'environment', 'url', 'path', 'description',)


class WebHookAdmin(admin.ModelAdmin):
    search_fields = ('id', 'status_code', 'status', 'description')

    # columns to be displayed on listing view

    list_display = ('status', 'status_code', 'url', 'description')


class UISettingsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'display_name',)
    list_display = ('display_name', 'unique_name', 'url', 'path', 'environment', 'description',)


class JSONSimulatorAdmin(admin.ModelAdmin):
    search_fields = ('id', 'unique_name',)
    list_display = ('status', 'unique_name', 'url', 'path', 'environment', 'description',)


class MockingAdmin(admin.ModelAdmin):
    search_fields = ('id', 'unique_name',)
    list_display = ('unique_name', 'json_string', 'description',)


class TestRailAdmin(admin.ModelAdmin):
    search_fields = ('id', 'testrail_username',)
    list_display = ('status', 'testrail_username', 'testrail_password', 'testrail_url',)


admin.site.register(APISettings, APISettingsAdmin)
admin.site.register(WebHook, WebHookAdmin)
admin.site.register(UISettings, UISettingsAdmin)
admin.site.register(JSONSimulator, JSONSimulatorAdmin)
admin.site.register(MockingData, MockingAdmin)
admin.site.register(TestrailDetails, TestRailAdmin)
