from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title   = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        #<> Existem duas formas de se criar uma nova linha na tabela:
        #<> 1- objects.create(title="...", content="...") --> já usa save (commit)
        #<> 2- Criar um objeto e usar o método .save

        #% método .create()
        new_note = Note.objects.create(title=title, content=content)
        
        #% Outra forma -- método .save()
        # new_note = Note(title=title, content=content)
        # new_note.save()

        """ Obs.: .save() também pode ser utilizado para fazer o UPDATE de alguma linha já existente.
        Queries: https://docs.djangoproject.com/en/3.1/topics/db/queries/
        Queries: https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.create"""
        
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render (request, "notes/index.html", {'notes': all_notes})