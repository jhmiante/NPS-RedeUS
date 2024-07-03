from django.db import models


class NPS(models.Model):
    data_inclusao = models.DateField('Data', auto_now_add=True)
    filial = models.IntegerField(default=1)
    nome = models.CharField(max_length=500, null=True, blank=True, default=None)
    email = models.CharField(max_length=500, null=True, blank=True, default=None)    
    atendimento = models.IntegerField(default=0)
    apresentacao = models.IntegerField(default=0)
    qualidade = models.IntegerField(default=0)
    observacao = models.CharField(max_length=2000, null=True, blank=True, default='-')
    detalhes = models.CharField(max_length=2000, null=True, blank=True, default='-')

    class Meta:
        db_table = 'nps'
        verbose_name = "NPS"
        verbose_name_plural = "NPS"
        ordering = ['data_inclusao']
