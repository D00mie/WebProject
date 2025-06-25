import sqlite3
import json
import cgi

params = cgi.FieldStorage()

fun_name = params.getfirst('fun_name', '')
result_id = params.getfirst('result_id', -1)
algorithm = params.getfirst('algorithm', 'sql')

print('Content-type: text/html\n')
connection = sqlite3.connect('cgi-bin/data.db')
cursor = connection.cursor()

if algorithm == 'sql':
    cursor.execute('select ' + fun_name + '(price) from goods;')
elif algorithm == 'py':
    cursor.execute('select price from goods;')

x = cursor.fetchall()

result = x[0][0]
if algorithm == 'py':
    if fun_name == 'max':
        for i in x:
            if i[0] > result:
                result = i[0]
    elif fun_name == 'min':
        for i in x:
            if i[0] < result:
                result = i[0]
    elif fun_name == 'avg':
        result = 0
        for i in x:
            result += i[0]
        result = result / len(x)
    else:
        result = 0

connection.close()
y = json.dumps([result, result_id])
print(y)