from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=100)
    dt_criacao_cat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_cat

class Fabricante(models.Model):
    dt_criacao_fab = models.DateTimeField(auto_now_add=True)
    nome_fab = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_fab

class Loja(models.Model):
    dt_criacao_lj = models.DateTimeField(auto_now_add=True)
    nome_lj = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_lj

class Entrada(models.Model):
    dt_criacao_ent = models.DateTimeField(auto_now_add=True)
    dt_entrada = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    n_serie = models.IntegerField(null=True, blank=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    qtd_entrada = models.IntegerField()
    lj_origem = models.ForeignKey(Loja, on_delete=models.CASCADE)
    observacao = models.TextField()

    def __str__(self):
        return self.descricao

class Saida(models.Model):
    dt_criacao_sai = models.DateTimeField(auto_now_add=True)
    dt_saida = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    n_serie = models.IntegerField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    qtd_saida = models.IntegerField()
    lj_destino = models.ForeignKey(Loja, on_delete=models.CASCADE)
    observacao = models.TextField()

    def __str__(self):
        return self.descricao

class controleti(models.Model):
    dt_criacao_ti = models.DateTimeField(auto_now_add=True)
    Ip_Address = models.GenericIPAddressField(protocol='Ipv4')
    Mac = models.CharField(max_length=17)
    Hostname = models.CharField(max_length=80)
    Setor = models.CharField(max_length=80)
    Responsavel = models.CharField(max_length=120)
    Contato = models.CharField(max_length=120)
    Observacao = models.TextField(max_length=300)
    Servico = models.CharField(max_length=120)

    def __str__(self):
        return self.Hostname


