from django.db import models

from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)

class Maps(models.Model): 
    # name = models.CharField(max_length=50) 
    maps_Main_Img = models.FileField(upload_to='images/') 
