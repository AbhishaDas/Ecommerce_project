
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserInfo(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.password =make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
     

