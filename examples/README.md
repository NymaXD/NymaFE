# Ejemplos de uso

Estos scripts de NymaFE te dan una idea de como utilizar este lenguaje.

Recuerda que para ejecutar un script debes utilizar el comando 'exec' seguido del nombre del archivo, con o sin comillas ("").

    exec "test1.nfe"
    exec test1.nfe

> Recuerda que la única extensión válida es '.nfe'

## Script 1: 'test1.nfe'

Este script simplemente demuestra las funcionalidades del lenguaje creando y modificando carpetas y archivos.

    home
    create -d "New Folder"
    cd "New Folder"
    create new_file.txt
    ls
    write new_file.txt "Hello world!"
    view new_file.txt
    del new_file.txt
    home

1. Accede al directorio raíz del usuario
     > "C:\Users\Usuario" en Windows y /home/usuario/ en Linux

2. Crea una nueva carpeta "New Folder"
3. Accede a dicha carpeta
4. Crea un nuevo archivo "new_file.txt"
5. Lista todo lo que haya en el directorio "New Folder"
6. Escribe "Hello world!" en "new_file.txt"
7. Visualiza el contenido del archivo
8. Borra el archivo "new_file.txt"
9. Regresa al directorio raíz


## Script 2: Limpiar cache multimedia de WhatsApp Desktop

Si eres usuario de Windows, ¿te ha pasado alguna vez que la aplicación WhatsApp ocupa demasiado espacio en el disco duro? Esto sucede porque WhatsApp almacena automáticamente todos los archivos multimedia en el disco duro. Con este script, podrás eliminar todos estos archivos y así liberar espacio de tu disco duro en solo 3 líneas de código.

    home
    cd "AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\shared"
    del transfers
    info "Se ha limpiado la cache multimedia de WhatsApp Desktop."
    home

> Haciendo énfasis en que, las 3 primeras lineas son las que eliminan la multimedia.
