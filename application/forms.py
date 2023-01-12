from django import forms
from django.forms import ModelForm
from .models import Category


class CategoryCreateForm(ModelForm):
    def __init__(self, *args, category=None, **kwargs):
        super().__init__(*args, **kwargs)
        if category:
            self.fields['category'].queryset = Category.objects.filter(category_name=category)
    class Meta:
        model = Category
        fields ='__all__'

