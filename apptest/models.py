from django.db.models.deletion import CASCADE
from apptest.forms import CHOICE_LIST
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entity(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
	    return self.name

class Engagement(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    username = models.CharField(max_length=16)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    current_status = models.CharField(max_length=1, choices=CHOICE_LIST)
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    
    def __str__(self):
	    return self.name
 
