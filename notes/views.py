from django.shortcuts import render, redirect
from .models import *

def index(request):
    if request.method == 'POST':
        title   = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_name = request.POST.get('tag')

        """ 
            Se o usuário informou um nome para tag, checa se já existe (insensível match)
            Se não existe, cria uma nova e adiciona relação na Note
            Se não informou nome para tag, cria uma Note sem relação.
        """
        if tag_name:
            tag, created = Tag.objects.get_or_create(name__iexact = tag_name, defaults={"name": tag_name}) # devolve created = True, se o objeto for criado.
            print(f"tag criada -- {tag.id}, {tag.name}")
        else:
            tag = None

        new_note = Note.objects.create(title=title, content=content, tag= tag)        
        return redirect('index')
        
    else:
        all_notes = Note.objects.all()
        return render (request, "notes/index.html", {'notes': all_notes})