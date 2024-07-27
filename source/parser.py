"""Parser del lenguaje"""

from lark import Lark

grammar = r"""

start: command

command: back | cd | clear | copy | create | create_dir | delete | double | exec | exit | help | home | insp | ls | move | open_f | rename | view | write

back: "back"
cd: "cd" dir
clear: "clear"
copy: "copy" source destination
create: "create" file
create_dir: "create -d" dir
delete: "del" source
double: "double" source
exec: "exec" file
exit: "exit"
help: "help" FLAG?
home: "home"
insp: "insp" dir?
ls: ("list" | "ls") FLAG?
move: "move" source destination
open_f: "open" file
rename: "rename" source source
view: "view" file
write: "write" file text


source: file | dir
destination: dir
text: "\"" (/[^"]+/) "\""

dir: quoted_dir | unquoted_dir

    quoted_dir: "\"" (/[^".]+/) "\""
    unquoted_dir: /[a-zA-Z0-9\/_-]+/

file: quoted_file | unquoted_file

    quoted_file: "\"" (/[^"\/]+/) "\""
    unquoted_file: /[a-zA-Z0-9\/_.-]+/


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