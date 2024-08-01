from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2')

