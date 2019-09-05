from django.contrib import admin

# Register your models here.
from .models import APISettings

admin.site.site_header = "Tingg Checkout"
admin.site.site_title = "API Settings"
admin.site.index_title = "Tingg Checkout"
admin.AdminSite.index_title="Tingg API Settings"


class APISettingsAdmin(admin.ModelAdmin):
    search_fields = ('id', 'display_name',)

    # columns to be displayed on listing view

    list_display = ('display_name', 'unique_name', 'url','path', 'description',)


admin.site.register(APISettings)
