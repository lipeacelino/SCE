from django.db import models


class Produto(models.Model):
    '''
    codigo, nome, quantidade, preco
    '''
    codigo = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=40)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    #max_digits=5, decimal_place=2

    class Meta:
        verbose_name_plural='Produtos'

    def __str__(self):
        return 'Cod: '+self.codigo + ' - ' + 'Nome: '+self.nome + ' - ' + 'Qtd: '+str(self.quantidade) + ' - ' + ' Preço: '+str(self.preco)
