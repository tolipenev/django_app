from django.db import models

# Create your models here.

class Entity(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()


class Engagement(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    username = models.CharField(max_length=16)
    entity_link = models.ForeignKey('Entity', on_delete=models.CASCADE)