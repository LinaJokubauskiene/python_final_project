from django.urls import path, include
from .views import index, add_note, add_category, delete_note, delete_category, show_categories, show_notes, show_note
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_note/', add_note, name='add_note'),
    path('show_notes/', show_notes, name='show_notes'),
    path('show_note/<int:note_id>/', show_note, name='show_note'),
    path('add_category/', add_category, name='add_category'),
    path('show_categories/', show_categories, name='show_categories'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('search/', views.search, name='search'),
    # path(('search/<int:note_id>', views.note, name='note')
    # path('update_note/<int:note_name>/', update_note, name='update_note'),
]

