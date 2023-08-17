import  json
def extract_route(string):
    list = string.split(' ')
    r = list[1]
    r = r[1:]
    return r
    
def read_file(path):
    with open(path, mode='r+b') as file:
        return file.read()
    
def load_data(arq):
    path = 'data/'+arq
    dict = {}
    with open(path, mode='r') as file:
        dict = json.load(file)
    return dict

def load_template(arq):
    path = "templates/"+arq
    with open(path, 'r') as file:
        return file.read() #transforma arquivo em string

def anota_json(params): 
    with open("data/notes.json", 'r+') as file:
        file_data = json.load(file)
        file_data.append(params)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def build_response(body='', code=200, reason='OK', headers=''):
    status_line = f'HTTP/1.1 {code} {reason}\n'
    response = f'{status_line}{headers}\n{body}'
    return response.encode()




    

