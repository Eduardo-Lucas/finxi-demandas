"""finxi_demandas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from .views import ping
from droids import views as droids_api

schema_view = get_schema_view(title='Desafio FINXI',
                              url='https://127.0.0.1:8000/api/')

router = routers.DefaultRouter()
router.register('pecas', droids_api.PecaViewSet)
router.register('anunciantes', droids_api.AnuncianteViewSet)
router.register('demandas', droids_api.DemandaViewSet)

urlpatterns = [
    path('schema/', schema_view),
    path('api/', include(router.urls)),
    path('accounts/', include("accounts.urls")),
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),
    path("", include("droids.urls")),
]
