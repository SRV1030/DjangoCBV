from django.db import models
from django.core.urlresolvers import reverse

class School(models.Model):
    name=models.CharField(max_length =256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CBV_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name


# Create your models here.
