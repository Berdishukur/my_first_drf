from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    author=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title



class Unversitetlar(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
class Yunalishlar(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    unversitet=models.ForeignKey(Unversitetlar,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
class Fanlar(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    yunalish=models.ForeignKey(Yunalishlar,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.name







