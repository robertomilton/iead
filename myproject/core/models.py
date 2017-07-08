from django.db import models
from localflavor.br.br_states import STATE_CHOICES

CIVIL = (
    ('so', 'solteiro'),
    ('ca', 'casado'),
    ('di', 'divorciado'),
    ('ou', 'outros'),
)

ESCOLARIDADE = (
    ('efi', 'Ensino Fundamental Incompleto'),
    ('efc', 'Ensino Fundamental Completo'),
    ('emi', 'Ensino Médio Incompleto'),
    ('emc', 'Ensino Médio Completo'),
    ('esi', 'Ensino Superior Incompleto'),
    ('esc', 'Ensino Superior Completo'),
    ('ou', 'outros'),
    ('ind', 'indefinido'),
)

ADMITIDO = (
    ('bat', 'batismo'),
    ('ca', 'carta'),
    ('acl', 'aclamação'),
    ('ind', 'indefinido'),
)


class Person(models.Model):
    nome = models.CharField(max_length=100)
    data_consagracao = models.DateField(
        'data de consagração', null=True, blank=True)
    data_apresentacao = models.DateField(
        'data de apresentação', null=True, blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    cartao = models.BooleanField('cartão')
    funcao = models.CharField('função', max_length=100, null=True, blank=True)
    nome_pai = models.CharField(
        'nome do pai', max_length=100, null=True, blank=True)
    nome_mae = models.CharField(
        'nome da mãe', max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(
        'data de nascimento', null=True, blank=True)
    naturalidade = models.CharField(max_length=100, null=True, blank=True)
    estado_nascimento = models.CharField(
        'estado', max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    pais_nascimento = models.CharField(
        'país de nascimento', max_length=50, default='Brasil')
    estado_civil = models.CharField(
        'estado civil', max_length=2, choices=CIVIL, default='ou', null=True, blank=True)
    rg = models.CharField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    escolaridade = models.CharField(
        max_length=3, choices=ESCOLARIDADE, default='ind', null=True, blank=True)
    profissao = models.CharField(
        'profissão', max_length=100, null=True, blank=True)
    data_batismo = models.DateField('data de batismo', null=True, blank=True)
    igreja_cidade = models.CharField(
        'igreja cidade', max_length=100, null=True, blank=True)
    admitido = models.CharField(
        'admitido por', max_length=3, choices=ADMITIDO, default='ind', null=True, blank=True)
    data_admissao = models.DateField('data de admissão', null=True, blank=True)
    endereco = models.CharField(
        'endereço', max_length=150, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(
        'UF', max_length=2, choices=STATE_CHOICES, default='SP', null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fone = models.CharField(max_length=14, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)
    # foto

    class Meta:
        ''' É uma classe Builtin do Django com recursos adicionais '''
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        ''' Retorna a pessoa ao invés de Person object '''
        return self.nome
