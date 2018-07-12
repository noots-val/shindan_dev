from django.db import models

"""
診断したんだん全般のテーブルを定義。

修正する際には、以下のファイルも訂正すること
1. commonER図.a5er
2. commonテーブル定義書.xlsx（ツールで出力可能）
"""


class App(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return str(self.pk)


class Article(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    header = models.TextField(null=True)
    content1 = models.TextField(null=True)
    content2 = models.TextField(null=True)
    content3 = models.TextField(null=True)
    img1 = models.ImageField(upload_to='images/', null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=255)
    order = models.IntegerField(default=999)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.pk)
