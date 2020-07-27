from django.db import models

# Create your models here.
class ComplaintInfo(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True,null=True)
    year=models.CharField(max_length=90)
    reg_no=models.CharField(max_length=9, null=True)
    block=models.CharField(max_length=10, null=True)
    room_no=models.IntegerField(unique=True)
    complaintbox=models.TextField(max_length=255)

    def __str__(self):
        return self.name

class WardenInfo(models.Model):
    image=models.ImageField(upload_to="media", blank=True)
    warden_name=models.CharField(max_length=255,null=True)
    designation=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=255, null=True)
    block = models.CharField(max_length=10, null=True)
    contact=models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.warden_name
