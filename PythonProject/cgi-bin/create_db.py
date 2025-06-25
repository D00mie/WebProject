# Importam biblioteka cu ajutorul carea putem sa lucram cu Baze
# de date
import sqlite3

# Sa stabilim conexiunea cu fisierul baza de date data.db
# Daca fisierul nu exista va fi creat automat
connection = sqlite3.connect('data.db')

# Creem un obiect special numit 'cursor' si cu ajutorul acestui
# obiect noi putem modifica datele din BD cu ajutorul sql-request
cursor = connection.cursor()

# Creem un SQL care va crea un tabel in BD
# Creem un tabel goods
# id - uniq
# name - denumirea produsului
# price - pretul
# commentariu
sql = '''
CREATE TABLE IF NOT EXISTS goods(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price INTEGER,
comment TEXT
)
'''

# Executam SQL-request care creaza tabel
cursor.execute(sql)


# Adaugam in tabel 3 row pentru asta executam 3 SQL-requesturi
#cursor.execute('INSERT INTO goods(name, price) VALUES("Avion", 1000)')
#cursor.execute('INSERT INTO goods(name, price) VALUES("Ski", 2000)')
#cursor.execute('INSERT INTO goods(name, price) VALUES("Paine", 5)')

connection.commit()

cursor.execute('SELECT * FROM goods')
goods = cursor.fetchall()
print(goods)

connection.close()


