from django.db import models

"""
16タイプ関連のテーブルを定義。

修正する際には、以下のファイルも訂正すること
1. 16タイプER図.a5er
2. 16タイプテーブル定義書.xlsx（ツールで出力可能）
"""


class PokemonResult(models.Model):
    name = models.CharField(max_length=255)
    head = models.TextField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.pk)
