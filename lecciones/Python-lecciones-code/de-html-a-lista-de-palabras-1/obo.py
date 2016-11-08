# obo.py

def quitarEtiquetas(contenidoPagina):
    lugarInicio = contenidoPagina.find("<p>")
    lugarFin = contenidoPagina.rfind("<br/>")

    contenidoPagina = contenidoPagina[lugarInicio:lugarFin]
    return contenidoPagina