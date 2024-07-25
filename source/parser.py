"""Parser del lenguaje"""

from lark import Lark

grammar = r"""
    start: command

    command: back | cd | exit

    back: "back"

    cd: "cd" dir

    exit: "exit"

    dir: unquoted_dir | quoted_dir
    
        unquoted_dir: ("/" | "\\")? (WORD | ".")+ ("/" | "\\")?
        quoted_dir: "\"" (/[^"]+/) "\""

    WORD: /[a-zA-Z0-9]+/
    SPACE: " "


    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='start', parser='lalr')

def command_executor(input_text):
    from commands import Commands
    tree = parser.parse(input_text)
    Commands().transform(tree) 