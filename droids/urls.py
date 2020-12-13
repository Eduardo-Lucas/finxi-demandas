from django.urls import path

from .views import PecaList, PecaDetail

urlpatterns = [
    path("api/pecas/", PecaList.as_view()),
    path("api/pecas/<int:pk>/", PecaDetail.as_view()),
]
