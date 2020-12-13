from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

from finxi_demandas import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Usuários devem informar um E-mail válido!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


SIM_NAO_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)


class Peca(models.Model):
    """ Manutenção do Cadastro de Peças """
    codigo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    urgente = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='Não')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao}"


class Anunciante(models.Model):
    """ Manutenção do Cadastro de Anunciantes """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, )
    telefone = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField("Celular", max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    endereco = models.CharField("Endereço", max_length=60, blank=True, null=True)
    complemento = models.CharField("Complemento", max_length=60, blank=True, null=True)
    numero = models.CharField("Número", max_length=20, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField("CEP", max_length=9, null=True, blank=True, )
    estado = models.CharField("UF", max_length=2, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True, default='Brasil')

    def __str__(self):
        return self.nome


STATUS_CHOICES = (
    ('Aberta', 'Aberta'),
    ('Finalizada', 'Finalizada'),
)


class Demanda(models.Model):
    anunciante = models.ForeignKey(Anunciante, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Aberta')
