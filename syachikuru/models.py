from django.db import models

"""
社畜る関連のテーブルを定義。

修正する際には、以下のファイルも訂正すること
1. 社畜るER図.a5er
2. 社畜るテーブル定義書.xlsx（ツールで出力可能）
"""


class Characteristic(models.Model):
    characteristic_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.pk)


class Question(models.Model):
    question_sentence = models.TextField()
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Result(models.Model):
    level = models.IntegerField()
    type = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.pk)


class Candidate(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.pk)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_sentence = models.TextField()
    point = models.IntegerField()

    def __str__(self):
        return str(self.pk)


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
