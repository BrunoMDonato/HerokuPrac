from django.contrib import admin
from django.urls import path, include

from Heroku1.views import *

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('', Inicio, name='Inicio'),

    path('pages/', PostLista.as_view(), name='post_list'),
    path('nuevo/', PostCrear.as_view(), name='post_create'),
    path('pages/<pk>', PostDetalle.as_view(), name='post_detail'),
    path('editar/<pk>', PostActualizar.as_view(), name='post_update'),
    path('borrar/<pk>', PostBorrar.as_view(), name='post_delete'),

    path('like/<pk>', Likes, name='like_post' ),

    path('accounts/login', login_request, name= 'Login'),
    path('accounts/signup', register_request, name='Register'),
    path('accounts/logout/', LogoutView.as_view(template_name='Heroku1/logout.html'), name='Logout'),

    path('accounts/profile/', editar_usuario.as_view(), name='editar_perfil'),
    path('accounts/password/', Cambiar_contraseña.as_view(template_name='Heroku1/cambiar_cont.html')),
    path('cont_corr/', contraseña_correct, name='cont_corr'),

    path('pages/<pk>/comentario/', CrearComentario.as_view(), name='agregar_comentario'),
    path('avatar/',EditarAvatar.as_view(), name='Avatar' ),

    path('about/', sobre_mi, name='sobre_mi'),
   

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)