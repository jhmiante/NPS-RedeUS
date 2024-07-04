from django.urls import path

from .views import index_view, nps_view, nps_fim

urlpatterns = [
    path("", index_view, name='index_view'),

    path("nps/", nps_view, name='nps_view'),
    path("nps/<int:filial>/", nps_view, name='nps_view'),
    path("nps/obrigado/", nps_fim, name='nps_fim'),
]