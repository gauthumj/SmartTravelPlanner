from django import forms
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserTravel

class UserInfo(UserCreationForm):

    password1 = forms.CharField(min_length=6, max_length=25, widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(min_length=6, max_length=25, widget=forms.PasswordInput(), required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class MultiplestringField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        super(MultiplestringField, self).__init__(*args, **kwargs)
        self.coerce = str

    def valid_value(self, value):
        return True

class UserTravelForm(forms.Form):
    places = MultiplestringField()
    class Meta:
        model = UserTravel
        fields = ['user','places']


