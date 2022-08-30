from ast import Pass
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404

from Heroku1.models import Posts, Comentarios, Avatar
from Heroku1.forms import *

from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy 



def Inicio(request):

    #titulos = list(Posts.objects.all())

    avatars = Avatar.objects.filter(user=request.user.id)
    avatares = avatars.order_by('-pk')
    try:
        avats = avatares[0].imagen.url      
    except:
        avats = None
 
    return render (request, 'Heroku1/index.html') #{'posts':titulos, 'avatar' : avats})

   

class PostLista( ListView):

    model = Posts
    template_name = 'Heroku1/posts_list.html'
    ordering = ['-pk']


class PostDetalle ( LoginRequiredMixin, DetailView):

    model = Posts
    template_name = "Heroku1/posts_detalle.html"

    def get_context_data(self, *arg, **kwargs):

        context = super(PostDetalle, self).get_context_data(**kwargs)
        var = get_object_or_404(Posts, id=self.kwargs['pk'])
        likes_tot = var.total_likes()
        liked = False
        if var.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['likes_totales'] = likes_tot
        context['liked']=liked
        return context


class PostCrear(LoginRequiredMixin, CreateView):

    model = Posts
    success_url = "/pages/"
    form_class = FormPosts


class PostActualizar(LoginRequiredMixin, UpdateView):

    model = Posts
    success_url = "/pages/"
    form_class = EditPosts
    template_name = "Heroku1/posts_update.html"


class PostBorrar(LoginRequiredMixin, DeleteView):
    
    model = Posts
    success_url = "/pages/"


def login_request(request):
    
    titulos = Posts.objects.all()
    if request.method== 'POST':

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data= formulario.cleaned_data

            nombre_usuario = data.get('username')
            contrasenia = data.get('password')

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
                
            else:
                return redirect('Inicio')

        else:
            return render (request, 'Heroku1/login.html', {'errors': ['Datos incorrectos'], 'bool':True})

    else:
        form = AuthenticationForm()
        return render (request, 'Heroku1/login.html', {'form': form})


def register_request(request):
    
    titulos = Posts.objects.all()
    if request.method == 'POST':

        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            print (usuario)
            form.save()
            succes = 'Usuario creado correctamente'
            return render (request, 'Heroku1/register.html', {'var' : succes})
        else:

            return render(request, 'Heroku1/register.html', {'errors':['Datos incorrectos: La contraseña debe ser mayor a 8 caracteres. Al menos una mayuscula. Evite similitudes con el nombre de usuario o correo'], 'posts':titulos})

    else: 
        form=UsuarioRegistroForm()
        return render(request, 'Heroku1/register.html' , {'form':form})


class editar_usuario(generic.UpdateView):
    form_class = Editar_perfil
    template_name= 'Heroku1/editar_perfil.html'
    success_url= reverse_lazy ('Inicio')

    def get_object(self):
        return self.request.user





def Likes(request, pk):
    post = get_object_or_404(Posts, id=request.POST.get('post_id'))
    
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked= True


    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class Cambiar_contraseña(PasswordChangeView):
    form_class = CambioContraseña
    success_url = reverse_lazy('cont_corr')


def contraseña_correct(request):
    return render (request, 'Heroku1/cont_cambio_correct.html')


class CrearComentario(LoginRequiredMixin, CreateView):

    model = Comentarios
    template_name = 'Heroku1/comentario.html'
    form_class = ComentarioForm
    success_url= reverse_lazy('post_list')


    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def sobre_mi (request):
    return render (request, 'Heroku1/sobre_mi.html')



class EditarAvatar(CreateView):
   
    model = Avatar
    template_name = 'Heroku1/editar_avatar.html'
    success_url= reverse_lazy ('Inicio')
    fields= '__all__'

