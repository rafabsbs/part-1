from django.urls import path

from apps.usuarios.views import cadastro

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
]