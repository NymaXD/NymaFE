# NymaFE

## :construction: :warning: Proyecto en desarrollo :warning: :construction:

<p align=justify>NymaFE es un lenguaje DSL que permite manipular archivos y directorios en nuestro sistema operativo a través de comandos que pretenden ser simples y fáciles de memorizar.</p>

<p align=justify>Con este lenguaje vas a ser capaz de manipular archivos :page_with_curl: y carpetas :file_folder: en un directorio, leer su contenido, abrirlos, renombrarlos, copiarlos, etc.</p>

## :page_facing_up: Manipulación de archivos</h2>
Con estos comandos vas a poder realizar de manera sencilla las tareas más comunes a la hora de utilizar archivos, tales como copiar, mover, renombrar, eliminar, etc.

* ### view
  <p>Permite visualizar en pantalla el contenido de un archivo de texto plano.</p>

      view archivo.txt

* ### open
  <p>Abre o ejecuta un archivo.</p>

      open program.exe
    
* ### rename
  <p>Permite renombrar un archivo.</p>

      rename archivo.txt archivo_renombrado.txt

* ### double
  <p>Duplica un archivo en el directorio actual.</p>

      double archivo.txt

* ### copy
  <p>Copia un archivo en el directorio especificado.</p>

      copy archivo.txt /ruta/de/destino

* ### move
  <p>Mueve un archivo en el directorio especificado.</p>

      move archivo.txt /ruta/de/destino

* ### del
  <p>Elimina un archivo.</p>

      del archivo.txt

* ### create
  <p>Crea un nuevo archivo si este no existe.</p>

      create archivo.txt

* ### write
  <p>Añade una nueva línea en un archivo de texto plano.</p>

      write archivo.txt "Texto a escribir"

* ### insp
  <p>Muestra las propiedades de un archivo.</p>

      insp archivo.txt
  

## :open_file_folder: Manipulación de directorios</h2>
Con estos comandos vas a poder manipular los directorios, acceder a ellos, inspeccionarlos y eliminarlos

* ### insp -d
  <p>Muestra un recuento de los archivos y carpetas de un directorio.</p>

      insp -d /ruta/del/directorio/

  > Si no se introduce un directorio se inspeccionará el directorio actual

* ### create -d
  <p>Crea nueva carpeta en el direvtorio actual..</p>

      create -d "Nombre Carpeta"

  > Si no se introduce un nombre se predefinirá "Nueva Carpeta"

* ### del
  <p>Elimina un directorio.</p>

      del /ruta/del/directorio

* ### cd
  <p>Accede a un directorio.</p>

      cd /ruta/del/directorio

* ### back
  <p>Regresa un nivel en el directorio.</p>

      back

* ### home
  <p>Accede al directorio raíz del usuario.</p>

      home


## :memo: Utilidades</h2>
Comandos para funciones generales.

* ### list
  <p>Lista archivos y carpetas en el directorio actual</p>

      list

  #### Flags:

  * -f Para listar solo archivos

        list -f

  * -d Para listar solo directorios

        list -d

  * --< ext > Para listar solo archivos con una extensión específica

        list --html
      

* ### clear
  <p>Limpia la consola.</p>

      clear

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

  * -u Para listar comandos de utilidades

        help -u
