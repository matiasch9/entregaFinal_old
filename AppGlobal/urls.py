from django.urls import path
from AppGlobal.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index),
    path('recetas/',recetas),
    path('about/',about),
    path('create_autores/',create_autores),
    path('login/', login_request),
    path('perfil/',perfil),
    path('registro/',registro),
    path('logout/', LogoutView.as_view(template_name = 'index.html'), name="Logout" ),
    path('perfil/changeAvatar/', agregarAvatar),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/password/', password),
]