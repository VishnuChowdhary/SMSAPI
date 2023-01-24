from django.db import models

# Create your models here.

class Students(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=80, blank=False , null=False)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=150)
    department = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.first_name