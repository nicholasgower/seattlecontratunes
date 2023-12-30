from django.test import TestCase
from .models import Song, Medley
from django.contrib.auth.models import User
# Create your tests here.

class MedleyTuneTestCase(TestCase):
    
    def setUp(self):
        User.objects.create(id=1)
        Song.objects.create(name="One",abc="test",uploader_id=1)
        Medley.objects.create(Tune1="One",uploader_id=1)
        pass
    def test_medley_tune_to_tune(self):
        ''' This test seeks to test if when a tune is referenced in a medley,
        it will find its matching tune in the Song database.
        
        
        
        '''
        for MedleyInstance in Medley.objects.all():
            for Tune in Medley.getTuneNames(id=MedleyInstance.pk):
                #print(len(Song.objects.filter(name__icontains=Tune)))
                self.assertEqual(len(Song.objects.filter(name__icontains=Tune))>0,True)
    