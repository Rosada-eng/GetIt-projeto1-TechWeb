import socket 
from utils import *
from views import *
import re
from database import Database, Note

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print('-----------------------', request, '\n\n')

    route = extract_route(request)

    #@ GET:
    if request.startswith('GET'):
        # Extrai a rota de cada arquivo a ser lido
        filepath = CUR_DIR / route
        print(f"route: {route} --> {filepath}")

        if filepath.is_file(): 
            # Lê o arquivo solicitado e devolve em texto
            response = build_response() + read_file(route)

        elif route == '':
            # Builda a página HTML automaticamente construída
            response = build_response() + load_index()

        else:
            # último caso: response = bytes vazio
            response = build_response(code=400, reason="Bad Request") + bytes()


    #@ POST -- adicionar, editar ou excluir note
    elif request.startswith('POST'):
        db = Database('getit')
        card_id = re.sub(r"\D", "", route)

        if route.startswith("edit-card"):
            note = db.get_one_note(card_id)
            note_params = {
                'title': note.title,
                'content': note.content,
                'id': note.id
            }

            response = build_response() + load_edit_page(note_params)
        
        elif route.startswith("edition-completed"):
            # extrai titulo e conteúdo do corpo do request
            params = extract_body_from_request(request)
            if not params['title']:
                note = db.get_one_note(card_id)
                params['title'] = note.title

            edited_note = Note(id=card_id, title=params['title'], content=params['content'])
            result = db.edit_note(edited_note)
            if result == True:
                response = build_response(code=303, reason="See other", headers="\nLocation: /") + load_index()

            else:
                response = build_response(code=400, reason="Bad Request") + bytes()

        elif route.startswith("delete"):
            result = db.delete_note(card_id)
            if result == True:
                response = build_response() + load_index()
            else:
                response = build_response(code=400, reason="Bad Request") + bytes()

        elif route.startswith("add"):
            params = extract_body_from_request(request)
            new_note = Note(title=params['title'], content=params['content'])
            result = db.add_note(new_note)

            if result == True:
                response = build_response() + load_index()
            else:
                response = build_response(code=400, reason="Bad Request") + bytes() 
    else:
        response = build_response(code=400, reason="Bad Request") + bytes()

    client_connection.sendall(response)
    client_connection.close()

server_socket.close()