import ply
import ply.lex

operators = [ '+', '-', '/', '*', '&', '|', '<', '>',
              '.', '!', ',' ]
grouping = [ '[', ']', '(', ')', '{', '}' ]
misc = [ ';' ]
literals = operators + grouping + misc

reserved = {
    'class': 'CLASS',
    'public': 'PUBLIC',
    'static': 'STATIC',
    'void': 'VOID',
    'String': 'STRING',
    'return': 'RETURN',
    'extends': 'EXTENDS',
    'int': 'INT',
    'boolean': 'BOOLEAN',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'this': 'THIS',
    'new': 'NEW',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'length': 'LENGTH',
    'null': 'NULL',
    'System.out.println': 'PRINTLN'
}
tokens = (['IDENTIFIER', 'INTEGER_LITERAL', 'FLOAT_LITERAL',
           'LESS_EQUAL', 'MORE_EQUAL'] + list(reserved.values()))

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Token ilegal encontrado: '%s'" % t.value[0])
    t.lexer.skip(1)

def t_IDENTIFIER(t):
    r'\b[_][0-9a-zA-Z]|[a-zA-Z]+[_0-9a-zA-Z]*\b'
    return t

# Esta necesita más trabajo para obtener solo el número de importancia.
def t_INTEGER_LITERAL(t):
    r'\b0*([1-3]?[0-9]{1,9}|41[0-9]{8}|428[0-9]{7}|4293[0-9]{6}|42948[0-9]{5}|429495[0-9]{4}|4294966[0-9]{3}|42949671[0-9]{2}|429496728[0-9]|429496729[0-5])\b'
    return t

def t_FLOAT_LITERAL(t):
    r'[0-9]+\.[0-9]+'
    return t

def main():
    input_file = open("inputs/factorial.java", "r")
    lexer = ply.lex.lex()
    lexer.input(input_file.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    main()
