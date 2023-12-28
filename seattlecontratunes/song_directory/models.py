


# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


medley_categories=[
    ("Contra","Contra"),
    ("Unplayed","Unplayed Contra"),
    ("Waltz","Waltz"),
    ("Polka","Polka"),
    ("English Ceildh","English Ceildh"),
    ("Northumbrian Pipe and Fiddle","Northumbrian Pipe and Fiddle")

    ]

#class User(AbstractUser):
#    pass




class Version(models.Model):
    major=models.IntegerField(default=0)
    minor=models.IntegerField(default=0)
    patch=models.IntegerField(default=0)
    details=models.TextField(default="")
    date=models.DateTimeField()
    def __str__(self):
        return "{}.{}.{}".format(self.major,self.mino,self.patch)
    def set_value(self,str):
        nums=str.split(".")
        self.major=nums[0]
        self.minor=nums[1]
        self.patch=nums[2]

#class CommentSection(models.Model):
#    pass
#    #id=models.UUIDField(primary_key=True,default=uuid4)    
#        
#class Comment(models.Model):
#    url_code=models.UUIDField(default=uuid4)
#    
#    comment_section=models.ForeignKey(CommentSection, on_delete=models.CASCADE)
#    uploader_id=models.ForeignKey(User, on_delete=models.CASCADE)
#    
#    class Meta:
#        permissions=[("can_delete_own_comment","Can delete comments uploaded by self")]

#class CommentLike(models.Model):
#    user=models.ForeignKey(, on_delete=models.CASCADE)



class Song(models.Model):
    '''Model for Song object. On the website, these are called tunes, but due to an initial
    misunderstanding of the differences between tunes and songs, they are called "songs" in
    the source code
    '''
    
    url_code=models.UUIDField(default=uuid4)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=4000,blank=True)
    abc=models.CharField(max_length=4000)
    
    uploaded_time=models.DateTimeField(default=datetime.datetime.now())
    #likes=models.IntegerField(default=0)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    #def was_published_recently(self):
    #    now=timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #def is_fakebook(self,id):
    #    self_abc=self.get(id=id).abc
    #    return 
    
    
    class Meta:
        
        permissions=[("can_delete_own_song","Can delete songs uploaded by self")]
    #def findSongs(search):
    #    return super().objects.filter(name__contains=search)
    def changedClef(self,id,clef="bass"):  
        self_abc=self.get(id=id).abc
        clef_index=self_abc.index("\nK:")
        next_newline=self_abc.index("\n",clef_index+1)
        injection=" clef={}".format(clef)
        return "".join((self_abc[:next_newline],injection,self_abc[next_newline:]))



        
    
class Medley(models.Model):
    ''' 
    Model representing a medley of 2-3 tunes played during a particular dance.
    '''
    
    
    url_code=models.UUIDField(default=uuid4)
    Tune1=models.CharField(max_length=200)
    Tune2=models.CharField(max_length=200,blank=True, default="")
    Tune3=models.CharField(max_length=200,blank=True,default="")
    uploaded_time=models.DateTimeField(default=datetime.datetime.now())
    
    earliest_play=models.DateField(null=True,blank=True)
    latest_play=models.DateField(null=True,blank=True)
    
    earliest_play_legacy=models.CharField(max_length=32,blank=True)
    latest_play_legacy=models.CharField(max_length=32,blank=True)
    
    
    bands=models.CharField(max_length=200,blank=True)
    keys=models.CharField(max_length=32,blank=True)
    notes=models.CharField(max_length=4000,blank=True)
    additional_notes=models.CharField(max_length=4000,blank=True)
    medley_type=models.CharField(choices=medley_categories,max_length=200)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{}, {}, {}".format(self.Tune1,self.Tune2,self.Tune3)
    class Meta:
        permissions=[("can_delete_own_medley","Can delete medleys uploaded by self")]
    def getTuneLinks(id):
        out=[]
        this=Medley.objects.get(id=id)
        for tune in [this.Tune1, this.Tune2, this.Tune3]:
            
            
            links=Song.objects.filter(name__contains=tune.strip())
            out.append(links)
        return out
 
           