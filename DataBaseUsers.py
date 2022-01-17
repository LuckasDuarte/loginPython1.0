import sqlite3
from sqlite3.dbapi2 import Cursor


conn = sqlite3.connect('DatabaseUsers.db')
cursor= conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Usuário TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")

print('Conectado ao banco de dados !!!')



