from import_export.admin import ImportExportModelAdmin

from .models import App, Article
from django.contrib import admin


class AppAdmin(ImportExportModelAdmin):
    list_display = ['id', 'category', 'title', 'logo', 'summary']
    list_editable = ['category', 'title', 'logo', 'summary']
    ordering = ('id',)


class ArticleAdmin(ImportExportModelAdmin):
    list_display = ['id', 'category', 'title', 'header', 'content1', 'content2', 'content3', 'img1', 'img2', 'status',
                    'order', 'created_at', 'updated_at']
    list_editable = ['category', 'title', 'header', 'content1', 'content2', 'content3', 'img1', 'img2', 'status',
                     'order']
    ordering = ('id',)


admin.site.register(App, AppAdmin)
admin.site.register(Article, ArticleAdmin)
