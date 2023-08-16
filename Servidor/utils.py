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
