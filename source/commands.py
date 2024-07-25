"""Modulo que contiene todas las funciones del lenguaje"""

# Librerías a utilizar
import os
import shutil
from pathlib import Path
from tabulate import tabulate
from colorama import init, Style, Fore
from lark import Transformer, Token, Tree
from functools import wraps

# Configuración de colorama
init(autoreset=True)

# Variables
current_path = Path.cwd()
home_path = Path.home()

# Funciones internas
def error(msg: str):
    """Envía un mensaje de error.

    Arguments:
        msg {str} -- Error que ocurrió.
    """
    print(f"{Fore.RED}{Style.BRIGHT}Error:", f"{Fore.WHITE}{Style.BRIGHT}{msg}")


def warn(msg: str):
    """Envía un mensaje de advertencia.

    Arguments:
        msg {str} -- Advertencia que se debe mostrar.
    """
    print(f"{Fore.YELLOW}{Style.BRIGHT}{msg}")


def clear():
    """Limpia la consola"""
    os.system("cls" if os.name == "nt" else "clear")


class Commands(Transformer):
    """Clase que contiene todas las funciones del lenguaje"""

    """def _strip_quotes(self, arg):
        Elimina las comillas dobles de un token.

        Arguments:
            arg {str} -- Token

        Returns:
            str -- Token sin las comillas dobles.
        

        if isinstance(arg, str) and arg.startswith('"') and arg.endswith('"'):
            return arg[1:-1]
        return arg"""

    @staticmethod
    def _convert_arg(arg):
        if isinstance(arg, Token):
            return arg.value
        elif isinstance(arg, Tree):
            # Si es un Tree, convertimos recursivamente sus hijos
            return ' '.join(Commands._convert_arg(child) for child in arg.children)
        return str(arg)


    @staticmethod
    def convert_args(func):
        @wraps(func)
        def wrapper(self, args):
            converted_args = [Commands._convert_arg(arg) for arg in args]
            return func(self, converted_args)
        return wrapper


    def back(self, args):
        try:
            global current_path
            os.chdir("..")
            current_path = Path.cwd()
        
        except Exception as e:
            error(e)


    @convert_args
    def cd(self, args):
        try:

            global current_path

            path = current_path / dir

            if path.is_dir():
                os.chdir(path)
                current_path = Path.cwd()
            
            else:
                warn("Especifica un directorio valido.")
            
        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)

        
    def clear(self, args):
        """Limpia la consola"""
        os.system("cls" if os.name == "nt" else "clear")


    def copy_file(self, args):
        """Copia un archivo o directorio"""
        try:
            shutil.copy(file, destination)
        except FileNotFoundError:
            error(f"El archivo '{file}' no se encuentra.")
        except PermissionError:
            error(f"No tienes permisos para copiar el archivo '{file}'.")
        except Exception as e:
            error(e)


    def exec(self, file):
        """Ejecuta un script desde un archivo

        Arguments:
            file {file} -- El archivo que contiene el script
        """
        
        with open(file, "r") as file:
            from parser import command_executor
            
            for line in file.readlines():
                command_executor(line)


    def exit(self, args):
        """Sale del interprete"""
        clear()
        exit()
    
    def view(file):   
        """Muestra en consola el contenido de un archivo de texto plano

        Arguments:
            file {file} -- Archivo
        """
        try:
            with open(file, 'r') as file:
                print(file.read())

        except FileNotFoundError:
            error(f"El archivo '{file}' no se encuentra.")
        except PermissionError:
            error(f"No tienes permisos para leer el archivo '{file}'.")
        except Exception as e:
            error(e)


   
