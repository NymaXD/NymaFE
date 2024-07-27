"""Este modulo contiene toda la ayuda del lenguaje."""

from tabulate import tabulate
from colorama import init, Style, Fore

# Configuración de colorama
init(autoreset=True)

def help_all():
    title = f"\n{Fore.CYAN}{Style.BRIGHT}\nMostrando todos los comandos\n"
    foot = f"\n{Fore.CYAN}{Style.BRIGHT}\nSi necesitas mas informacion visita https://github.com/NymaXD/NymaFE"

    headers = ["Comando", "Funcion"]

    commands = [
        ["back", "Regresar un nivel en la jerarquía de directorios."],
        ["cd", "Acceder a un directorio."],
        ["clear", "Limpia la consola."],
        ["copy", "Copia un archivo o directorio en el directorio especificado."],
        ["create", "Crea un nuevo archivo."],
        ["create -d", "Crea una nueva carpeta."],
        ["del", "Elimina un archivo o directorio."],
        ["double", "Duplica un archivo o un directorio en el directorio actual."],
        ["exec", "Ejecuta un script de NymaFE."],
        ["exit", "Sale del interprete."],
        ["help", "Muestra los comandos disponibles."],
        ["help (comando)", "Muestra la ayuda de un comando."],
        ["home", "Accede al directorio raíz del usuario."],
        ["info", "Imprime un mensaje en consola."],
        ["insp", "Inspecciona el contenido de un directorio."],
        ["ls / list", "Lista archivos y carpetas en el directorio actual."],
        ["move", "Mueve un archivo en el directorio especificado."],
        ["open", "Abre o ejecuta un archivo."],
        ["rename", "Renombra un archivo."],
        ["view", "Visualiza en pantalla el contenido de un archivo de texto plano."],
        ["write", "Añade una nueva línea en un archivo de texto plano."]
    ]

    table = tabulate(commands, headers, tablefmt="grid")
    print(title, table, foot)


def help_files():
    title = f"\n{Fore.CYAN}{Style.BRIGHT}Mostrando comandos de manipulación de archivos\n"

    headers = ["Comando", "Funcion"]

    commands = [
        ["copy", "Copia un archivo en el directorio especificado."],
        ["create", "Crea un nuevo archivo."],
        ["del", "Elimina un archivo."],
        ["double", "Duplica un archivo en el directorio actual."],
        ["move", "Mueve un archivo en el directorio especificado."],
        ["open", "Abre o ejecuta un archivo."],
        ["rename", "Renombra un archivo."],
        ["view", "Visualiza en pantalla el contenido de un archivo de texto plano."],
        ["write", "Añade una nueva línea en un archivo de texto plano."]
    ]

    table = tabulate(commands, headers, tablefmt="grid")
    print(title, table)


def help_dirs():
    title = f"\n{Fore.CYAN}{Style.BRIGHT}Mostrando comandos de manipulación de directorios\n"

    headers = ["Comando", "Funcion"]

    commands = [
        ["back", "Regresar un nivel en la jerarquía de directorios."],
        ["cd", "Acceder a un directorio."],
        ["copy", "Copia una carpeta en el directorio especificado."],
        ["create -d", "Crea una nueva carpeta."],
        ["del", "Elimina un directorio."],
        ["double", "Duplica un directorio en el directorio actual."],
        ["home", "Accede al directorio raíz del usuario."],
        ["insp", "Inspecciona el contenido de un directorio."],
        ["move", "Mueve una carpeta en el directorio especificado."],
        ["rename", "Renombra un directorio."]
    ]

    table = tabulate(commands, headers, tablefmt="grid")
    print(title, table)

def help_utilities():
    title = f"\n{Fore.CYAN}{Style.BRIGHT}Mostrando comandos utilitarios\n"

    headers = ["Comando", "Funcion"]

    commands = [
        ["clear", "Limpia la consola."],
        ["exec", "Ejecuta un script de NymaFE."],
        ["exit", "Sale del interprete."],
        ["help", "Muestra los comandos disponibles."],
        ["help (comando)", "Muestra la ayuda de un comando."],
        ["info", "Imprime un mensaje en consola."],
        ["ls / list", "Lista archivos y carpetas en el directorio actual."],
    ]

    table = tabulate(commands, headers, tablefmt="grid")
    print(title, table)


def help_help():

    title = f"\n{Fore.CYAN}{Style.BRIGHT}\nComando 'help'\n"
    text = """
    help           >> Mostrar toda la ayuda
    help -f        >> Mostrar comandos de manipulación de archivos
    help -d        >> Mostrar comandos de manipulación de directorios
    help -u        >> Mostrar comandos de utilidades
    help (comando) >> Mostrar la ayuda de un comando
    """
    print(title, text)


def help_list():

    title = f"\n{Fore.CYAN}{Style.BRIGHT}\nComando 'list'\n"
    text = """
    list         >> Mostrar archivos y carpetas en el directorio actual
    list -f      >> Mostrar solo archivos en el directorio actual
    list -d      >> Mostrar solo carpetas en el directorio actual
    """
    print(title, text)