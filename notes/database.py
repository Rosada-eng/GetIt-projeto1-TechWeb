""" 
    Configura os métodos necessários para manipular o banco de dados
"""

from models import *
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
def edit_note(note_id, fields_to_be_edited:dict):
    n_modified = Note.objects.filter(id=note_id).update(**fields_to_be_edited)

    return n_modified
    
#! DELETE_NOTE
def delete_note(note_id):
    n_deleted = Note.objects.delete(id=note_id)
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