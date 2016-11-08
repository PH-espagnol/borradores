# contenido-juicio.py

import urllib2, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib2.urlopen(url)
HTML = respuesta.read()

print(obo.quitarEtiquetas(HTML))