import db_utils
import cgi

params = cgi.FieldStorage()
_id = params.getfirst('id', '0')
name = params.getfirst('name', '')
price = params.getfirst('price', '0')
comment = params.getfirst('comment', '')

db_utils.exec_sql('UPDATE goods SET name = "{}", price={}, comment="{}"WHERE id={}'.format(name, price, comment, _id))
