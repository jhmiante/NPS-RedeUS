from django.shortcuts import render, redirect

from .models import NPS

def index_view(request):
    return render(request, 'index.html')


def nps_view(request, filial=1):
    if request.method == 'POST':
        atendimento = int(request.POST.get('atendimento', 0))
        apresentacao = int(request.POST.get('apresentacao', 0))
        qualidade = int(request.POST.get('qualidade', 0))
        nome = request.POST.get('nome', '-')
        email = request.POST.get('email', '-')
        observacao = request.POST.get('observacao', '-')

        obj = NPS(
            atendimento=atendimento,
            apresentacao=apresentacao,
            qualidade=qualidade,
            nome=nome,
            email=email,
            observacao=observacao
        )

        obj.save()

        return redirect('nps_fim')
    return render(request, 'nps.html')


def nps_fim(request):
    return render(request, 'nps_fim.html')
