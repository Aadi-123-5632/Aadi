from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.CharField(max_length=122)
    def __str__(self):
        return self.name

# Create your models here.
