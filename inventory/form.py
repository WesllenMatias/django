from django.forms import ModelForm
from inventory.models import Entrada, Saida, Categoria, Loja, Fabricante, controleti, Setor


class EntradaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ['dt_entrada', 'descricao', 'categoria', 'modelo', 'n_serie', 'fabricante', 'qtd_entrada', 'lj_origem', 'observacao']

class SaidaForm(ModelForm):
    class Meta:
        model = Saida
        fields = ['dt_saida', 'descricao', 'categoria', 'modelo', 'n_serie', 'fabricante', 'qtd_saida', 'lj_destino', 'observacao']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_cat']

class LojaForm(ModelForm):
    class Meta:
        model = Loja
        fields = ['nome_lj']

class FabricanteForm(ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nome_fab']

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['nome_setor']

class ControletiForm(ModelForm):
    class Meta:
        model = controleti
        fields = ['Hostname', 'Ip_Address', 'Mac', 'Setor', 'Loja', 'Responsavel', 'Contato', 'Servico', 'Observacao']