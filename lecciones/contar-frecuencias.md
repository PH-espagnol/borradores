---
title: Contar frecuencias de palabras con Python
authors:
- William J. Turkel
- Adam Crymble
date: 2012-07-17
reviewers:
- Miriam Posner
- Jim Clifford
translator:
- Víctor Gayol
layout: default
next: crear-y-ver-archivos-html-con-python
previous: normalizar-datos
---

## Objetivo de la lección

Tu lista ahora está lo suficientemente limpia para comenzar a analizar su contenido de una manera útil. Contar la frecuencia de palabras específicas en la lista puede proveernos con datos ilustrativos. Python posee una manera fácil de contar frecuencias, pero requiere el uso de un nuevo tipo de variable: el *diccionario*. Antes de comenzar a trabajar en un diccionario, considera los procesos utilizados para calcular las frecuencias en una lista.

### Archivos necesarios para esta lección

-   `obo.py`

Si no tienes este archivo puedes descargar un archivo [zip][] que contiene el código de las lecciones previas de esta serie.

## Frecuencias

Ahora queremos contar la frecuencia de cada palabra en nuestra lista. Ya has visto que es fácil procesar una lista utilizando un bucle `for`. Intenta guardar y ejecutar el ejemplo siguiente. Recuerda que `+=` le indica al programa que añada algo al final de una variable existente.

``` python
# count-list-items-1.py

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))
```

Aquí, comenzamos con una cadena de texto y la dividimos en una lista tal como hicimos antes. Entonces, creamos una lista (inicialmente vacía) llamada *wordfreq*, fuimos por cada una de las palabras en *wordlist* y contamos el número de veces que cada palabra aparece en toda la lista. Añadimos entonces el conteo de palabras a nuestra lista *wordfreq*. Utilizando la operación `zip`, somos capaces de hacer coincidir la primera palabra de nuestra lista de palabras con el primer número en la lista de frecuencias, la segunda palabra con la segunda frecuencia, y así el resto. Terminamos con una lista de palabras y frecuencias pareadas. La función `str` convierte cualquier objeto en una cadena así que puede ser impresa.

Debes obtener algo como esto:

``` python
String
it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness

List
['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age',
'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
'foolishness']

Frequencies
[4, 4, 4, 1, 4, 2, 4, 4, 4, 1, 4, 2, 4, 4, 4, 2, 4, 1, 4,
4, 4, 2, 4, 1]

Pairs
[('it', 4), ('was', 4), ('the', 4), ('best', 1), ('of', 4),
('times', 2), ('it', 4), ('was', 4), ('the', 4),
('worst', 1), ('of', 4), ('times', 2), ('it', 4),
('was', 4), ('the', 4), ('age', 2), ('of', 4),
('wisdom', 1), ('it', 4), ('was', 4), ('the', 4),
('age', 2), ('of', 4), ('foolishness', 1)]
```

Te retribuirá estudiar el código anterior hasta entenderlo antes de seguir adelante.

Python incluye también una herramienta muy conveniente llamada [lista por comprensión][] (*list comprehension*), que puede ser utilizada para hacer lo mismo que hace el bucle `for`, pero de manera más económica.

``` python
# count-list-items-1.py

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist] # a list comprehension

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))
```

Si estudias esta lista por comprensión cuidadosamente descubrirás que hace exactamente lo mismo que el bucle `for` en el ejemplo previo, pero de una manera condensada. Cualquiera de los dos métodos trabajará bien, así que utiliza la versión con la que te sientas más a gusto.

Por regla general es más acertado que utilices un código que entiendas en vez de un código que se ejecute más rapidamente.

En este punto tenemos una lista de pares en la que cada par contiene una palabra y su frecuencia. Esta lista es algo redundante. Si el artículo 'the' se encuentra 500 veces, entonces esta lista contendrá quinientas copias del par ('the', 500). También la lista tiene el orden en el que aparecen las palabras en el texto original en vez de enlistar las palabras de la más a la menos frecuente. Podemos resolver ambos problemas convirtiendo la lista en un diccionario e imprimiendo entonces el diccionario en el orden en el que aparecen de más a menos los elementos.

## Diccionarios de Python

Las cadenas y las listas están ordenadas secuencialmente, lo cual significa que puedes acceder a sus contenidos utilizando un índice, un número que comienza en 0. Si tienes una lista que contiene cadenas, puedes utilizar un par de índices para acceder primero a una cadena particular de la lista y luego a un carácter particular de esa cadena. Estudia los ejemplos siguientes.

``` python
s = 'hello world'
print(s[0])
-> h

print(s[1])
-> e

m = ['hello', 'world']
print(m[0])
-> hello

print(m[1])
-> world

print(m[0][1])
-> e

print(m[1][0])
-> w
```

Para seguirle el rastro a las frecuencias, vamos a utilizar otro tipo de objeto de Python, un diccionario. El diccionario es una colección *no-ordenanda* de objetos. Esto significa que no puedes usar un índice para recobrar elementos de ella. Sin embargo, puedes buscarlos mediante la utilización de una clave (de ahi el nombre de *diccionario*). Estudia el ejemplo siguiente:

``` python
d = {'world': 1, 'hello': 0}
print(d['hello'])
-> 0

print(d['world'])
-> 1

print(d.keys())
-> ['world', 'hello']
```

