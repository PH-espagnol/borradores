---
title: Introducción al control de versiones con GitHub Desktop
authors: 
- Daniel van Strien
date: 2016-06-17
reviewers:
- Ethan Miller
- Lisa Spiro
translator:
Antonio Rojas Castro
layout: default
difficulty: 1
---

## Objetivos de la lección

Con esta lección aprenderás el funcionamiento básico de los sistemas de control de versiones, entenderás por qué son útiles y te familiarizarás con [GitHub Desktop] (https://desktop.github.com/), un control de versiones de documentos en formato de texto plano. Al finalizar la lección, serás capaz de entender:

* qué es un control de versiones y por qué puede ser útil
* las diferencias entre Git y GitHub
* cómo utilizar un control de versiones con la interfaz gráfica 'GitHub Desktop'
* qué otros recursos pueden ayudarte a implementar un control de versiones para investigar.

## *Software* necesario

GitHub Desktop is currently only available for Windows and Mac. If you use Linux you will probably already be familiar with the command line and will be able to use the Command Line version of Git. 


## ¿Qué es un control de versiones y por qué debería utilizarlo? 

Antes de ponerse manos a la obra, conviene comprender qué es un control de versiones y por qué puede ser útil para tu investigación. En términos generales, un control de versiones consiste en tomar instantáneas de tus archivos a lo largo del proceso de creación. La mayoría de personas, de hecho, trabajan con algún sistema de control de versiones para gestionar sus archivos. A menudo, el control tiene lugar guardando distintas versiones de un mismo archivo. Por ejemplo, no es raro encontrarnos antes un directorio que contiene los siguientes archivos:

```
midocumento.txt
midocumentoversion2.txt
midocumentoconrevisiones.txt
midocumentofinal.txt
```
Esta forma de nombrar los archivos puede ser más o menos sistemática. Si añadimos fechas, puede ser un poco más fácil seguir los cambios:

```
midocumento2016-01-06.txt
midocumento2016-01-08.txt
```
Aunque este método sea un poco más fácil de entender, sigue habiendo problemas. En primer lugar, este método no registra o describe qué cambios se han producido entre uno y otro archivo guardado. Pueden ser pequeñas correcciones de erratas, o bien tratarse de la reescritura de pasajes enteros o incluso de una modificación mayor, por ejemplo, de la estructura del documento. Además si quieres revertir alguno de estos cambios, tendrás que averiguar cuándo se hizo el cambio y deshacerlo.

Con un control de versiones se persigue solucionar este tipo de problemas mediante la puesta en marcha de un registro sistemático de cambios en los archivos. A grandes rasgos, puede afirmarse que el contro de versiones realiza instantáneas de los archivos a lo largo del tiempo. Estas instantáneas documentan el momento en que fueron tomadas pero también qué cambios tuvieron lugar entre cada una de ellas, lo cual permite recuperar una version más antigua de tu archivo. A partir de aquí se abren un sinfín de posibilidades gracias al control de versiones.


### ¿Por qué un control de versiones para documentos?

A medida que para investigar utilizamos herramientas digitales y almacenamiento en formato digital, se vuelve relevantes reflexionar sobre cómo optimizar la gestión de nuestros datos. Más aún, el control de versiones puede ser indispensable si tenemos intención de colaborar con otros investigadores. Aunque el control de versiones fue diseñado en sus orígenes para tratar archivos de código, creemos que la gestión de documentos también se beneficiaría. La lección que proponemos no cubre todas las ventajas del control de versiones pero al finalizarla podrás llevar a cabo las siguientes tareas:

* rastrear el desarrollo y los cambios de tus documentos
* registrar los cambios que has hecho de una manera que puedas entender posteriormente
* experimentar con versiones distintas de un documento al mismo tiempo que conservas la más antigua
* fusionar dos versiones de un documento y administrar los conflictos existentes entre distintas versiones
* revertir cambios y volver atrás gracias al historial de versiones anteriores de tu documento

En concreto, el control de versiones es útil para facilitar la colaboración. De hecho, una de las razones que explican el origen del control de cambios es que permitera a varias personas trabajar al mismo tiempo en un proyecto de considerables dimensiones y utilizar Git para administrar las fuentes del núcleo Linux. Utilizar un control de versiones favorece la colaboración debido a su flexibilidad. Por ejemplo, dos personas pueden trabajar en un mismo documento al mismo tiempo y fusionar los cambios. Si existe un 'conflicto' entre las dos versiones, el sistema de control permitiría al usuario ver el conflicto y decidir cómo 'fusionar' las dos versiones dando lugar a una 'tercera' version. De esta manera, conservarías la 'historia' del documento, es decir, las versiones anteriores y, en consecuencia, podrías revertir el proceso eligiendo una versión más antigua.
 
No es necesario, sin embargo, poner en marcha un control de versiones para todos tus documentos. En algunas ocasiones resulta muy útil; por ejemplo, para escribir artículos, libros o tesis doctorales.

La implementación del control de versiones que proponemos en esta lección está pensada para que los documentos sean públicos. No obostante, puedes utilizar un control de versión y mantener tus documentos ocultos de manera permanente o bien hasta que decidas publicarlos en línea. 

## Diferencias entre Git y GitHub

Aunque a veces se utilizan como sinónimos, Git y GitHub no son lo mismo. Git es un sistema específico diseñado para controlar versiones en un entorno Linux; fue desarrollado por Linus Torvalds con el objetivo primordial de gestionar código fuente. Por supuesto, existen otros [controles de versiones] (https://en.wikipedia.org/wiki/Comparison_of_version_control_software) pero su uso no está tan difundido. Git puede referirse tanto a una forma de controlar versiones como al programa utilizado para llevar a cabo dicha tarea.

En cambio, GitHub es una compañía que aloja repositorios Git (más detalles abajo) y que proporciona un programa específico para usar Git. Entre las modalidades de uso, destaca el programa 'GitHub Desktop', sobre el que trata este tutorial. Actualmente, si tenemos en cuenta el [número de proyectos y de usuarios] (https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities#Popularity), es posible afirmar que GitHub es la plataforma más popular para alojar en abierto el código de proyectos digitales.

Pese a que GitHub está diseñado originalmente para publicar código fuente, algunos proyectos, como *Programming Historian en español*, lo utilizan para controlar las versiones y para gestionar el flujo de trabajo de sus publicaciones, libros de texto, etc. Así que familiarizarte con GitHub no solo te permitirá controlar las versiones de tu documento sino contribuir a los proyectos que utilizan GitHub. En esta lección nuestro objetivo es ofrecer una introducción al funcionamiento básico de los objetivos y principios del control de versiones de un archivo de texto plano. La lección no es exhaustiva pero proporciona un punto de partida para que puedas seguir aprendiendo por tu cuenta.

### ¿Por qué no utilizar Dropbox o Google Drive?

Dropbox, Google Drive y otros servicios ofrecen alguan forma de controlar las versiones en sus sistemas. A veces esto es suficiente para tus necesidades. Sin embargo, existen algunas ventajas por las que vale la pena utilizar un control de versiones como Git:

* Mayor cobertura de lenguaje: Git admite tanto texto como lenguajes de programación. A medida que la investigación incluye métodos informáticos y herramientas digitales, se vuelve necesario disponer de una plataforma que gestione publicaciones tradicionales (artículos, libros, etc.) pero también nuevos tipos de publicaciones como código, conjunto de datos, etc.
* Más control: un sistema de control de versiones te dará mayor poder para gestionar los cambios de tus documentos.
* Historial más útil: si utilizas un sistema de control como Git, podrás producir un historial de tu documento. A través de este historial tú y tus colaboradores podréis navegar fácilmente por las distintas etapas del documento. 

### Algunos proyectos académicos que utilizan control de versiones

Utilizar un control de versiones se ha consolidado en algunas disciplinas científicas, aunque su adopción está lejos de ser universal. En las Humanidades y en las Ciencias Sociales, el uso de Git es mucho menos frecuente. Los proyectos que listamos a continuación muestran algunas de las posibilidades del uso de Git en un entorno académico: 

*  [The Programming Historian en español](https://github.com/programminghistorian/jekyll) utiliza GitHub en su flujo de trabajo para gestionar la [revista] (https://github.com/programminghistorian/jekyll/issues), las [lecciones](http://programminghistorian.org/new-lesson-workflow) y para producir la [web](http://programminghistorian.org/posts/how-we-moved-to-github).
* [Python Programming for the Humanities](https://github.com/fbkarsdorp/python-course) es un tutorial introductorio sobre el lenguaje de programación Python. 
* [ProfHacker](http://chronicle.com/blogs/profhacker/tag/github) ha publicado varias entradas de blog sobre proyectos que usan GitHub en un contexto académico.

Nuevos proyectos surgen de manera constante y muchas de las herramientas que utilizas en las Humanidades Digitales se hospedan en GitHub; por este motivo, GitHub puede ser útil para utilizar con mayor facilidad alguna de estas herramientas.

## Cómo empezar

GitHub Desktop, la aplicación de escritorio de GitHub, te permitirá empezar a utilizar un control de versiones sin problemas. GitHub Desktop es, de hecho, una Interfaz Gráfica de Usuario (GUI) diseñada para facilitar el uso de Git. Las interfaces gráficas de usuario permiten al usuario interactuar con el programa a través de un dispositivo visual que reemplaza la línea de comandos. Aunque utilizar la línea de comandos ofrece muchas ventajas a largo plazo, si utilizas GitHub Desktop reducirás la curva de aprendizaje; encontrarás más recursos sobre la línea de comando al final de la lección.

### Una breve nota sobre la terminología

Uno de los aspecots más complejos del uso de GitHub es la terminología. El nombre de algunos de los comandos se entienden fácilmente porque son evidentes, pero otros no tanto. En este tutorial intentaremos explicar brevemente los términos poco comunes. Si te pierdes, puedes consultar el [glosario](https://help.github.com/articles/github-glossary/) de GitHub. Sin embargo, creemos que es mejor ir aprendiendo los términos sobre la marcha, a medida que se utiliza el programa, en lugar de intentar comprender toda la terminología antes de empezar. 

### Regístrate con una cuenta en GitHub

Puesto que vamos a utilizar GitHub, necesitarás registrate con una cuenta en [GitHub](GitHub.com) si no lo has hecho ya. Para [estudiantes] (https://education.github.com/pack) e [investigadores] (https://github.com/blog/1840-improving-github-for-science), GitHub ofrece repositorios privados de manera gratuita. Este tipo de repositorios no son necesarios pero quizá esta opción te seduzca si quieres mantener tu trabajo en privado.

### Instala GitHub Desktop

Una vez te hayas registrado, el proceso de instalación variará dependiendo de si utilizas Windows o Mac. Las instrucciones pueden cambiar, por lo que te recomendamos que sigas el procedimiento explicado en la [página de instalación de GitHub] (https://desktop.github.com/). Tras descargar GitHub Desktop e instalarlo, ya podemos empezar a usar el programa con un archivo de texto plano.

## Version Controlling a Plain Text Document

Los sistemas de control de versiones como Git funcionan mejor con archivos de texto plano. Este tipo de archivos contienen un marcado muy sencillo; por el contrario, los archivos Word (u otros generados con procesadores similares) producen código que no es legible para los humanos. Además, cualquier archivo guardado como '.txt' puede abrirse sin problemas con Word, LibreOffice o Notepad. La 'portabilidad' es la principal ventaja del texto plano pues estos archivos pueden abrirse y ejecutarse en la mayoría de ordenadores.

Pese a las ventajas evidentes de escribir nuestros documentos en texto plano, también debemos señalar algunas limitaciones. Los archivos de texto plano en sí no permiten marcar algunas palabras en *cursiva* o bien con **negrita**; tampoco es posible incluir encabezado o citaciones. Para realizar esto necesitaremos una sintaxis adicional: 'markdown'. 

Con Markdown podremos, pues, dar formato aj nuestro texto plano. Seguramente hayas utilizado HTML o LaTex en el pasado. Estos lenguajes de marcado también expresan información sobre el estilo y la estrcutura del documento. No obstante, el propósito de Markdown es minimizar el marcado, lo cual significa que es más fácil centrarse en el contenido, en la escritura, sin preocuparse en cómo marcar el texto -de ahí el nombre de 'markdown'-. 

Esta lección no cubre la sintaxis Markdown por razones de espacio pero es útil explorar su funcionamiento una vez te sientas cómodo con el control de versiones. Conviene señalar, por otra parte, que GitHub integra una versión propia de la sintaxis Markdown. Si añades la sintaxis Markdown a tus docuemntos, tu control de versiones gestionado con GitHub Desktop visualizará de manera correcta tu documento en la web. La mejor manera de aprender Markdown es con un poco de práctica. Puedes empezar con nuestra [Introducción a Markdown](http://programminghistorian.org/lessons/getting-started-with-markdown) escrita por Sarah Simpkin, o bien con la lección  [Escritura sostenible con Pandoc y Markdown](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) escrita por Dennis Tenen y Grant Wythoff. 

### Editores de texto

Para escribir un documento de texto plano necesitamos un editor. Hay muchos editores disponibles, algunos gratuitos, otros de pago. Algunos son fáciles de usar mientras que otros tienen una curva de aprendizaje y un potencial que sobrepasa las funciones de un editor de texto. A largo plazo, un editor avanzado como Vim o Emacs puede ahorrarte tiempo pero de momento puedes empezar con un editor más simple. Por ejemplo, [Atom](https://atom.io/) es un buen editor desarrollado por GitHub que destaca la sintaxis Markdown y, además, se integra con la plataforma GitHub. Es gratuito y su código es abierto; además, incluye un [manual] (http://flight-manual.atom.io/) de instrucciones muy exhaustivo.

Si no quieres instalar un programa nuevo, puedes utilizar uno de los editores que incluidos en tu ordenador como TextEdit para Mac o bien Notepad para Windows. Si decides continuar aprendiendo Markdown en el futuro, te recomendamos utilizar un editor de texto que destaque la sintaxis Markdown, entre otras funcionalidades.

### Crear un documento

Podemos empezar creando un documento muy sencillo.

```
¡Hola mundo!
```

Añade este texto (o algo parecido) en documento de texto plano nuevo. ¿Listo? A continuación, guarda el archivo con la extensión '.md'. Esta extensión es la más popular para los archivos markdown aunque a veces es posible utilizar otras. A veces el editor de texto guarda los archivos como Rich Text Format (RTF) por defecto, así que asegúrate de que el archivo se guarda en formato de texto plano un directorio nuevo. Si ocurre esto, puedes cambiarlo en la pestaña preferencias u opciones de tu editor. En cualquier caso, identifica tu archivo y tu directorio con un nombre semánticamente claro. Aunque la extensión utilizada sea'.md', hay que asegurarse de que el archivo es de 'texto plano'. Por lo general, la codificación del documento no será ningún problema una vez te acostumbres a usar el editor de texto.

Para utilizar de manera efectiva el control de versiones de Git, es importante organizar tu proyecto en directorios. Git rastrea el contenido de cada directorio creando un *repositorio* a partir de cada uno de ellos. Un repositorio se compone de todos los archivos que están siendo *controlados* por Git. Lo mejor es crear un directorio para cada proyecto en el que trabajas; por ejemplo, un repositorio para un artículo que estés escribiendo, otro para la composición de tu libro, uno más para el código en desarrollo, etc. Estos directorios son como las carpetas normales y corrientes que tienes en tu ordenador; la única particularidad es que los archivos deben ser añadidos de manera expresa al repositorio para que sean controlados mediante Git. 

### Añadir un documento

Hay varias formas de *añadir* un archivo para que GitHub Desktop lo controle. Por ejemplo, podemos arrastrar un directorio con el archivo a GitHub Desktop. Si haces esto, el programa te preguntará si quieres crear un repositorio para este directorio. Otra manera consiste en cliclar sobre el icono 'más' para abrir el buscador y elegir la carpeta que queremos añadir.

{% include figure.html filename="getting-started-with-github-desktop-1.png" caption="Adding a folder to GitHub Desktop" %}

Una vez hemos añadido nuestra carpeta podremos verla en la lista de repositorios situada en la columna izquierda. 

{% include figure.html filename="getting-started-with-github-desktop-2.png" caption="Adding a folder to GitHub Desktop" %}

Si clicamos sobre el repositorio que acabamos de añadir, podremos ver los archivos contenidos. En este menú, además, podremos elegir qué archivos queremos rastrear pues a veces trabajamos en proyectos con archivos que no lo requieren. Al lado, a la derecha, se visualizan los documentos. 

 


If we show hidden folders in the folder we have just added to GitHub you will see that the folder now contains an extra folder with the name '.git'. This folder is how GitHub desktop tracks changes we make within our version controlled folder whether these changes be adding new files or modifying existing ones. 

{% include figure.html filename="getting-started-with-github-desktop-18.png" caption="The folder being watched by GitHub desktop" %}


Lets go back to the document in our text editor and add something new. 

```
Hello world!
a second line
```

Save the changes to your file and go back to GitHub Desktop. You will see that these new lines of text appear. This lets us know that GitHub is able to see changes in your file but at the moment these changes haven't been recorded in an official 'snapshot' of your repository. 

To do this we need to **commit** our changes.

### Committing Changes  

A **commit** tells Git that you made some changes which you want to record. Though a **commit** seems similar to saving a file, there are different aims behind 'committing' changes compared to saving changes. Though people sometimes save different versions of a document, often you are saving a document merely to record the version as it is when it is saved. Saving the document means you can close the file and return to it in the same state later on. **Commits**, however, take a snapshot of the file at that point and allow you to document information about the changes made to the document. 

{% include figure.html filename="getting-started-with-github-desktop-3.png" caption="Committing changes" %}

To commit changes you must give a summary of the changes and include an optional message. It is important that you think carefully about when to make commits. The advantages of version control taking snapshots of your changes regularly relies on you making commits. It is often tempting to just commit changes when you have finished working on a document but this might not reflect when important changes occurred.

When you commit you will see 'commit to master'. This refers to the 'master branch'. Within a Git repository it is possible to have multiple 'branches.' These different branches are essentially different places in which to work. Often they are used to test new ideas or work on a particular feature. Initially it is not necessary to use the branches feature of GitHub, but you may want to learn to use it in the future, particularly if you want to use GitHub to collaborate on a repository with other people.  

A useful way to think about commits is as the 'history' of your document. Each commit records a development or change made to the documents in your repository; the history of the document can be traced by looking at all of the commits. For this history to be useful later on, either for ourselves or for someone else, it is important that this history is recorded at relevant points. Trying to make commits 'atomic' is an important consideration. What this means is that each commit 'makes sense' on its own. The changes in the commit and the message are understandable without having to look at surrounding commits. 

Thinking about how version control is used for code can make this idea more clear. When a new feature, or a bug fix, is added to some software it is important that these features can be isolated. If a commit includes changes to different aspects of the code it makes it hard to isolate when problems were introduced. It is also makes it difficult to remove a single change that is causing problems if other changes are included in the commit. 

There are differences between using version control for code and text which will impact on how you make commits. However, the aim of making commits 'atomic' can still be used. For example, it would make sense to commit changes to the structure of a document separately to grammar and spelling fixes. If you later decided to change the structure you would likely still want to maintain your other fixes. 

### Commit Messages

It is important that you use meaningful commit summaries and messages. Writing good commit messages requires some prior thought. Messages that make sense to you as an explanation of changes when you make a commit may no longer make sense to you in the future. If you are going to use version control in collaboration with other people it is especially important that other people can understand your commit messages. Version control as a system for managing changes to documents works best when active thought goes into using the software. It is therefore particularly important when collaborating with other that there is a shared understanding and approach to using version control. 

One way of addressing this is to try to follow a 'commit style'. One influential [suggestion](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) for a commit style has been made by Tim Pope. The style suggestions made by Tim Pope are partly ['built in'](https://github.com/blog/926-shiny-new-commit-styles) to the GitHub Desktop commit message interface but understanding the format will help ensure a consistent approach. The following commit message paraphrases Tim Pope's suggested format to focus on commits relating to text rather than code:

```
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary. In some contexts, the first line is treated as the subject of an email and the rest of the text as the body.  

Write your commit message in the present tense: "Fix typos" and not "Fixed
typos."  This convention matches with other aspects Git commands.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, preceded by a
  single space, with blank lines in between, but conventions vary here
```

The GitHub Desktop interface takes care of some of these 'style' issues but it is good to be conscious about how you write commit messages. It will not always be necessary to write an extensive commit message but is important that the message is clear about the changes being made and that the commits and the commit message are useful 'atomically'. 

An example of a short but clear commit message in the context of written work:

```
Reorder document outline

Move the methods section below the sources section in the document outline. 
Why? Some of the methods discussion doesn't make sense without a description 
of the sources being used. 
```

A potentially useful parallel to writing good commit messages is the messages included when you edit a Wikipedia or Wiki page. When writing these messages it is important to explain the changes you made to the page and the reasoning behind these changes so that other people who see the changes can understand your reasoning. Approaching commit messages as if they will be read not only by yourself but also by others will help you write clear and meaningful commit messages.  

### Building a Good Repository

The benefits of using version control rely to a large degree on using the system effectively. This means thinking about when to make commits and how to best convey the changes in that commit in a message. Focusing on making both your messages and your commits 'atomic' will make it easier to 'move' through different stages of your repositories history. A good repository will allow you to easily understand changes that were made at different stages, will be understood by other people and will help you reflect on the changes you make to a document. 

There is some difference between how you would manage a repository primarily focused on code and one focused on text. Both, however, benefit from clear and logical organisation. This is something that is important to do with your research data regardless of whether you are version controlling it and/or making it public. For a useful introduction to managing research data see James Baker's lesson [Preserving Your Research Data](http://programminghistorian.org/lessons/preserving-your-research-data). 

### Publishing Your Repository

At the moment we are only recording our changes locally. We may be happy to only store our changes locally (it is still important to back our files up) but we may want to upload our repository onto GitHub to make it public or to have it stored outside of our computer. The process of doing this through GitHub Desktop is straightforward. On GitHub desktop you 'publish' repositories. This will **push** your repository from your computer to the GitHub website and set up a **remote** repository in the process. 

{% include figure.html filename="getting-started-with-github-desktop-4.png" caption="Publishing a repository" %}

Once you have 'published' your repository it will be viewable on your profile at GitHub's website. It is possible to setup a private repository on GitHub but this requires you to have either signed up as a [student](https://education.github.com/pack) or [researcher](https://github.com/blog/1840-improving-github-for-science) or to pay for a [GitHub subscription](https://github.com/pricing). If you haven't signed up for one of these options you will not be able to create a private repository without first signing up for a subscription. Unless you need to start a subscription you can safely ignore the 'billing information' section. For this lesson it will be fine to publish a public repository. To quickly view your repository online you can use the repository menu and choose 'View on GitHub'. This will bring you to your repository online in your browser. 

{% include figure.html filename="getting-started-with-github-desktop-5.png" caption="Repository menu" %}

You can now see your document in your online repository.

{% include figure.html filename="getting-started-with-github-desktop-6.png" caption="The online repository you have published" %}

Once your document is online, you can continue to make local changes to your file. But you will have to **sync** your local changes to reflect these changes in the published GitHub repository. GitHub stores changes both locally (on your computer) and remotely (on their servers). It is important to keep these changes in sync. On GitHub Desktop this process is simplified by using a sync option rather than by using the **push** and **pull** commands used on the command line. You will see a 'sync' button on GitHub Desktop. This will ensure your local (computer) and remote (GitHub server) repositories are the same. If you want to work on your document before 'publishing it' you can choose to make commits without syncing. This will allow you to implement version control early on whilst keeping the changes local to your computer initially.  

### Making Changes Remotely

It is also possible to make a change to your repository on the web interface. Clicking on the name of the file will take you to a new page showing your document. 

{% include figure.html filename="getting-started-with-github-desktop-7.png" caption="The view of your document online" %}

(Note: At this point it might seem strange that all the text appears on one line, when your local file had two lines. This is because in Markdown, syntax paragraphs must be broken using a blank line; two consecutive lines are interpreted as a single paragraph. If we had used the file extension '.txt' we would have had a line break appear here, but using the extension '.md' told the GitHub web interface to preview the document using Markdown rules. This is another reason that using a text editor which includes facilities for rendering your Markdown file will be useful when you are first using the format.)  

From the web interface you have a variety of options available to you, including viewing the history of changes, viewing the file in GitHub Desktop, and deleting it. You can also see some other options next to 'code'. These options will not be so important to begin with but you may want to use them in the future. For now we will try editing a file in the web interface and syncing these changes to our local repository.

Click on the edit option.

{% include figure.html filename="getting-started-with-github-desktop-8.png" caption="The edit link" %}

You will now be able to edit the file and add some new text. 

{% include figure.html filename="getting-started-with-github-desktop-9.png" caption="The editing view" %}

Once you have made some changes to your file, you will again see the option to commit changes at the bottom of the text entry box. 

{% include figure.html filename="getting-started-with-github-desktop-10.png" caption="The remote commit view" %}


Once you have committed these changes they will be stored on the remote repository. To get them back onto our computer we need to sync our these changes. We will see the 'sync' button on GitHub Desktop. 

{% include figure.html filename="getting-started-with-github-desktop-11.png" caption="The sync button" %}

We now have our remote changes synced back onto our computer.

{% include figure.html filename="getting-started-with-github-desktop-12.png" caption="Our document with remote changes synced" %}

You can see from this view that we now have the text with changes highlighted in green and red. Red indicates where things have been removed while green indicates additions. This can be useful for viewing the edits you have made before making a commit and helps you spot whether all the changes are ones you want to commit. On the left you will see a history of the changes you have made. At the moment this is very brief but as you work on a project the history might become much longer. Being able to see the changes you have made at different stages can be very useful.

## Managing Conflicts

A 'conflict' emerges when you try to merge or 'sync' two versions of a document with changes which conflict with each other. If you are careful about committing and syncing local changes (on your computer) then it is unlikely you will run into this issue, but if you do it can be resolved fairly easily.

The most likely way a conflict will emerge is if you make a change remotely (on the GitHub website), and then make a subsequent change on your local machine without first synching the changes from the website.  If you make changes in different parts of a document these changes can be 'merged' or synced together without any conflict. But these changes might conflict with one another (i.e. if you try and change the same line of the document in two different ways).

An example will help illustrate how conflicts can emerge and how to deal with them. Say we add a change to our remote repository (on the GitHub website).

{% include figure.html filename="getting-started-with-github-desktop-13.png" caption="A remote change to our document" %}

We commit this change on the website and subsequently make a change to the document on our local machine. 

{% include figure.html filename="getting-started-with-github-desktop-14.png" caption="A local change to our document" %}

If we now commit our local changes and then sync our changes we get a message warning us about sync conflicts.

{% include figure.html filename="getting-started-with-github-desktop-15.png" caption="GitHub desktop warning of sync conflicts" %}

This is not a big problem. What you will need to do is manage these conflicts. GitHub desktop offers you the option of opening the file with the sync conflicts. 

{% include figure.html filename="getting-started-with-github-desktop-16.png" caption="GitHub desktop options for opening file containing conflicts" %}

If we choose to open file with an external editor the document will open with whichever text editor/application we have chosen as the default for opening markdown files. If you haven't set a default application you can choose to 'show in finder'. This will show the folder with your file. From here you can open it with your preferred editor. 

If we take a look at the file we will see Git has highlighted the conflicting section. 

{% include figure.html filename="getting-started-with-github-desktop-17.png" caption="Conflicts highlighted in our document" %}

You will see that the conflicting section is marked with `<<<<<<<` and ends with `>>>>>>>`. These are known as the conflict markers. The two conflicting blocks are divided by a `=======` line. There are a number of approaches to dealing with a conflict. You could choose to go with either of the changes by deleting the version you no longer want and removing the conflict markers. You could also decide to change the section entirely and not choose either of the options. Once you have 'resolved' the conflict you can go onto commit and sync your changes as usual. When you go to commit your changes you see that GitHub desktop specifies that the commit is to merge a conflict. This is useful if you later want to go back and review how you managed any conflicts. 

This may seem like a convoluted approach to dealing with conflicts but it is very useful because of the control given to you in dealing with conflicts. If conflicts emerge on a system like Dropbox the result is two files being created. Although this is better than potentially loosing important changes, it also means you still have to look at these two documents and decide how you are going to merge them. If you are careful about always syncing changes you will be able to avoid having to deal with conflicts. When collaborating the likelihood for conflicts increases so it is useful to be aware of how to deal with conflicts before you begin to collaborate using GitHub.

## Version Control in a Plain Text Workflow  

So far we have only implemented version control with a very basic document. Learning more about Markdown and writing in plain text will allow you to use version control in more the sorts of documents you would use in your day-to-day work. Version controlling a Markdown document will allow you to learn the Markdown syntax while reinforcing your understanding of version controlling documents. [Sustainable Authorship in Plain Text using Pandoc and Markdown](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) by Dennis Tenen and Grant Wythoff will provide you with an understanding of how you could use plain text for academic writing using Pandoc and Markdown. Pandoc allows you to convert Markdown formated Plain Text files into numerous different formats including HTML, PDF and Word. The combination of Markdown, Pandoc and Version Control will provide a powerful, sustainable and flexible approach to academic writing.

The workflow introduced in this lesson can also be used as a foundation to create static websites hosted on GitHub. Once you are comfortable using GitHub Desktop, you may wish to proceed to Amanda Visconti's lesson, [Building a Static Website with Jekyll and GitHub Pages](../lessons/building-static-sites-with-jekyll-github-pages).

## Further Resources

GitHub Desktop offers an easy way of getting started with GitHub and version control. Depending on your use case GitHub desktop may be sufficient for your needs. If you are already familiar with using the Command Line then using Git on the Command Line may offer some advantages. Version control systems like Git have a lot of features available to use. Some of these will only be applicable in very specific contexts, others will be more commonly useful. Alongside the lesson suggested above the resources below will allow you to gain a deeper understanding of version control.

* The [GitHub Desktop](https://desktop.github.com/) and the GitHub Desktop [documentation](https://help.github.com/desktop/) outlines more features included in GitHub Desktop. 
* GitHub provides extensive support in the form of [guides](https://guides.github.com/) and [help](https://help.github.com/). 
* [GitHub Glossary](https://help.github.com/articles/github-glossary/) outlines the most commonly used GitHub/Git terminology. 
* [Atlassian](https://www.atlassian.com/git/tutorials): Some in-depth but clear tutorials on using git. There is a focus on explaining the differences between git and other version control systems which may not be relevant but will help you understand the inner workings of git in greater detail. 
* [Pro Git](https://git-scm.com/book/en/v2): A book on Git. Begins with the basics and later covers more advanced usage of Git.
* For [students](https://education.github.com/pack) and [researchers](https://github.com/blog/1840-improving-github-for-science) GitHub offers free private repositories. These repositories may be useful for early drafts of work or for managing notes which are never intended to becoming public. Note: it might not be a good idea to store things which are very sensitive on GitHub even in a private repository. 
* [ProfHacker](http://chronicle.com/blogs/profhacker/tag/github) has posts on various projects on using GitHub in an academic context. 
* [GitHub, Academia, and Collaborative Writing](https://www.hastac.org/blogs/harrisonm/2013/10/12/github-academia-and-collaborative-writing) discusses using GitHub for collaborative writing. 
* [Introduction to the Bash Command Line](http://programminghistorian.org/lessons/intro-to-bash) introduces the command line which will be useful preparation for using GitHub on the command line.

