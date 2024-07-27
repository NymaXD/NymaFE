"""Parser del lenguaje"""

from lark import Lark

grammar = r"""

start: command

command: back | cd | clear | copy | create | create_dir | delete | double | exec | exit | help | home | insp | ls | move | open_f | rename | view | write

back: "back"
cd: "cd" (dir | QUOTED_SOURCE)
clear: "clear"
copy: "copy" source destination
create: "create" filename
create_dir: "create -d" (dir | QUOTED_SOURCE)
delete: "del" source
double: "double" source
exec: "exec" filename
exit: "exit"
help: "help" FLAG?
home: "home"
insp: "insp" (dir | QUOTED_SOURCE)?
ls: ("list" | "ls") FLAG?
move: "move" source destination
open_f: "open" filename
rename: "rename" source source
view: "view" filename
write: "write" filename QUOTED_SOURCE


source: (file | dir | QUOTED_SOURCE)
destination: dir | QUOTED_SOURCE
filename: (file | QUOTED_SOURCE)

dir: /[a-zA-Z0-9\/\\:_-]+/
file: /[a-zA-Z0-9._-]+/
QUOTED_SOURCE: "\"" (/[^"]+/) "\""

FLAG: "-d" | "-u" | "-f" | "help" | "list"

%import common.WS
%ignore WS

"""

parser = Lark(grammar, start='start', parser='earley')

def command_executor(input_text):

    if not input_text == "" and not input_text.isspace():

        from commands import Commands
        tree = parser.parse(input_text)
        Commands().transform(tree) 