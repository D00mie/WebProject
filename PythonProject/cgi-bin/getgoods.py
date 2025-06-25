import sqlite3
import db_utils

connection = sqlite3.connect('cgi-bin/data.db')
cursor = connection.cursor()

print('Content-type: text/html\n')

db_utils.select_goods(cursor)
connection.close()