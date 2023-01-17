from django import forms
from django.forms import ModelForm
from .models import Category, Note


class CategoryCreateForm(ModelForm):
    def __init__(self, *args, category=None, **kwargs):
        super().__init__(*args, **kwargs)
        if category:
            self.fields['category'].queryset = Category.objects.filter(category__name=category)

    class Meta:
        model = Category
        fields = '__all__'


class NoteCreateForm(ModelForm):
    def __init__(self, *args, note=None, **kwargs):
        super().__init__(*args, **kwargs)
        if note:
            self.fields['note'].queryset = Note.objects.filter(note__name=note)

    class Meta:
        model = Note
        fields = '__all__'


class CategoryUpdateForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class NoteUpdateForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class CategoryDeleteForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class NoteDeleteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
