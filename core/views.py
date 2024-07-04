from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def nps_view(request, filial=1):
    return render(request, 'nps.html')
