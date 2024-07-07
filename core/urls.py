from django.urls import path

from .views import index_view, nps_view, nps_detalhe, nps_fim, download_app

urlpatterns = [
    path("", index_view, name='index_view'),

    path("nps/", nps_view, name='nps_view'),
    path("nps/detalhe/<int:pk>/", nps_detalhe, name='nps_detalhe'),
    path("nps/<int:filial>/", nps_view, name='nps_view'),
    path("nps/obrigado/", nps_fim, name='nps_fim'),
    path("download-app/<int:tipo>/", download_app, name='download_app'),
]