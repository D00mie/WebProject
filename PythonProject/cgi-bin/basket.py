import cgi
import json
import sqlite3

params = cgi.FieldStorage()
goods = params.getfirst('goods', '')

goods = json.loads(goods)

connection = sqlite3.connect('cgi-bin/data.db')
cursor = connection.cursor()

expression = str(-int(goods[0]))

for i in range(1, len(goods)):
    expression += ',' + str(-int(goods[i]))

cursor.execute('select * from goods where id in({});'.format(expression))
x = cursor.fetchall()

connection.close()

html = '<table border = "1px" width = "300px">'

for i in x:
    html += '<tr>'

    for j in i:
        html += '<td>' + str(j) + '</td>'

    html += '</tr>'

html += '</table>'

print('''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Basket</title>
    <script>
        
        function pay() {
        
        alert("Success");
        }
        
    </script>
</head>
<body>
<h1>Basket</h1>
<h2> Produsele selectate: </h2>

''' + html +'''
<br>
<button onclick="pay()">Pay</button>
</body>
</body>
</html>
''')