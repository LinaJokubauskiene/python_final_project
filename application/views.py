from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Note
from .forms import CategoryCreateForm, NoteCreateForm
from django.db.models import Q
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return HttpResponse("Note app!")

def views():
    return None


def index(request):
    return render(request, 'index.html')

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


def show_notes(request):
    notes = Note.objects.all()
    return render(request, 'show_notes.html', context={'notes': notes})

def show_categories(request):
    categories = Category.objects.values()
    return render(request, 'show_categories.html', context={'categories': categories})


@login_required(login_url='login')

def delete_category(request, category_name):
    category = Category.objects.get(name=category_name)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'confirm_delete_category.html', context={'delete_category': category})


def search(request):
    query = request.GET.get('query')
    search_results = Note.objects.filter(Q(name=query))
    return render(request, 'search.html', {'notes': search_results, 'query': query})
    # return redirect('show_notes.html')

# def get_queryset(self):
#     categories= Category.object.filter(note__category='Category')
#     return categories


class CategoryBaseView(View):
    model = Category
    fields = ['note']
    success_url = reverse_lazy('category_lists')


class CategoryCreateView(CategoryBaseView, CreateView):
    pass


class CategoryListView(CategoryBaseView, ListView):
    pass


class CategoryUpdateView(CategoryBaseView, UpdateView):
    pass


class CategoryDeleteView(CategoryBaseView, DeleteView):
    pass
