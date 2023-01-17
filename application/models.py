from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Name', max_length=50, unique=True, null=False, blank=True)

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='note', null=True, blank=True)
    search_fields = ('note_name')
    list_filter = ('category')

class Meta:
    ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.category})'




