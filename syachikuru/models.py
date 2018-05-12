from django.db import models


class Question(models.Model):
    question_sentence = models.TextField()

    def __str__(self):
        return str(self.pk)


 class Result(models.Model):
    level = models.IntegerField()
    type = models.CharField(max_length=255)
    img_url1 = models.URLField(null=True)
    img_url2 = models.URLField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.pk)


class Candidate(models.Model):
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.pk)


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_number = models.CharField(max_length=255)
    choice_sentence = models.TextField()

    def __str__(self):
        return str(self.pk)


class Answer(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
