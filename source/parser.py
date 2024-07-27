"""Parser del lenguaje"""

from lark import Lark
from lark.exceptions import UnexpectedToken, UnexpectedCharacters, UnexpectedEOF

def load_grammar(grammar):
    """Cargar la gramatica desde grammar.lark"""

    with open(grammar, 'r') as file:
        return file.read()


grammar = load_grammar("grammar.lark")

parser = Lark(grammar, start='start', parser='earley')


def command_executor(input_text):

    try: 
        if not input_text == "" and not input_text.isspace():

            from commands import Commands
            tree = parser.parse(input_text)
            Commands().transform(tree) 
    
    except UnexpectedToken:
        raise Exception("Error de sintaxis. Escribe 'help' para más informacion.")

    except UnexpectedCharacters:
        raise Exception("Error de sintaxis. Escribe 'help' para más informacion.")

    except UnexpectedEOF:
        raise Exception("Error de sintaxis. Escribe 'help' para más informacion.")