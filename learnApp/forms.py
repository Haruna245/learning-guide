from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserAccount


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserAccount
        fields = ('email','firstname','lastname','userType','phonenumber')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserAccount
        fields = ('email','firstname','lastname','userType','phonenumber')
