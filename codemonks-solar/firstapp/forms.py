from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from firstapp.models import Maps 


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class MapsForm(forms.ModelForm): 
    maps_Main_Img=forms.FileField(label="Map Image", required=True)
    # name=forms.CharField(label="hi", required=False)
    class Meta: 
        model = Maps 
        
        fields = ['maps_Main_Img']       
