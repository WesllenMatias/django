"""sys_inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from inventory.views import list, listExit, EntForm, SaiForm, CatForm, LjForm, FabForm, ControlForm, listControleti
from inventory.views import SetForm, home, registro
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls, name='url_adm'),
    path('', LoginView.as_view(), name='url_login'),
    path('home/', home,  name='url_home'),
    path('registro/', registro, name='url_registro'),
    path('list/', list, name='url_list'),
    path('saidas/', listExit, name='url_list_saida'),
    path('cadEntrada/', EntForm, name='url_cadEntrada'),
    path('cadSaida/', SaiForm, name='url_cadSaida'),
    path('cadCategoria/', CatForm, name='url_cadCategorias'),
    path('cadLoja/', LjForm, name='url_cadLojas'),
    path('cadFabricante/', FabForm, name='url_cadFabricantes'),
    path('cadControleti/', ControlForm, name='url_cadControleti'),
    path('listControleti/', listControleti, name='url_listControleti'),
    path('cadSetor', SetForm, name='url_cadSetor'),
    path('logout/', LogoutView.as_view(next_page='url_login'), name="url_logout")
]
