from django.db import models


class History(models.Model):
    s = models.CharField(max_length=50)
