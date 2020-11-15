from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserTravel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=20)
    places = models.TextField(max_length=1000,null=True,default="")

    def __str__(self):
        return self.username