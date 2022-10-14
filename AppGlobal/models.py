from django.db import models
from django.contrib.auth.models import User
from AppGlobal.choices import tipos

# Create your models here.
class Blog(models.Model):
   titulo = models.CharField(max_length=20)
   descripcion = models.CharField(max_length=50)
   body = models.TextField(max_length=5000)
   publish_date = models.DateTimeField('published date')
   image = models.ImageField(upload_to='imagenes', null = True, blank = True)
   tipo = models.CharField(max_length=12, choices=tipos)
   
class Autores(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"username:{self.username} - email:{email}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)