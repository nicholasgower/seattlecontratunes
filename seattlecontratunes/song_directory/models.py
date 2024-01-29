


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


from .constants.report_choices import report_choices #Reasons why someone might report content.
from .constants.choices import item_availability_choices #Possible states of an item's availability.
class Report(models.Model):
    '''Model that stores reports of rule violations from user.'''
    name=models.CharField(max_length=128)
    url=models.CharField(max_length=128)
    reason=models.CharField(choices=report_choices,max_length=128)
    elaboration=models.CharField(max_length=4000)
    email=models.EmailField()
    submitted_time=models.DateTimeField(default=timezone.now)
    
    uploader=models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    resolved=models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return "From: {}, Reason:{}, Time:{}".format(self.name,self.reason,self.submitted_time)



    
class UserContent(models.Model):
    """ Class representing a piece of user-uploaded content with a dedicated page
     Rules of User-uploaded content: 
       1. All content can be made public, private, or unlisted
       2. Nothing the user deletes themselves should be deleted from the database.
          It should only be hidden from non-admins.
    """
    url_code=models.UUIDField(default=uuid4)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=4000,blank=True)
    availability=models.CharField(choices=item_availability_choices,default="public",max_length=10)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)


class Song(models.Model):
    '''Model for Song object. On the website, these are called tunes, but due to an initial
    misunderstanding of the differences between tunes and songs, they are called "songs" in
    the source code.
    '''
    url_code=models.UUIDField(default=uuid4)
    name=models.TextField(max_length=200)
    description=models.TextField(max_length=4000,blank=True)
    availability=models.CharField(choices=item_availability_choices,default="public",max_length=10)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    abc=models.CharField(max_length=12000)
    
    uploaded_time=models.DateTimeField(default=timezone.now)
    #likes=models.IntegerField(default=0)
    
    
    
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



    
class SetListEntry(models.Model):
    url_code=models.UUIDField(default=uuid4)
    song_id=models.ForeignKey(Song,on_delete=models.CASCADE)
    #SetList=models.ForeignKey(SetList,on_delete=models.CASCADE)
    #previous=models.ForeignKey('self',blank=True,null=True,on_delete=models.SET_NULL)
    next=models.ForeignKey('self',blank=True,null=True,on_delete=models.SET_NULL)
    
   # def __str__(self):
   #     return Song.item.get(song_id)

class SetList(models.Model):
    """ Set lists are structured like a linked list: To reconstruct the setlist:
        1. Get the root entry from SetList:
        2. Get the next entry until next=null 
        
    """
    url_code=models.UUIDField(default=uuid4)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=4000,blank=True)
    availability=models.CharField(choices=item_availability_choices,default="public",max_length=10)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_time=models.DateTimeField(default=timezone.now)
    
    
    
    root_entry=models.ForeignKey(SetListEntry,on_delete=models.CASCADE)
    def __str__(self):
        return "Set List: {}".format(super.name)
        
    
class Medley(models.Model):
    ''' 
    Model representing a medley of 2-3 tunes played during a particular dance.
    '''
    
    
    url_code=models.UUIDField(default=uuid4)
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    Tune1=models.CharField(max_length=200)
    Tune2=models.CharField(max_length=200,blank=True, default="")
    Tune3=models.CharField(max_length=200,blank=True,default="")
    
    
    
    uploaded_time=models.DateTimeField(default=timezone.now)
    
    earliest_play=models.DateField(null=True,blank=True)
    latest_play=models.DateField(null=True,blank=True)
    
    earliest_play_legacy=models.CharField(max_length=32,blank=True)
    latest_play_legacy=models.CharField(max_length=32,blank=True)
    
    
    bands=models.CharField(max_length=200,blank=True)
    keys=models.CharField(max_length=32,blank=True)
    notes=models.CharField(max_length=4000,blank=True)
    additional_notes=models.CharField(max_length=4000,blank=True)
    medley_type=models.CharField(choices=medley_categories,max_length=200)
    
    
    
    availability=models.CharField(choices=item_availability_choices,default="public",max_length=10)
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
    def getTuneNames(id):
        this=Medley.objects.get(id=id)
        return [this.Tune1,this.Tune2,this.Tune3]
 
           