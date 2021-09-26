""" 
    Configura os métodos necessários para manipular o banco de dados
"""

from .models import *
from django.shortcuts import render, redirect

#! CREATE_NOTE
def add_note(title, content, tag=None):
    Note.objects.create(title= title, content=content, tag=tag)
    return 

#! GET_ONE_NOTE
def get_one_note(note_id):
    note = Note.objects.get(id = note_id)
    return note

#! GET_ALL_NOTES
def get_all_notes():
    notes = Note.objects.all()
    return notes

#! UPDATE_NOTE
def edit_note(note_id, fields_to_be_edited):
    # checa se existe a tag. Se não existir, 
    # cria uma nova com com o nome informado na edição
    
    #@ checar tag_name se é None
    tag, created = Tag.objects.get_or_create(
        name__iexact=fields_to_be_edited['tag_name'], 
        defaults={'name': fields_to_be_edited['tag_name']}
        )
    edited_note = {
        'title':    fields_to_be_edited['title'],
        'content':  fields_to_be_edited['content'],
        'tag':      tag
    }
    
    n_modified = Note.objects.filter(id=note_id).update(**edited_note)

    return n_modified
    
#! DELETE_NOTE
def delete_note(note_id):
    n_deleted = Note.objects.get(id=note_id).delete()
    return n_deleted

#! CREATE_TAG
def add_tag():
    return

#! GET_ONE_TAG
def get_one_tag():
    return

#! GET_ALL_TAGS 
def get_all_tags():
    return

#! UPDATE_TAG
def edit_tag():
    return

#! DELETE_TAG
def delete_tag():
    return