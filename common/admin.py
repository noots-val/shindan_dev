from .models import App
from django.contrib import admin


class AppAdmin(admin.ModelAdmin):
    fields = ["id", "category", "title", "logo", "summary"]


admin.site.register(App, AppAdmin)
