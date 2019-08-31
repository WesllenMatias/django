from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Entrada
from .models import Saida
from .models import Categoria
from .models import controleti
from .form import EntradaForm, SaidaForm, CategoriaForm, LojaForm, FabricanteForm, ControletiForm, SetorForm
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def registro(request):
    if request.method == "POST":
        reg = UserCreationForm(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('url_login')
    else:
        reg = UserCreationForm()
    return render (request, 'registro.html', {'reg':reg})

@login_required
def home(request):
    return render(request, 'listControleti.html')

@login_required
def list(request):
    data ={}
    data ['Entradas'] = Entrada.objects.all()
    return render(request, 'list.html', data)

@login_required
def listControleti(request):
    data ={}
    data ['Controleti'] = controleti.objects.all()
    return render(request, 'listControleti.html', data)

@login_required
def listExit(request):
    data = {}
    data['Saidas'] = Saida.objects.all()
    return render(request, 'saidas.html', data)

@login_required
def listCategoria(request):
    data = {}
    data['Categorias'] = Categoria.objects.all()
    return render(request, 'cadCategorias.html', data)

@login_required
def EntForm(request):
    data = {}
    form_entradas = EntradaForm(request.POST or None)

    if form_entradas.is_valid():
        form_entradas.save()
        return redirect('url_cadEntrada')

    data['form_entradas'] = form_entradas
    return render(request, 'cadEntrada.html', data)

@login_required
def SaiForm(request):
    data1 = {}
    form_saidas = SaidaForm(request.POST or None)

    if form_saidas.is_valid():
        form_saidas.save()
        return redirect('url_cadSaida')

    data1['form_saidas'] = form_saidas
    return render(request, 'cadSaida.html', data1)

@login_required
def CatForm(request):
    data = {}
    form_categorias = CategoriaForm(request.POST or None)

    if form_categorias.is_valid():
        form_categorias.save()
        return redirect('url_cadCategorias')

    data['form_categorias'] = form_categorias
    return render(request, 'cadCategorias.html', data)

@login_required
def LjForm(request):
     data = {}
     form_lj = LojaForm(request.POST or None)

     if form_lj.is_valid():
         form_lj.save()
         return redirect('url_cadLojas')
     data['form_lj'] = form_lj
     return render(request, 'cadLojas.html', data)

@login_required
def FabForm(request):
     data = {}
     form_fab = FabricanteForm(request.POST or None)

     if form_fab.is_valid():
         form_fab.save()
         return redirect('url_cadFabricantes')

     data['form_fab'] = form_fab
     return render(request, 'cadFabricantes.html', data)

@login_required
def SetForm(request):
    data = {}
    form_setor = SetorForm(request.POST or None)

    if form_setor.is_valid():
        form_setor.save()
        return redirect('url_cadSetor')

    data['form_setor'] = form_setor
    return render(request,'cadSetor.html', data)

def qtdTotal(request):
    data = {}
    data['Total'] = Saida.objects.all(Sum(qtdTotal))

@login_required
def ControlForm(request):
    data = {}
    form_control = ControletiForm(request.POST or None)

    if form_control.is_valid():
        form_control.save()
        return redirect('url_cadControleti')

    data['form_control'] = form_control
    return render(request, 'cadControleti.html', data)
