# html-a-lista-1.py
import urllib2, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

respuesta = urllib2.urlopen(url)
html = respuesta.read()
texto = obo.quitarEtiquetas(html)
listaPalabras = texto.split()

print(listaPalabras[0:120])