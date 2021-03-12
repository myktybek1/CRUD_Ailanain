from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = 'employee'
# Create your models here.
