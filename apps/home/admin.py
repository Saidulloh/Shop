from django.contrib import admin
from apps.home.models import *
from .forms import *
# Register your models here.

admin.site.register(Setting)

class SocialSidebarAdmin(admin.ModelAdmin):
    form = SocialSidebarForm
    list_display = ['link_address', 'social_name']
    prepopulated_fields = {'social_name':('link_address',)}

    fieldsets = (
        (None, {
            'fields': ('link_address', 'social_name', 'icon', 'background')
            }),
        )

admin.site.register(SocialSidebar, SocialSidebarAdmin)