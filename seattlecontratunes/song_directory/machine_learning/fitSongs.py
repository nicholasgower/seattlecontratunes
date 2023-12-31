# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:57:17 2023

@author: Nicholas
"""
from .models import Song
#import scikit_learn
from sklearn.ensemble import RandomForestClassifier


def fitSongs():
    songs=Song.abc.objects.all()
    clf=RandomForestClassifier(random_state=0)
    
    clf.fit(songs.values_list("name",flat=True),songs.values_list("abc",flat=True))
    
    
    
