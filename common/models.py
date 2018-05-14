from django.db import models


class App(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    logo = models.URLField(null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return str(self.pk)
