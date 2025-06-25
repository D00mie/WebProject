import cgi
import db_utils

params = cgi.FieldStorage()
_id = params.getfirst('id')

db_utils.exec_sql('DELETE FROM goods WHERE id={}'.format(_id))
