from django.contrib import admin

# Register your models here.
from savings.models import Target


class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'days')

admin.site.register(Target, TargetAdmin)