Los diccionarios pueden resultar algo confusos para un programador novato. Trata de pensarlos como un diccionario de palabras de cualquier lengua. Si no sabes (o recuerdas) exactamente en qué difiere "biyectiva" de "inyectiva" puedes buscar los dos términos en el *Diccionario de la Lengua Española*. El mismo principio se aplica cuando imprimes `print(d['hello']);` excepto que, en vez de imprimir una definición literaria imprime el valor asociado con la palabra clave 'hello' tal como lo definiste cuando creaste el diccionatio llamado *d*. En este caso, el valor es "0".

Toma en cuenta que utilizas paréntesis para definir el diccionario y corchetes para acceder a las cosas dentro de él. La operación `keys` devuelve una lista de claves (*keys*) que se definen en el diccionario.

## Los pares palabra-frecuencia

Sobre la base de lo que tenemos hasta ahora queremos una función que pueda convertir una lista de palabras en un diccionario de pares de palabra-frecuencia. El único comando nuevo que vamos a necesitar en `dict`, que hace un diccionario a partir de una lista de pares. Copia lo siguiente y añádelo en el módulo `obo-py`.

``` python
# Dada una lista de palabras, devuelve un diccionario de
# pares de palabra-frecuencia.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))
```

También querremos una función que pueda ordenar un diccionario de pares de palabra-frecuencia, en orden de frecuencia descendente. Copia esto y añádelo también al módulo `obo.py`.

``` python
# Ordena un diccionario de pares palabra-frecuencia en
# orden de frecuencia descendente.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
```

Ahora podemos escribir un programa que importe un URL y nos devuelva pares de palabra-frecuencia de la página Web puestos en orden descendente de frecuencia. Copia el siguiente programa en el Komodo Edit, guárdalo como `html-to-freq.py` y ejecútalo. Estudia el programa y los datos de salida con atención antes de continuar.

``` python
#html-to-freq.py

import urllib2, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
```

## Retirar palabras vacías

Cuando observamos los datos de salida del programa `html-to-freq.py`, vemos que las palabras más frecuentes en el texto son palabras funcionales como "the", "of", "to" y "and".

``` python
(192, 'the')
(105, 'i')
(74, 'to')
(71, 'was')
(67, 'of')
(62, 'in')
(53, 'a')
(52, 'and')
(50, 'you')
(50, 'he')
(40, 'that')
(39, 'his')
(36, 'it')
```

Por lo general, estas palabras son las más comunes en cualquier texto en idioma inglés, por lo que no nos dicen mucho acerca de lo que es distintivo en el juicio de Bowsey. En general, estamos más interesados en encontrar las palabras que nos ayuden a diferenciar este texto de textos acerca de diferentes temas. Así que vamos a filtrar las palabras funcionales comunes. Las palabras que son ignoradas como éstas se conocen como *palabras vacías*. Vamos a utilizar la siguiente lista adaptada de una que fue publicada en línea por los [informáticos de Glasgow][]. Cópiala y ponla al principio de la biblioteca `obo.py` que estás construyendo.

``` python
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']
```

Ahora, deshacerse de las palabras fucionales de una lista es tan fácil como utilizar otra lista por comprensión. Añade también esta función al módulo `obo.py`.

``` python
# Dada una lista de palabras, retira cualquiera que esté
# en la lista de palabras funcionales.

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]
``` 

Ensamblar todo
--------------

Ahora tenemos todo lo que necesitamos para determinar frecuencias de palabras en páginas Web. Copia lo siguiente en Komodo Edit, guárdalo como `html-to-freq-2.py` y ejecútalo.

``` python
# html-to-freq-2.py

import urllib2
import obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
```

Si todo va bien, tus datos de salida se verán como esto:

``` python
(25, 'house')
(20, 'yes')
(20, 'prisoner')
(19, 'mr')
(17, 'man')
(15, 'akerman')
(14, 'mob')
(13, 'black')
(12, 'night')
(11, 'saw')
(9, 'went')
(9, 'sworn')
(9, 'room')
(9, 'pair')
(9, 'know')
(9, 'face')
(8, 'time')
(8, 'thing')
(8, 'june')
(8, 'believe')
...
```

## Lecturas sugeridas

Lutz, Learning Python

-   Ch. 9: Tuples, Files, and Everything Else
-   Ch. 11: Assignment, Expressions, and print
-   Ch. 12: if Tests
-   Ch. 13: while and for Loops

Pilgrim, Diving into Python

-   Ch. 7: [Regular Expressions][]

### Sicronización de código

Para seguir a lo largo de las lecciones futuras es importante que tengas los archivos correctos y programas en el directorio "programming-historian" de tu disco duro. Al final de cada lección puedes descargar el archivo zip "programming-historian" para asegurarte que tienes el código correcto.

-   programming-historian-5 ([zip sync][])

  [lista por comprensión]: http://docs.python.org/tutorial/datastructures.html#list-comprehensions
  [informáticos de Glasgow]: http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
  [Regular Expressions]: http://www.diveintopython.net/regular_expressions/index.html
  [zip]: ../assets/python-lessons4.zip
  [zip sync]: ../assets/python-lessons5.zip
