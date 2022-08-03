from msilib.schema import Error
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=10,null=False)
    cost = models.PositiveIntegerField(null=False)
    number = models.PositiveIntegerField(null=False)
    create = models.DateTimeField(auto_now=True)
    note = models.TextField(null=True ,default='note: ')

    class Meta :
        ordering = ["-create"]

    def __str__(self):
        return self.name

class sales(models.Model):
    item = models.ForeignKey(item,on_delete=models.SET_NULL,null=True)
    cost = models.PositiveIntegerField(null=False ,default='0')
    number = models.PositiveIntegerField(null=False)
    create = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ["-create"]
        
    def __str__(self):
        try:
            return self.item.name
        except:
            return 'deleted item'


