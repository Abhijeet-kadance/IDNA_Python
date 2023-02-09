from django.db import models

# Create your models here.

class TestData(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True,null=True)
    
    def __str__(self):
        return self.title