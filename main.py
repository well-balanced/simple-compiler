from lexer import Lexer
from ast_node import Parser

code = "xyz = 3 + 5"

lexer = Lexer(code)
lexer.tokenize()

parser = Parser(lexer.tokens)
ast = parser.parse()

print(ast)
