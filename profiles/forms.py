from django.forms import ModelForm
from django import forms


class ProfileFollow(forms.Form):
     profile_pk = forms.IntegerField(widget=forms.HiddenInput())
     action = forms.CharField(widget=forms.HiddenInput())

class FollowForm(forms.Form):
    profile_pk = forms.IntegerField(label="Identificador del usuario", widget=forms.HiddenInput())