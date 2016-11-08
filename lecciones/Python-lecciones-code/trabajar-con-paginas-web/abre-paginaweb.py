# abre-paginaweb.py

import urllib2

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib2.urlopen(url)
contenidoWeb = respuesta.read()

print(contenidoWeb[0:300])