from django.db import models

"""
16タイプ関連のテーブルを定義。

修正する際には、以下のファイルも訂正すること
1. 16タイプER図.a5er
2. 16タイプテーブル定義書.xlsx（ツールで出力可能）
"""


# ================================= 16タイプ共通 ===============================================

class Type(models.Model):
    name = models.CharField(max_length=4)
    description = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Function(models.Model):
    name = models.CharField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return str(self.pk)


class Group(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return str(self.pk)


class TypeFunction(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    hierarchy = models.IntegerField()

    def __str__(self):
        return str(self.pk)


class TypeGroup(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Anime(models.Model):
    title = models.CharField(max_length=255)
    character_name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Question(models.Model):
    category = models.IntegerField()
    question_sentence = models.TextField()

    def __str__(self):
        return str(self.pk)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_sentence = models.TextField()
    point = models.IntegerField()

    def __str__(self):
        return str(self.pk)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


# ================================= 動物 ===============================================

class AnimalResult(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    head = models.TextField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.pk)


# ================================= ポケモン ===============================================


class PokemonResult(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    head = models.TextField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Pokemon(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)


# ================================= RPG ===============================================

class RpgResult(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    head = models.TextField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.pk)
