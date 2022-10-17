from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from AppGlobal.models import Blog

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput())
    password1 = forms.CharField(label="Repetir Contraseña", widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Last Name'}))
    #password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Password"}))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "New password"}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()

## Blog
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('titulo', 'descripcion', 'body', 'image')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }
