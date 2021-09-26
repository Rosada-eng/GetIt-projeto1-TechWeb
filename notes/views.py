from django.shortcuts import render, redirect
from .models import *
from .database import *
import re


def check_for_changes(new_title, new_tag, new_content, note_id):
    old_note = get_one_note(note_id)

    if new_title == '':
        title = old_note.title
    else:
        title = new_title

    if new_tag == '':
        tag = old_note.tag.name
    else:
        tag = new_tag

    content = re.sub("(\\r\\n(\s*))*$", '', new_content)
     

    return title, tag, content

def index(request):
    all_notes = get_all_notes()
    return render (request, "notes/index.html", {'notes': all_notes})

def add_card(request):
    """ 
        método chamado pela URL add-new-card
    """

    title   = request.POST.get('title')
    content = request.POST.get('content')
    tag_name = request.POST.get('tag')
    try: 
        """ 
            Se o usuário informou um nome para tag, checa se já existe (insensível match)
            Se não existe, cria uma nova e adiciona relação na Note
            Se não informou nome para tag, cria uma Note sem relação.
        """
        if tag_name:
            tag, created = Tag.objects.get_or_create(name__iexact = tag_name, defaults={"name": tag_name}) # devolve created = True, se o objeto for criado.
            if created:
                print(f"Nova tag criada: {tag.id} - {tag.name}")
        else:
            tag = None

        new_note = add_note(title=title, content=content, tag= tag)        
        
        return redirect('index')

    except:
        print("Não foi possível adicionar uma nova Note")
        return redirect('index')

def edit_page(request):
    note_id = int(request.POST.get('note_id'))
    note = get_one_note(note_id)

    return render(request, "notes/edit_page.html", {'note': note} )

def edition_completed(request):
    """ 
        Checa se o usuário realizou mudanças em title ou tag (campos não vazios).
        Caso não tenha realizado, mantém os title e tag antigos. 
        Caso tenha, atualiza com os novos valores.
    """
    print(request.POST)
    note_id = int(request.POST.get('note_id'))

    new_title   = request.POST.get('title')
    new_tag     = request.POST.get('tag')
    new_content     = request.POST.get('content')

    title, tag, content  = check_for_changes(new_title, new_tag, new_content, note_id)

    edited_note = {
        'title':    title,
        'content':  content,
        'tag_name': tag
        }

    edit_note(note_id = note_id, fields_to_be_edited=edited_note)
    return redirect('index')

def remove_note(request):
    print(request.POST)
    note_id = int(request.POST.get('note_id'))
    print(f"id: {note_id}")
    delete_note(note_id)
    return redirect('index')

