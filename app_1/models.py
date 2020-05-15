from django.db import models

# Create your models here.
class User(models.Model):
	first_name=models.CharField(max_length=15)
	lest_name=models.CharField(max_length=15)
	age=models.IntegerField(default=15)
	date_bith=models.DateTimeField()
	def __str__(self):
		return self.first_name


class data(models.Model):
	pepole_id=models.ForeignKey(User , on_delete=models.CASCADE)
	pepole_dgree=models.IntegerField(default=15)
	def __str__(self):
		return self.pepole_id

class img(models.Model):
    title=models.CharField(max_length=15)
    text=models.TextField(default=" ")
    many=models.IntegerField(default=0)
    img= models.ImageField(upload_to='images/')
