from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User, Profile

class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'user', 'gender', 'birth', 'address', 'phone_number', 'image')

# get_user_model()?
ProfileFormset = forms.inlineformset_factory(
    User, Profile, ProfileForm, extra=1, max_num=1, can_delete=False
)
