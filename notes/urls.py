from django.urls import path, re_path
from . import views

urlpatterns = [
    # qnd a rota '' for acessada, ele deve utilizar a função views.index
    path('', views.index, name='index'), 
    path('add-new-card', views.add_card, name='add_card'),
    re_path(r'^edit-card', views.edit_page, name='edit_page'),
    re_path(r'^edition-completed', views.edition_completed, name='edit_note_completed'),
    re_path(r'^delete-card', views.remove_note, name='delete_card'),
    re_path(r'^filter-by-tag', views.index, name='filtered-index'),
    re_path(r'^clear-filter', views.clear_filters, name='clear_filters'),
    
    #<> Rotas para API:
    path('api/notes/<int:note_id>/', views.api_note), # URL que retorna uma note específica
    path('api/notes/', views.api_note),     # URL que retorna uma lista de notes
    ]