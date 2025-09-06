from django.db import models

# Create your models here.

# Creating company model
class Company(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    about = models.TextField()
    type=models.CharField(max_length=100, choices=(
        ('IT', 'IT'), ('NON IT', 'NON IT'), ('Mobile Phones', 'Mobile Phones')
    ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Creating Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ("Team Leader", "TL"),
        ("Project Manager", "PM"),
        ('Software Engineer', 'SE')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)