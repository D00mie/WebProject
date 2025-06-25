from http.server import HTTPServer, CGIHTTPRequestHandler

address = ('',  80)

httpd = HTTPServer(address, CGIHTTPRequestHandler)

print('start')
httpd.serve_forever()
print('stop')
# localhost
# index.html
#<table>
#<tr>
#<td></td>
#</tr>
#</table>