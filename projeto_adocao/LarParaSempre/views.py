from django.shortcuts import render, redirect, get_object_or_404
from .models import Abrigo
from .forms import abrigoForm

# Create your views here.

def viewHome(request):
    abrigos = Abrigo.objects.all()
    context = {'abrigos':abrigos}
    return render(request, 'home.html', context)


def viewAbrigoDetails(request, id):
    abrigo = get_object_or_404(Abrigo, pk=id)
    context = {'abrigo':abrigo}
    return render(request, 'details.html', context)


def viewAddAbrigo(request):
    if request.method == 'POST':
        form = abrigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = abrigoForm()
        
    context = {'form':form}
    return render(request, 'addAbrigo.html', context)

def viewDeleteAbrigo(request, id):
    abrigo = get_object_or_404(Abrigo, pk=id)
    if request.method == 'POST':
        abrigo.delete()
        return redirect('home')
    context = {'abrigo': abrigo}
    return render(request, 'deleteAbrigo.html', context)     

def viewUpdateAbrigo(request, id):
    abrigo = get_object_or_404(Abrigo, pk=id)
    if request.method == 'POST':
        form = abrigoForm(request.POST, instance=abrigo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = abrigoForm(instance=abrigo)
    return render(request, 'updateAbrigo.html', {'form': form})            
