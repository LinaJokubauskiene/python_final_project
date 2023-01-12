from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Note
from .forms import CategoryCreateForm


# Create your views here.


def index(request):
    return HttpResponse("Note app!")

def views():
    return None


def index(request):
    return render(request, 'index.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES, category='Category1')
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'add_category.html', context={'form': form})
    form = CategoryCreateForm(category='Category1')
    return render(request, 'add_category.html', context={'form': form})


def show_categories(request):
    categories = Category.objects.values()
    return render(request, 'show_categories.html', context={'categories': categories})


def show_notes(request):
    notes = Note.objects.values()
    return render(request, 'show_notes.html', context={'notes': notes})

def delete_category(request, category_name):
    category = Category.objects.get(name=category_name)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'confirm_delete_category.html', context={'category': category})
