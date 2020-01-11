from django.db import models

# Create your models here.

class Member(models.Model):
    member_image = models.ImageField(upload_to='images/')
    member_name = models.CharField(max_length=50)