# :question: Tutorial

Aquí encontrarás un breve resumen de cómo funciona la sintaxis del lenguaje. Más abajo encontrarás la <a href="#book-lista-de-comandos">lista completa</a> de comandos.

## Sintaxis

### :page_facing_up: Archivos

Existen comandos que requieren un archivo como argumento, como por ejemplo 'view', que permite visualizar su contenido.
Para pasar como argumento el archivo escribes su nombre con o sin comillas dobles (""), ambas formas son válidas.
    
    view archivo.txt
    view "archivo.txt"

En caso de que el nombre del archivo contenga espacios, deberás escribirlo con comillas dobles obligatorialemnte.

    view "Mi archivo de texto.txt"

La extensión es opcional, puedes manipular archivos sin extensión sin ningún problema.

    view archivo


### :open_file_folder: Directorios

Para los directorios aplica la misma regla.

    cd ruta/directorio
    cd ruta
    cd "Ruta directorio/Con espacios"


### :memo: Utilitarios

La mayoría de estos comandos no requiere ningún argumento, puesto que realizan funciones generales sin afectar ningún archivo o directorio.

    back
    clear
    exit

Salvo 2 excepciones, que pueden llevar opcionalmente banderas o 'flags'. Dichos comandos son list (o 'ls' en su forma corta) y help.

Para el caso de ls/list, comando que lista todo lo que esté en el directorio actual, puede llevar las flags '-f' y '-d' para listar únicamente archivos o directorios respectivamente.

    list
    list -f
    ls -d

Para el caso de help, tiene las flags '-f', '-d', y '-u'. Puedes encontrar más información de estas flags <a href="#flags">aquí.</a>

    help
    help -u

Adicionalmente, puedes escribir un comando seguido de 'help' para ver más información sobre dicho comando. Actualmente los únicos comandos que tienen esta opción son 'help' y 'list'

    help help
    help list

# :book: Lista de comandos
Aquí está la lista completa de comandos

* <a href="#page_facing_up-manipulación-de-archivos">Comandos de archivos</a>
* <a href="#open_file_folder-manipulación-de-directorios">Comandos de directorios</a>
* <a href="#memo-comandos-utilitarios">Comandos utilitarios</a>

## :page_facing_up: Manipulación de archivos</h2>
Con estos comandos vas a poder realizar de manera sencilla las tareas más comunes a la hora de utilizar archivos, tales como copiar, mover, renombrar, eliminar, etc.

* ### copy
  <p>Copia un archivo en el directorio especificado.</p>

      copy archivo.txt /ruta/de/destino

* ### create
  <p>Crea un nuevo archivo si este no existe.</p>

      create archivo.txt

* ### del
  <p>Elimina un archivo.</p>

      del archivo.txt

* ### double
  <p>Duplica un archivo en el directorio actual.</p>

      double archivo.txt

* ### move
  <p>Mueve un archivo en el directorio especificado.</p>

      move archivo.txt /ruta/de/destino

* ### open
  <p>Abre o ejecuta un archivo.</p>

      open program.exe

* ### rename
  <p>Permite renombrar un archivo.</p>

      rename archivo.txt archivo_renombrado.txt
  
* ### view
  <p>Permite visualizar en pantalla el contenido de un archivo de texto plano.</p>

      view archivo.txt
  
* ### write
  <p>Añade una nueva línea en un archivo de texto plano.</p>

      write archivo.txt "Texto a escribir"

  > Debes colocar el texto entre comillas dobles ("") obligatoriamente.
  


## :open_file_folder: Manipulación de directorios</h2>
Con estos comandos vas a poder manipular los directorios, acceder a ellos, inspeccionarlos y eliminarlos

* ### back
  <p>Regresa un nivel en el directorio.</p>

      back

* ### cd
  <p>Accede a un directorio.</p>

      cd /ruta/del/directorio

* ### copy
  <p>Copia una carpeta en el directorio especificado.</p>

      copy /ruta/del/directorio /ruta/de/destino

* ### create -d
  <p>Crea nueva carpeta en el direvtorio actual..</p>

      create -d "Nombre Carpeta"

* ### del
  <p>Elimina un directorio.</p>

      del /ruta/del/directorio

* ### double
  <p>Duplica un directorio en el directorio actual.</p>

      double /ruta/del/directorio

* ### home
  <p>Accede al directorio raíz del usuario.</p>

      home
  
* ### insp
  <p>Muestra un recuento de los archivos y carpetas de un directorio.</p>

      insp /ruta/del/directorio/

  > Si no se introduce un directorio se inspeccionará el directorio actual

* ### move
  <p>Mueve un directorio en el directorio especificado.</p>

      move /directorio/ /ruta/de/destino

* ### rename
  <p>Permite renombrar un directorio.</p>

      rename /directorio/ /NuevoNombre/
  


## :memo: Comandos utilitarios</h2>
Comandos para funciones generales.

* ### clear
  <p>Limpia la consola.</p>

      clear

* ### exec
  <p>Ejecuta un script de NymaFE desde un archivo.</p>

      exec script.nfe

  > Obligatoriamente debe ser un archivo .nfe que contenga un script válido.

* ### exit
  <p>Sale del intérprete.</p>

      exit

* ### help
  <p>Muestra la lista de comandos.</p>

      help

  #### Flags:

  * -f Para listar comandos de manipulación de archivos

        help -f

  * -d Para listar comandos de manipulación de directorios

        help -d

  * -u Para listar comandos utilitarios

        help -u

  * (comando) Para mostrar la ayuda de un comando

        help list

* ### info
  <p>Imprime un mensaje en consola.</p>

      info "Mensaje"

* ### ls / list
  <p>Lista archivos y carpetas en el directorio actual</p>

      list
      ls
  
  #### Flags:

  * -f Para listar solo archivos

        list -f

  * -d Para listar solo directorios

        list -d
      
  > Ambos comandos "ls" y "list" funcionan con las flags.
