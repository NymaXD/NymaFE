"""Interfaz principal de la línea de comandos"""

from parser import command_executor
from commands import error, warn, clear
from lark.exceptions import UnexpectedToken, UnexpectedCharacters, UnexpectedEOF

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
            error("Error de sintaxis. Escribe 'help' para más informacion.")

        except UnexpectedCharacters as e:
            error("Error de sintaxis. Escribe 'help' para más informacion.")

        except UnexpectedEOF as e:
            error("Error de sintaxis. Escribe 'help' para más informacion.")
            
        except Exception as e:
            error(e)


if __name__ == "__main__":

    main()