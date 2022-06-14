from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    sub=models.CharField(max_length=700)
    message=models.CharField(max_length=800)
    def __str__(self):
        return self.name