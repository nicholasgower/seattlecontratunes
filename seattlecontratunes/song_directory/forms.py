from django import forms

from .constants.item_availability_choices import item_availability_choices
class SongForm(forms.Form):
    #form_template_name = "song_form_snippet.html"
    name=forms.CharField(label="Name",max_length=200)
    #abc=forms.TextArea(label="ABC",max_length=4000)
    abc=forms.CharField(label="ABC",max_length=12000,widget=forms.Textarea())
    description=forms.CharField(label="Description",max_length=4000,required=False)
    availability=forms.ChoiceField(label="Availability",choices=item_availability_choices)

class SongEditForm(SongForm):
    #form_template_name = "song_form_snippet.html"
    name=None
    #abc=forms.TextArea(label="ABC",max_length=4000)
    #description=forms.CharField(label="Description",max_length=4000,required=False)
    #availability=forms.ChoiceField(label="Availability",choices=item_availability_choices)    
    

#Report choices taken from Youtube's report form    
from .constants.report_choices import report_choices
    
class ReportForm(forms.Form):
    form_template_name = "song_directory/report_form_snippet.html"
    
    name=forms.CharField(max_length=128)
    url=forms.CharField(label="URL",max_length=128)
    reason=forms.ChoiceField(label="Reason",choices=report_choices)
    elaboration=forms.CharField(label="Elaborate",max_length=4000)
    email=forms.EmailField(label="Email",required=False)