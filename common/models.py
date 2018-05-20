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
    logo = models.URLField(null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return str(self.pk)
