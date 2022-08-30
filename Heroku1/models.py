from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Posts(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = RichTextField(blank=True, null=True)
    fecha_pub = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='fotos', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likesPost')
    subtitulo = models.CharField(max_length=400)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    usuario = models.CharField(max_length=100)
    post = models.ForeignKey(Posts, related_name='comentarios' , on_delete=models.CASCADE)
    contenido = RichTextField(blank=True, null=True)
    fecha_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.usuario)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

