from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class User(AbstractUser):
    objects = UserManager()
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,blank=True,null=True)
    avatar = models.ImageField(upload_to="profile",null=True,blank=True)
    
    def __str__(self):
        return self.user        

    
    
    
