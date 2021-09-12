""" 
    Configura os métodos necessários para manipular o banco de dados no SQLite
"""

import sqlite3
from dataclasses import dataclass
from utils import CUR_DIR
import os

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, DB_name):
        self.name = DB_name
        self.path = os.path.join(CUR_DIR, 'data', f'{self.name}.db')
        # Conecta a um banco de dados já existente
        self.conn = sqlite3.connect(self.path)
        print(f"Conectando ao banco em {self.path}")

    def add_note(self, note:Note, table_name='notes', columns_name='title, content, id'):
        """ Insere uma nova note na tabela notes.
            Retorna True, se sucesso. False, caso contrário.
        """
        try: 
            self.conn.execute(f"""
                INSERT INTO {table_name} (title, content) 
                VALUES ('{note.title}', '{note.content}')

            """)
            self.conn.commit()

            print("Nota adicionada com sucesso")
            return True
        
        except:
            print("Falha ao adicionar nota")
            return False


    def get_one_note(self, id_note, table_name='notes', columns_name='title, content, id'):
        """ Retorna uma única nota com o id especificado
            Por padrão, procura no banco de dados fornecido, na table 'notes'
        """
        try: 
            #<> Cursor retorna um iterável objeto de sqlite3
            cursor = self.conn.execute(f"""
                SELECT {columns_name} FROM {table_name}
                WHERE id = {id_note}
            """)

            for notes in cursor:
                note = Note(title=notes[0], content=notes[1], id=notes[2])
            return note

        except:
            print("Não foi possível selecionar a Note especificada. Confira os valores informados")
            return None

        
    def get_all_notes(self, table_name='notes', columns_name='title, content, id'):
        """ Retorna todas as notas do banco.
            Por padrão, procura no banco de dados fornecido, na table 'notes'
        
        """
        try:   
            cursor = self.conn.execute(f"""
                SELECT {columns_name} FROM {table_name}
            """)
            
            notes = [
                Note(title=note[0], content=note[1], id=note[2]) 
                for note in cursor 
            ]

            return notes

        except:
            print("Não foi possível retornar as Notas do banco de dados.")
            return None

    def edit_note(self, note:Note, table_name='notes'):
        """ Edita uma nota já existente.
            Recebe uma nova nota já formatada na maneira desejada 
            Retorna True, se sucesso. False, caso contrário.
        """

        try:

            self.conn.execute(f"""
                UPDATE {table_name} SET
                title = '{note.title}', content='{note.content}'
                WHERE id = {note.id}
            
            """)

            self.conn.commit()
            return True

        except:
            print("Não foi possível editar a nota. Cheque as informações fornecidas")
            return False

    def delete_note(self, id_note, table_name='notes'):
        """ Exclui uma nota no banco de dados, apenas com o id fornecido"""
        try:
            self.conn.execute(f"""
                DELETE FROM {table_name}
                WHERE id = {id_note}
            """)

            self.conn.commit()
            return True

        except:
            print("Não foi possível deletar a Nota informado")
            return False