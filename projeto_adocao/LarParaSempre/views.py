from django.shortcuts import render, redirect, get_object_or_404
from .models import Abrigo
from .forms import *

# Create your views here.

def viewHome(request):
    abrigos = Abrigo.objects.all()
    query = request.GET.get("busca")
    if query:
        abrigos = Abrigo.objects.filter(nome__icontains=query)
    else:
        abrigos = Abrigo.objects.all()
    context = {'abrigos':abrigos}
    return render(request, 'home.html', context)


def viewAbrigoDetails(request, id):
    abrigo = get_object_or_404(Abrigo, pk=id)
    context = {'abrigo':abrigo}
    return render(request, 'abrigo/detailsAbrigo.html', context)


def viewAddAbrigo(request):
    if request.method == 'POST':
        form = abrigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = abrigoForm()
        
    context = {'form':form}
    return render(request, 'abrigo/addAbrigo.html', context)

def viewDeleteAbrigo(request, id):
    abrigo = get_object_or_404(Abrigo, pk=id)
    if request.method == 'POST':
        abrigo.delete()
        return redirect('home')
    context = {'abrigo': abrigo}
    return render(request, 'abrigo/deleteAbrigo.html', context)     

def viewUpdateAbrigo(request, id):
    abrigo = get_object_or_404(Abrigo, pk=id)
    if request.method == 'POST':
        form = abrigoForm(request.POST, instance=abrigo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = abrigoForm(instance=abrigo)
    return render(request, 'abrigo/updateAbrigo.html', {'form': form})            

def viewAddPet(request):
    if request.method == 'POST':
        form = petForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listPets')
    else:
        form = petForm()
        
    context = {'form':form}
    return render(request, 'pet/addPet.html', context)

def viewListPets(request):
    pets = Pet.objects.all()
    query = request.GET.get("busca")
    if query:
        pets = Pet.objects.filter(nome__icontains=query)
    else:
        pets = Pet.objects.all()
    context = {'pets':pets}
    return render(request, 'pet/listPets.html', context)

def viewPetDetails(request, id):
    pet = get_object_or_404(Pet, pk=id)
    context = {'pet':pet}
    return render(request, 'pet/detailsPet.html', context)

def viewDeletePet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    if request.method == 'POST':
        pet.delete()
        return redirect('listPets')
    context = {'pet': pet}
    return render(request, 'pet/deletePet.html', context)  

def viewUpdatePet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    if request.method == 'POST':
        form = petForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('listPets')
    else:
        form = petForm(instance=pet)
    return render(request, 'pet/updatePet.html', {'form': form}) 