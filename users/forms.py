from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import  forms

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone")