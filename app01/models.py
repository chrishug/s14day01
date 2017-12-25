from django.db import models

# Create your models here.

class Group(models.Model):
    caption = models.CharField(max_length=64,unique=True)

class UserInfo(models.Model):
    username = models.CharField(max_length=32,unique=True,null=False)
    password = models.CharField(max_length=128,null=False)
    email = models.EmailField(max_length=32,null=True)
    group = models.ForeignKey(Group,default=1)
