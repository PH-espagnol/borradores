# obo.py
def quitarEtiquetas(contenidoPagina):
    lugarInicio = contenidoPagina.find("<p>")
    lugarFin = contenidoPagina.rfind("<br/>")

    contenidoPagina = contenidoPagina[lugarInicio:lugarFin]

    adentro = 0
    texto = ''

    for caract in contenidoPagina:
        if caract == '<':
            adentro = 1
        elif (adentro == 1 and caract == '>'):
            adentro = 0
        elif adentro == 1:
            continue
        else:
            texto += caract

    return texto