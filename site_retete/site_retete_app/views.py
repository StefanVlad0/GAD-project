from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Reteta
from .forms import AdaugaRetetaForm, ImportaRetetaForm
from bs4 import BeautifulSoup
import requests
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

def importa_reteta(request):
    if request.method == 'POST':
        form = ImportaRetetaForm(request.POST)
        if form.is_valid():
            link_reteta = form.cleaned_data['link_reteta']
            reteta = extrage_reteta(link_reteta)
            # Salvați reteta în baza de date sau faceți orice altă acțiune dorită
            print(reteta)
            Reteta.objects.create(
                nume=reteta['nume_reteta'],
                timp=reteta['timp'],
                dificultate=str(reteta['dificultate']),  # Convertiți dificultatea în șir
                ingrediente=', '.join(reteta['ingrediente']),  # Convertiți set-ul de ingrediente în șir
            )
            return redirect('home')
    else:
        form = ImportaRetetaForm()

    return render(request, 'importa_reteta.html', {'form': form})

def extrage_reteta(link_reteta):
    response = requests.get(link_reteta)
    soup = BeautifulSoup(response.text, 'html.parser')

    nume_reteta = soup.find('h1', class_='oRecipeHeader-title').text.strip()
    timp = soup.find('div', class_='mTimer-time').text.strip()
    container_dificultate = soup.find('div', class_='oRecipeHeader-meta')
    dificultate_int = len(container_dificultate.find_all('span', class_='icon_chefsCapFilled'))
    ingrediente = {ing.text.strip() for ing in soup.find_all('span', class_='oIngredientBox-ingName')}

    dificultate_map = {
        1: 'Usor',
        2: 'Mediu',
        3: 'Greu',
    }
    dificultate = dificultate_map.get(dificultate_int, 'Necunoscut')

    reteta = {
        'nume_reteta': nume_reteta,
        'timp': timp,
        'dificultate': dificultate,
        'ingrediente': ingrediente,
    }

    return reteta