import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ""

# note é o nome da tabela e nomeDB o nome da base de dados
class Database:
    def __init__(self, nomeBD):
        self.nome = nomeBD
        self.conn = sqlite3.connect(nomeBD+".db")
        self.conn.execute("""CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, 
                                                              title TEXT, 
                                                              content TEXT NOT NULL);""")

    def add(self, note_object: Note):
        #self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note_object.title}', '{note_object.content}');")
        self.conn.execute(f"INSERT INTO note (title, content) VALUES (?, ?);", (note_object.title, note_object.content))
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute(f"SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            note_object = Note(id = linha[0], title = linha[1], content = linha[2])
            lista.append(note_object)
        return lista
    
    def update(self, entry):
        # Precisa dar commit por update ou pode dar dois updates e um commit?
        self.conn.execute(f"UPDATE note SET title = '{entry.title}' WHERE id = {entry.id}")
        self.conn.commit()
        self.conn.execute(f"UPDATE note SET content = '{entry.content}' WHERE id = {entry.id}")
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")

