import cgi
import db_utils

params = cgi.FieldStorage()
print(params)
name = params.getfirst('name')
price = params.getfirst('price')
comment = params.getfirst('comment', "")

sql = 'INSERT INTO goods(name, price, comment) VALUES("{}", {}, "{}")'.format(name, price, comment)
db_utils.exec_sql(sql)
# db_utils.exec_sql('INSERT INTO goods(name, price, comment) VALUES("{}", {}, "{}")'.format(name, price, comment))