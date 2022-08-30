from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from Heroku1.models import *


class FormPosts(forms.ModelForm):
    class Meta:
        model = Posts
        fields= ('titulo', 'subtitulo' ,'contenido', 'imagen', 'autor')

        widgets ={
            'titulo': forms.TextInput(attrs={'class': 'form-control' }),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control' }),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usua', 'type':'hidden' }),
            'contenido': forms.Textarea(attrs={'class': 'form-control' }),

        }

class EditPosts(forms.ModelForm):
    class Meta:
        model = Posts
        fields= ('titulo', 'contenido', 'imagen', 'autor')

        widgets ={
            'titulo': forms.TextInput(attrs={'class': 'form-control' }),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usua', 'type':'hidden' }),
            'contenido': forms.Textarea(attrs={'class': 'form-control' }),
            
        }


class UsuarioRegistroForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Apellido', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm. Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {"username": None}

    def __init__(self, *args, **kwargs):
        super(UsuarioRegistroForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['password1'].widget.attrs['class'] ='form-control'
        self.fields['password2'].widget.attrs['class'] ='form-control'



class Editar_perfil(UserChangeForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(label='Nombre',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Apellido',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class CambioContraseña(PasswordChangeForm):
    
    old_password= forms.CharField(label='Contraseña actual',max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1= forms.CharField(label='Contraseña Nueva',max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label='Confirm. Contraseña',max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class ComentarioForm(forms.ModelForm):
    

    class Meta:
        model = Comentarios
        fields = [ 'usuario' , 'contenido']

        widgets ={
            'usuario' : forms.TextInput(attrs={'class': 'form-control' }),
            'contenido': forms.Textarea(attrs={'class': 'form-control' })  
        }
