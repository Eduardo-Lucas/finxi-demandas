from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Peca, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


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
