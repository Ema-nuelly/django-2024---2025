"""
URL configuration for gestao_de_patrimonio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_gestao_de_patrimonio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('bens/', views.bens, name='bens'),
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('localizacoes/', views.localizacoes, name='localizacoes'),
]
