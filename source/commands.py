"""Modulo que contiene todas las funciones del lenguaje"""

# Modulos y bibliotecas a utilizar
import os
import shutil
import time
import stat
import logging
from datetime import datetime
from pathlib import Path
from tabulate import tabulate
from colorama import init, Style, Fore
from lark import Transformer, Token, Tree
from functools import wraps

# Configuración de colorama
init(autoreset=True)

# Variables globales
current_path = Path.cwd()
home_path = Path.home()

# Funciones internas
def create_log():
    """Crea un archivo de logs cuyo nombre es la fecha actual."""
    
    if os.name == "nt":
        cache_path = home_path / "AppData/Local/NymaFE"
    else:
        cache_path = home_path / ".cache/NymaFE"

    if not cache_path.exists():
        cache_path.mkdir()

    date = datetime.now().strftime("%Y_%m_%d")
    log_file = cache_path / f"log_{date}.log"

    if not log_file.exists():
        log_file.touch()

    return log_file


# Configuracion de logging
log_file = create_log()

logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%d/%m/%Y")


def error(msg: str):
    """Envía un mensaje de error.

    Arguments:
        msg {str} -- Error que ocurrió.
    """
    print(f"\n{Fore.RED}{Style.BRIGHT}Error:", f"{Fore.WHITE}{Style.BRIGHT}{msg}")
    logging.error(msg)


def warn(msg: str):
    """Envía un mensaje de advertencia.

    Arguments:
        msg {str} -- Advertencia que se debe mostrar.
    """
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}{msg}")
    logging.warning(msg)


def info(msg: str):
    """Envía un mensaje informativo.

    Arguments:
        msg {str} -- Informacion que se debe mostrar.
    """
    print(f"\n{Fore.LIGHTGREEN_EX}{msg}")
    logging.info(msg)


def clear():
    """Limpia la consola"""
    os.system("cls" if os.name == "nt" else "clear")


