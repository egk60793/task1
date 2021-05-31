from django.contrib import admin
from .models import *


class DivisionAdmin(admin.ModelAdmin):
    list_display = ('divisional_name', 'divisional_code')
    list_display_links = ('divisional_name', 'divisional_code')
    search_fields = ('divisional_name', 'divisional_code')


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'status', 'it_employee', 'division')
    list_display_links = ('user_name', 'division')
    search_fields = ('user_name',)

admin.site.register(Division, DivisionAdmin)
admin.site.register(User, UserAdmin)
