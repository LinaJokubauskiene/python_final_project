from django import forms
from django.forms import ModelForm
from .models import Category, Note

class NoteCreateForm(ModelForm):
    def __init__(self, *args, note=None, **kwargs):
        super().__init__(*args, **kwargs)
        if note:
            self.fields['note'].queryset = Note.objects.filter(note_name=note)

    class Meta:
        model = Note
        fields ='__all__'


class CategoryCreateForm(ModelForm):
    def __init__(self, *args, category=None, **kwargs):
        super().__init__(*args, **kwargs)
        if category:
            self.fields['category'].queryset = Category.objects.filter(category_name=category)
    class Meta:
        model = Category
        fields ='__all__'

