from .models import App, Article
from django.contrib import admin


class AppAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "title", "logo", "summary"]
    list_editable = ["category", "title", "logo", "summary"]
    ordering = ("id",)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "title", "content", "status", "created_at", "updated_at"]
    list_editable = ["category", "title", "content", "status"]
    ordering = ("id",)


admin.site.register(App, AppAdmin)
admin.site.register(Article, ArticleAdmin)
