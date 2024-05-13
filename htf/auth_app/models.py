from django.db import models
from django.contrib.auth.models import User


    


# Create your models here.



class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.TextField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return self.email
class Bmi(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    weight=models.FloatField()
    height=models.FloatField()
    bmi=models.FloatField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user.username


    


    
