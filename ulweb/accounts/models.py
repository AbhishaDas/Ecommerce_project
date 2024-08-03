from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class UserInfo(AbstractUser):
    phone = models.CharField(max_length=50, default='')
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='userinfo_set',
        related_query_name='userinfo'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='userinfo_set',
        related_query_name='userinfo'
    )
    
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

     

