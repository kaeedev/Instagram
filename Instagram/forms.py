from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from profiles.models import UserProfile

class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) #Para que el campo contraseña sean asteriscos al escribir
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'password'
        ]

    #Esto es para cuando el formulario se envie, guarde la contraseña al usuario
    def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()

             #Para crear un nuevo usuario con un perfil asociado
            user_profile = UserProfile(user=user)
            user_profile.save()
            return user


class LoginForm(forms.Form):
     username = forms.CharField(label='Email o nombre de usuario')
     password = forms.CharField(label='Password', widget=forms.PasswordInput())

