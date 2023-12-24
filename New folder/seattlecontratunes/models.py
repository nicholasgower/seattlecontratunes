# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:10:28 2023

@author: Nicholas
"""
from django.db import models
from django.utils import timezone
import datetime


medley_categories=[
    "Contra",
    "Unplayed Contra",
    "Waltz",
    "Polka",
    "English Ceildh",
    "Northumbrian Pipe and Fiddle",
    ""
    ]


    

class Song(models.Model):
    name=models.CharField()
    description=models.CharField()
    abc=models.CharField()
    
    
    
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    
class Medley(models.Model):
    Tune1=models.CharField()
    Tune2=models.CharField()
    Tune3=models.CharField()
    
    earliest_play=models.DateField(null=True)
    latest_play=models.DateField(null=True)
    bands=models.CharField()
    keys=models.CharField()
    comments=models.CharField()
    additional_notes=models.CharField()
    medley_type=models.CharField(choices=medley_categories)