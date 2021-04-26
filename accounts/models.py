from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Upload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    option = models.CharField(max_length=50)
    file1 = models.FileField( upload_to="multimedia/")
    date = models.DateField( auto_now=True)

  
    