# Teste Database:
from database import *

def checa_teste(numero_teste, resposta, gabarito):
    if resposta == gabarito:
        print(f"Test {numero_teste} " + "\033[1;32m PASSED!" + "\033[0;0m" + '\n -------------- \n')
    else: 
        print(f"Test {numero_teste} " + "\033[1;31m FAILED!" + "\033[0;0m" + '\n -------------- \n')

#! Conectar com o BD
db = Database('getit')

#! GET ONE
note1 = db.get_one_note(id_note = 2)
print("Teste GET ONE --> note2: PÃO DOCE")

checa_teste(1, note1.title, "Pão doce")

#! GET ALL
print("Teste GET ALL")
all_notes = db.get_all_notes()
print(f"Numero de notas: {len(all_notes)}")

checa_teste(2, len(all_notes), 10)

#! POST 
print("Teste POST")
new_note = Note(title='New note', content='teste')
result = db.add_note(new_note)

checa_teste(3, result, True)
#! EDIT 

print("Teste EDIT NOTE")
edited_note = Note(id=11, title='Edited note', content='edited test')
result = db.edit_note(edited_note)

checa_teste(4, result, True)

#! DELETE 
print("Teste DELETE NOTE")
result = db.delete_note(id_note=11)

checa_teste(5, result, True)
