from django.shortcuts import render, redirect
from .models import *

def index(request):
    if request.method == 'POST':
        title   = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_name = request.POST.get('tag')

        tag, created = Tag.objects.get_or_create(name__iexact = tag_name)
        # devolve created = True, se o objeto for criado.

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