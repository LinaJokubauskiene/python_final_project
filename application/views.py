from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Note
from .forms import CategoryCreateForm, NoteCreateForm, NoteUpdateForm, NoteDeleteForm, CategoryUpdateForm, CategoryDeleteForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    return HttpResponse("Note app!")

def views():
    return None


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')

def add_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'Record created!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_category.html', context={'form': form})
    else:
        form = CategoryCreateForm()
    return render(request, 'add_category.html', context={'form': form})


@login_required(login_url='login')

def add_note(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            messages.success(request, 'Record created!')
            return redirect('index')
        messages.warning(request, 'Form not valid!')
        return render(request, 'add_note.html', context={'form': form})
    else:
        form = NoteCreateForm()
    return render(request, 'add_note.html', context={'form': form})


@login_required(login_url='login')
def show_notes(request):
    notes = Note.objects.all()
    return render(request, 'show_notes.html', context={'notes': notes})

def search(request):
    query = request.GET.get('query')
    search_results = Note.objects.filter(Q(name=query))
    return render(request, 'search.html', {'notes': search_results, 'query': query})

def filter_notes_by_category(request, category_id):
    note_list = Note.objects.filter(category=category_id)
    return render(request, 'show_notes.html', {'notes': note_list})

def show_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'show_note.html', context={'note': note})


@login_required(login_url='login')
def show_categories(request):
    categories = Category.objects.values()
    return render(request, 'show_categories.html', context={'categories': categories})

@login_required(login_url='login')
def update_category(request, category_id):
    if request.method == 'POST':
        category_model= CategoryUpdateForm.objects.get(category_id)
        form = CategoryUpdateForm(request.POST, instance=category_model)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated!')
            return redirect('update_category')
        messages.warning(request, 'Form not valid!')
        return render(request, 'update_category.html', context={'form': form})
    else:
        form = NoteUpdateForm()
    return render(request, 'show_categories.html', context={'form': form})


@login_required(login_url='login')
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('show_categories')
    return render(request, 'delete_category.html', context={'category': category})


@login_required(login_url='login')
def update_note(request, note_id):
    if request.method == 'POST':
        note_model= NoteUpdateForm.objects.get(note_id)
        form = NoteUpdateForm(request.POST, instance=note_model)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated!')
            return redirect('update_note')
        messages.warning(request, 'Form not valid!')
        return render(request, 'update_note.html', context={'form': form})
    else:
        form = NoteUpdateForm()
    return render(request, 'show_notes.html', context={'form': form})


@login_required(login_url='login')
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('show_notes')
    return render(request, 'delete_note.html', context={'note': note})


