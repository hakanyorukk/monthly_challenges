from django.contrib import admin

# Register your models here.

from .models import Months, Challenges

class MonthAdmin(admin.ModelAdmin):
    list_diplay = ("month", "slug")

admin.site.register(Months, MonthAdmin)
admin.site.register(Challenges)