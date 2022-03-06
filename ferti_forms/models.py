from django.db import models

# Create your models here.
class FertilizerData(models.Model):   
    crop=models.CharField(max_length=30,default="rice")
    nitrogen=models.IntegerField()
    potassium=models.IntegerField()
    phosphorous=models.IntegerField()

    def __str__(self):
         return self.crop