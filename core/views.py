from django.shortcuts import render, redirect, get_object_or_404

from .models import NPS, DadosConfig

def index_view(request):
    return redirect('nps_view')
    return render(request, 'index.html')


def download_app(request, tipo):
    """
    Tipo 1: App Store
    Tipo 2: Play Store
    """

    if tipo == 1:
        link = 'https://apps.apple.com/br/app/petrobras-premmia/id1299170535'
        key = 'Aplicativo: App Store'
    elif tipo == 2:
        link = 'https://play.google.com/store/apps/details?id=br.com.petrobras.br.ma02'
        key = 'Aplicativo: Play Store'
    else:
        return redirect('nps_view')
    
    obj = DadosConfig.objects.filter(key=key)
    if obj.exists():
        obj = obj.first()
    else:
        obj = DadosConfig(key=key, value=0)

    obj.value = int(obj.value) + 1
    obj.save()

    return redirect(link)


def nps_view(request, filial=1):
    if request.method == 'POST':
        atendimento = int(request.POST.get('atendimento', 5))
        apresentacao = int(request.POST.get('apresentacao', 5))
        qualidade = int(request.POST.get('qualidade', 5))
        nome = request.POST.get('nome', '-')
        email = request.POST.get('email', '-')
        observacao = request.POST.get('observacao', '-')

        obj = NPS(
            filial=filial,
            atendimento=atendimento,
            apresentacao=apresentacao,
            qualidade=qualidade,
            nome=nome,
            email=email,
            observacao=observacao
        )

        obj.save()

        if atendimento + apresentacao + qualidade < 12:
            return redirect ('nps_detalhe', pk=obj.pk)

        return redirect('nps_fim')
    return render(request, 'nps.html')


def nps_detalhe(request, pk):
    obj = get_object_or_404(NPS, pk=pk)
    
    if request.method == 'POST':
        detalhes = request.POST.get('detalhes', '-')
        obj.detalhes = detalhes
        obj.save()

        return redirect('nps_fim')
    return render(request, 'nps_detalhe.html')


def nps_fim(request):    
    return render(request, 'nps_fim.html')
