from django.db import models


# Create your models here.
class Tickets(models.Model):
    status = models.IntegerField()
    owner = models.IntegerField()
    assignee = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
