# guardar-paginaweb.py

import urllib2

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib2.urlopen(url)
contenidoWeb = respuesta.read()

f = open('obo-t17800628-33.html', 'w')
f.write(contenidoWeb)
f.close