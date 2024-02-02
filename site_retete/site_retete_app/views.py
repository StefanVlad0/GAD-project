from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Reteta
from .forms import AdaugaRetetaForm
# Create your views here.


def lista_retete(request):
    # retete = Reteta.objects.all()
    retete = [
        {'nume': 'Pui cu legume', 'timp': '30 minute', 'dificultate': 'Ușor', 'ingrediente': 'Pui, legume'},
        {'nume': 'Paste Carbonara', 'timp': '20 minute', 'dificultate': 'Mediu',
         'ingrediente': 'Paste, ou, bacon, parmezan'},
        # Adăugați mai multe rețete aici
    ]
    return render(request, 'lista_retete.html', {'retete': retete})


def home(request):
    retete = Reteta.objects.all()
    # retete = [
    #     {'nume': 'Pui cu legume', 'timp': '30 minute', 'dificultate': 'Ușor', 'ingrediente': 'Pui, legume'},
    #     {'nume': 'Paste Carbonara', 'timp': '20 minute', 'dificultate': 'Mediu',
    #      'ingrediente': 'Paste, ou, bacon, parmezan'},
    #     # Adăugați mai multe rețete aici
    # ]
    return render(request, "home.html", {'retete': retete})

def adauga_reteta(request):
    if request.method == 'POST':
        form = AdaugaRetetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdaugaRetetaForm()

    return render(request, 'adauga_reteta.html', {'form': form})

def reteta_view(request, id_reteta):
    reteta= get_object_or_404(Reteta, pk=id_reteta)
    return render(request, 'vizualizeaza_reteta.html', {'reteta': reteta})

def reteta_update(request, id_reteta):
    reteta= get_object_or_404(Reteta, pk=id_reteta)
    form = AdaugaRetetaForm(request.POST or None, instance=reteta)
    if form.is_valid():
        form.save()
        return redirect(f'/reteta/{id_reteta}')
    return render(request, 'modifica_reteta.html', {'form':form})

def reteta_delete(request, id_reteta):
    reteta = get_object_or_404(Reteta, pk=id_reteta)
    reteta.delete()
    return redirect('home')