class Commands(Transformer):
    """Clase que contiene todas las funciones del lenguaje"""

    @staticmethod
    def _convert_arg(arg):
        """Convierte un Tree a string"""

        if isinstance(arg, Token):
            return arg.value

        elif isinstance(arg, Tree):
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
            dir = args[0]
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


    @convert_args
    def copy(self, args):

        source = Path(args[0])
        destination = Path(args[1])

        try:

            if not source.exists():
                raise FileNotFoundError

            if not destination.is_dir():
                raise Exception(f"El directorio de destino '{destination}' no existe.")

            if source.is_file():

                destination = destination / source.name
                shutil.copy2(source, destination)

            elif source.is_dir():

                destination = destination / source.name
                shutil.copytree(source, destination)

        except FileNotFoundError:
            error(f"'{source}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            info(f"Se ha copiado '{source}' en {destination}.")


    @convert_args
    def create(self, args):
        
        try:

            name = Path(args[0])

            if not name.exists():
                name.touch()
                info(f"Se ha creado '{name}'.")
            else:
                warn(f"El archivo '{name}' ya existe.")

        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)


    @convert_args
    def create_dir(self, args):
        name = Path(args[0])

        try:
            if not name.exists():
                name.mkdir()
                info(f"Se ha creado '{name}'.")
            else:
                warn(f"El directorio '{name}' ya existe.")

        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)


    @convert_args
    def delete(self, args):
        source = Path(args[0])

        try:
            if not source.exists():
                raise FileNotFoundError

            if source.is_file():
                source.unlink()

            elif source.is_dir():
                shutil.rmtree(source)

        except FileNotFoundError:
            error(f"'{source}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            info(f"Se ha eliminado {source}.")


    @convert_args
    def double(self, args):

        source = Path(args[0])

        try:

            if not source.exists():
                raise FileNotFoundError

            if source.is_file():

                shutil.copy2(source, source.with_stem(f"{source.stem}_copy"))

            elif source.is_dir():

                shutil.copytree(source, f"{source}_copy")

        except FileNotFoundError:
            error(f"'{source}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            info(f"Se ha duplicado '{source}'.")


    @convert_args
    def exec(self, args):

        logging.info(f"Ejecutando script: {args[0]}")
        
        file = Path(args[0])

        try:
            start = time.time()

            if not file.suffix == ".nfe":
                raise Exception(f"El archivo '{file}' no es un script valido.")

            with open(file, "r") as file:
                from parser import command_executor
                
                for line in file.readlines():

                    try:
                        command_executor(line)

                    except Exception as e:
                        raise Exception(e)

            end = time.time()
            exec_time = end - start

        except FileNotFoundError:
            error(f"'{file}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)
            
            end = time.time()
            exec_time = end - start
            print(f"{Fore.RED}Ejecucion Fallida. {exec_time} segundos.")
            logging.error(f"Ejecucion fallida: {e}")

        else:
            info(f"Ejecucion finalizada en {exec_time} segundos.")


    def exit(self, args):
        """Sale del interprete"""
        logging.info("Saliendo del shell.")
        clear()
        exit()


    @convert_args
    def help(self, args):
        import help

        if len(args) > 0:
            flag = args[0]

            match flag:

                case "-d":
                    help.help_dirs()

                case "-f":
                    help.help_files()

                case "-u":
                    help.help_utilities()

                case "help":
                    help.help_help()

                case "list":
                    help.help_list()

        else:
            help.help_all()


    def home(self, args):
        try:
            global current_path
            os.chdir(Path.home())
            current_path = Path.cwd()
        
        except Exception as e:
            error(e)


    @convert_args
    def info(self, args):
        info(args[0])


    @convert_args
    def insp(self, args):

        try:

            if len(args) == 0:
                dir = Path.cwd()

            else:
                dir = Path(args[0])

                if not dir.exists():
                    raise FileNotFoundError

                if not dir.is_dir():
                    raise Exception(f"'{dir}' no es un directorio.")

            folder_count = 0
            file_count = 0

            for src in dir.iterdir():

                if src.is_dir():
                    folder_count += 1
                elif src.is_file():
                    file_count += 1

            file_stats = os.stat(dir)

            title = f"\n{Fore.CYAN}{Style.BRIGHT}\n{dir}\n"
            headers = ["Propiedad", "Valor"]
            table = [
                ["Tamaño", f"{file_stats.st_size}"],
                ["Archivos", file_count],
                ["Carpetas", folder_count]
            ]

            print(tabulate(table, headers, tablefmt="grid"))

        
        except FileNotFoundError:
            error(f"'{dir}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)


    @convert_args
    def ls(self, args):

        headers = ["Nombre", "Tipo", "Tamaño"]
        table = []

        try:

            if len(args) > 0:
                flag = args[0]

                match flag:

                    case "-d":
                        for dir in current_path.iterdir():
                            file_stats = os.stat(dir)

                            if dir.is_dir():
                                type_ = "Carpeta"
                                table.append([dir.name, type_, file_stats.st_size])

                        print(tabulate(table, headers, tablefmt="grid"))

                    case "-f":
                        for dir in current_path.iterdir():
                            file_stats = os.stat(dir)

                            if not dir.is_dir():
                                type_ = f"Archivo {dir.suffix}"
                                table.append([dir.name, type_, file_stats.st_size])

                        print(tabulate(table, headers, tablefmt="grid"))

            else:

                for dir in current_path.iterdir():
                    file_stats = os.stat(dir)

                    if dir.is_dir():
                        type_ = "Carpeta"
                    else:
                        type_ = f"Archivo {dir.suffix}"
                    
                    table.append([dir.name, type_, file_stats.st_size])

                print(tabulate(table, headers, tablefmt="grid"))

        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)


    @convert_args
    def move(self, args):

        source = Path(args[0])
        destination = Path(args[1])

        try:

            if not source.exists():
                raise FileNotFoundError

            if not destination.is_dir():
                raise Exception(f"El directorio de destino '{destination}' no existe.")

            destination = destination / source.name
            shutil.move(source, destination)

        except FileNotFoundError:
            error(f"'{source}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            info(f"Se ha movido '{source}' a {destination}.")


    @convert_args
    def open_f(self, args):
        file = Path(args[0])

        try:
            if not file.exists():
                raise FileNotFoundError
            if not file.is_file():
                raise Exception(f"'{file}' no es un archivo.")

            if os.name == "nt":
                os.system(f"{file}")
            else:
                os.system(f"./{file}")

        except FileNotFoundError:
            error(f"'{file}' no existe.")
        except PermissionError:
            error(f"Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            logging.info(f"Abriendo el archivo '{file}'.")


    @convert_args
    def rename(self, args):
        file = args[0]
        new_name = args[1]

        try:
            os.rename(file, new_name)

        except FileNotFoundError:
            error(f"El archivo '{file}' no existe.")
        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            info(f"Se ha renombrado '{file}' como '{new_name}'.")


    @convert_args
    def view(self, args):
        file = Path(args[0])
        
        try:
            with open(file, 'r') as file:
                print("\n" + file.read() + "\n")

        except FileNotFoundError:
            error(f"El archivo '{file}' no existe.")
        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)


    @convert_args
    def write(self, args):
        file = Path(args[0])
        text = args[1]

        try:
            with open(file, "a+") as file:
                file.write(f"{text}\n")

        except FileNotFoundError:
            error(f"El archivo '{file}' no existe.")
        except PermissionError:
            error("Permisos insuficientes.")
        except Exception as e:
            error(e)

        else:
            logging.info(f"Se ha escrito en el archivo '{file}'.")
