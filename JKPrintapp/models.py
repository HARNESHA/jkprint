from django.db import models
from datetime import datetime    

# Create your models here.

class newuser(models.Model):
    created=models.DateTimeField(default=datetime.now, blank=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=50)
    mobile=models.BigIntegerField()

    def __str__(self) -> str:
        return self.firstname

