from django import forms
from listings.models import Band
from listings.models import Announcement

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = "__all__"
        """ exclude = ('active', 'official_page') Pour exclure certains champs du formulaire """

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        exclude = ('band', 'like_new')