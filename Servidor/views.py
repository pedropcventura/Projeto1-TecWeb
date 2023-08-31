from utils import load_data, load_template, anota_json, build_response
import urllib
from database import Database, Note

db = Database('banco')

def editNote(noteID):
    noteID = int(noteID)
    for n in db.get_all():
        if n.id == noteID:
            note_object = n
    body = load_template('edit/edit.html').format(id=note_object.id, title=note_object.title, content=note_object.content)
    return build_response(body=body)

def update(noteID, request):
    noteID = int(noteID)

    request = request.replace('\r', '')
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {}
    for chave_valor in corpo.split('&'):
        chave_valor = urllib.parse.unquote_plus(chave_valor)
        if "titulo" in chave_valor:
            params["titulo"] = chave_valor[7:]
        if "detalhes" in chave_valor:
            params["detalhes"] = chave_valor[9:]
    note_object = Note(title = params["titulo"], content = params["detalhes"], id=noteID)
    db.update(note_object)
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=note_object.title, details=note_object.content,id=note_object.id, id2=note_object.id) 
        for note_object in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)
    return build_response(code=303, reason='See Other', headers='Location: /')

    
def deleteNote(noteID):
    db.delete(noteID)
    return build_response(code=204)

def error404():
    body = load_template('404/erro.html')
    return build_response(body=body,code=404)

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave_valor = urllib.parse.unquote_plus(chave_valor)
            if "titulo" in chave_valor:
                params["titulo"] = chave_valor[7:]
            if "detalhes" in chave_valor:
                params["detalhes"] = chave_valor[9:]
        #anota_json(params)
        note_object = Note(title = params["titulo"], content = params["detalhes"])
        db.add(note_object)
        return build_response(code=303, reason='See Other', headers='Location: /')


    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=note_object.title, details=note_object.content,id=note_object.id, id2=note_object.id) 
        for note_object in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)
    return build_response(body=body)
