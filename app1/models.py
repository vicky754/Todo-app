from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    title=models.CharField(max_length=30)
    discription=models.CharField(max_length=100)
    date=models.DateField()
    done=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
    	return self.title