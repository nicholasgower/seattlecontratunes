


# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


medley_categories=[
    ("Contra","Contra"),
    ("Unplayed","Unplayed Contra"),
    ("Waltz","Waltz"),
    ("Polka","Polka"),
    ("English Ceildh","English Ceildh"),
    ("Northumbrian Pipe and Fiddle","Northumbrian Pipe and Fiddle")

    ]


    

class Song(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=4000,blank=True)
    abc=models.CharField(max_length=4000)
    
    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def is_fakebook(self):
        pass
    
    
class Medley(models.Model):
    Tune1=models.CharField(max_length=200)
    Tune2=models.CharField(max_length=200,blank=True, default="")
    Tune3=models.CharField(max_length=200,blank=True,default="")
    
    earliest_play=models.DateField(null=True,blank=True)
    latest_play=models.DateField(null=True,blank=True)
    bands=models.CharField(max_length=200,blank=True)
    keys=models.CharField(max_length=32,blank=True)
    comments=models.CharField(max_length=4000,blank=True)
    additional_notes=models.CharField(max_length=4000,blank=True)
    medley_type=models.CharField(choices=medley_categories,max_length=200)
    
    def __str__(self):
        return "{}, {}, {}".format(self.Tune1,self.Tune2,self.Tune3)