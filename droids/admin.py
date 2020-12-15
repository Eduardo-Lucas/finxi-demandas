from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Peca, User, Anunciante, Demanda


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Anunciante)
class AnuncianteAdmin(admin.ModelAdmin):
    list_display = (
        "nome", "telefone", "celular", "cidade", "estado",
    )


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "peca", "quantidade", "status",
    )


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    fields = (
        "codigo", "descricao", "urgente", "data_cadastro", "data_alteracao",
    )
    list_display = (
        "codigo", "descricao", "urgente", "data_cadastro", "data_alteracao",
    )
    readonly_fields = (
        "data_cadastro", "data_alteracao",
    )
