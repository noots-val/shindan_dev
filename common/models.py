from django.db import models


class App(models.Model):
    app_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    logo = models.URLField(null=True)
    summary = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return str(self.pk)
