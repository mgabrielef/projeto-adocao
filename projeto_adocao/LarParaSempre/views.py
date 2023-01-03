from django.shortcuts import render, redirect
from .models import Abrigo
from .forms import abrigoForm

# Create your views here.

def viewHome(request):
    return render(request, 'home.html')

def viewAddAbrigo(request):
    if request.method == 'POST':
        form = abrigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarAbrigos')
    else:
        form = abrigoForm()
        
    context = {'form':form}

    return render(request, 'addAbrigo.html', context)

def viewGetAbrigo(request):
    abrigos = Abrigo.objects.all()
    context = {'abrigos':abrigos}
    return render(request, 'listarAbrigos.html', context)

def viewAbrigoDetails(request, pk):
    abrigo = Abrigo.objects.get(pk=pk)
    context = {'abrigo':abrigo}
    return render(request, 'details.html', context)