from django import forms
from apps.users.models import User

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
    