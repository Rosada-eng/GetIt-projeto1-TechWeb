from utils import load_template
from database import Database, Note

def load_all_notes():
    #! PREENCHIMENTO DO HTML COM AS NOTAS A PARTIR DO BANCO DE DADOS
    note_template = load_template(r"docs\templates\components\note.html")

    # Carrega todas as notes a partir do banco de dados
    db = Database('getit')
    all_notes = db.get_all_notes()

    lista_notes = [
        note_template.format(title=note.title, details=note.content, id=note.id) for note in all_notes
    ]

    # Transforma o array em uma única string
    notes = '\n'.join(lista_notes)

    return notes

def load_one_note(note_id):
    db = Database('getit')
    note = db.get_one_note(note_id)

    return note

def load_index():
    notes = load_all_notes()

    # Retorna a página HTML automaticamente preenchida encodificada.
    return load_template(r'docs\index.html').format(notes=notes).encode()

def load_edit_page(params):
    # Retorna a página HTML automaticamente preenchida encodificada.
    return load_template(r'docs\edit_page.html').format(id=params['id'], title=params['title'], content=params['content']).encode()