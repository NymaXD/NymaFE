"""Interfaz principal de la línea de comandos"""

from parser import command_executor
from commands import error, warn, clear
from lark.exceptions import UnexpectedToken, UnexpectedCharacters

def main():
    """Main interface"""

    clear()

    while True:
        
        try:
            from commands import current_path
            command = input(f"\n{current_path} # ")
            command_executor(command)

        except KeyboardInterrupt:
            warn("Ctrl + C")

        except UnexpectedToken as e:
            error("Comando desconocido. Escribe 'help' para mas informacion.")
            print(e)

        except UnexpectedCharacters as e:
            error("Error de sintaxis.")
            print(e)


if __name__ == "__main__":

    main()