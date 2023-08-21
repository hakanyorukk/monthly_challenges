from django.contrib import admin

# Register your models here.

from .models import Months, Challenges, Note

class MonthAdmin(admin.ModelAdmin):
    list_diplay = ("month_name", "slug", )

class NoteAdmin(admin.ModelAdmin):
    list_display = ("month", "title","date")

admin.site.register(Months, MonthAdmin)
admin.site.register(Challenges)
admin.site.register(Note, NoteAdmin)