from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=100, verbose_name="Nome da Categoria")
    dt_criacao_cat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_cat

class Fabricante(models.Model):
    dt_criacao_fab = models.DateTimeField(auto_now_add=True)
    nome_fab = models.CharField(max_length=100, verbose_name="Nome do Fabricante")

    def __str__(self):
        return self.nome_fab

class Loja(models.Model):
    dt_criacao_lj = models.DateTimeField(auto_now_add=True)
    nome_lj = models.CharField(max_length=20, default="", verbose_name="Descrição da Loja")

    def __str__(self):
        return self.nome_lj

class Setor(models.Model):
    dt_criacao_setor = models.DateTimeField(auto_now_add=True)
    nome_setor = models.CharField(max_length=20, default="", verbose_name="Descrição do Setor")

    def __str__(self):
        return self.nome_setor

class Entrada(models.Model):
    dt_criacao_ent = models.DateTimeField(auto_now_add=True)
    dt_entrada = models.DateTimeField(verbose_name="Data da Entrada")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name="Categoria")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    n_serie = models.IntegerField(null=True, blank=True, verbose_name="Nº de Série")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, verbose_name="Fabricante")
    qtd_entrada = models.IntegerField(verbose_name="Qtd. Entrada")
    lj_origem = models.ForeignKey(Loja, on_delete=models.CASCADE, verbose_name=" Loja Origem")
    observacao = models.TextField(verbose_name="Observação")

    def __str__(self):
        return self.descricao

class Saida(models.Model):
    dt_criacao_sai = models.DateTimeField(auto_now_add=True)
    dt_saida = models.DateTimeField(verbose_name="Data de Saída")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    n_serie = models.IntegerField(verbose_name="Nº de Série")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, verbose_name="Fabricante")
    qtd_saida = models.IntegerField(verbose_name="Qtd. Saída")
    lj_destino = models.ForeignKey(Loja, on_delete=models.CASCADE,verbose_name="Loja Destino")
    observacao = models.TextField(verbose_name="Observação")

    def __str__(self):
        return self.descricao

class controleti(models.Model):
    dt_criacao_ti = models.DateTimeField(auto_now_add=True)
    Ip_Address = models.GenericIPAddressField(protocol='Ipv4', verbose_name="Endereço IP")
    Mac = models.CharField(max_length=17)
    Hostname = models.CharField(max_length=80, verbose_name="Nome da Máquina")
    setor = models.CharField(max_length=30, verbose_name="Setor", default="")
    Loja = models.ForeignKey(Loja, on_delete=models.CASCADE,default="")
    Responsavel = models.CharField(max_length=120, verbose_name="Responsável")
    Contato = models.CharField(max_length=120)
    Observacao = models.TextField(max_length=300, verbose_name="Observação")
    Servico = models.CharField(max_length=120, verbose_name="Serviços")

    def __str__(self):
        return self.Hostname


