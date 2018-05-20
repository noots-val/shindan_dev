from .models import App
from django.contrib import admin


class AppAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "title", "logo", "summary"]
    ordering = ("id",)


admin.site.register(App, AppAdmin)
