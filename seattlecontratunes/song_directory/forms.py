from django import forms

class SongForm(forms.Form):
    name=forms.CharField(label="Name",max_length=200)
    abc=forms.CharField(label="ABC",max_length=4000)
    description=forms.CharField(label="Description",max_length=4000,required=False)