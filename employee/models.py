from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    empid=models.IntegerField(null='True')
    parmanent_address=models.TextField(null='True')
    age=models.IntegerField(null='True')
    dob=models.DateField(auto_now_add=False, auto_now=False, blank=True,null='True')
    country=models.CharField(max_length=256, null='True')
    gender=models.CharField(max_length=50, null='True')
    blood_group=models.CharField(max_length=10, null='True')
    marital_status=models.CharField(max_length=100,null='True')
    citizenship=models.CharField(max_length=50, null='True')
    passport_details=models.CharField(max_length=100, null='True')
    pan_number=models.CharField(max_length=50,null='True')
    aadhaar=models.IntegerField(null='True')
    name_as_per_aadhaar=models.CharField(max_length=100,null='True')
    temporary_address=models.CharField(max_length=500, null='True')
    full_name=models.CharField(max_length=100, null='True')
    

    father_firstname=models.CharField(max_length=100, null='True')
    father_lastname=models.CharField(max_length=100, null='True')
    mother_firstname=models.CharField(max_length=100, null='True')
    mother_lastname=models.CharField(max_length=100, null='True')
    


    def __str__(self):
        return f'{self.user.username} profile'