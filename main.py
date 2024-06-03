import sys
import ply.lex as lex
import ply.yacc as yacc

operators = ['+', '-', '/', '*', '&', '|', '<', '>',
             '.', '!', ',', '=']
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
        'LESS_EQUAL', 'MORE_EQUAL', 'COMMENT', 'MULTILINE_COMMENT'] + list(reserved.values()))
t_ignore = ' \t'
t_LESS_EQUAL = r'<='
t_MORE_EQUAL = r'>='

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Error léxico: token ilegal')
    print('\tLínea:', t.lineno)
    print('\tCadena:', t.value[0])
    t.lexer.skip(1)

def t_INVALID_IDENTIFIER(t):
    r'(\b_\b)|(\b[0-9]+[_a-zA-Z].*?\b)'
    print('Error léxico: identificador inválido')
    print('\tLínea:', t.lineno)
    print('\tCadena:', t.value)
    t.lexer.skip(1)


def t_INVALID_INTEGER(t):
    r'\b0*(\d{11,}|429496729[6-9]|4294967[3-9][0-9]{2}|429496[8-9][0-9]{3}|42949[7-9][0-9]{4}|429[5-9][0-9]{6}|4[3-9][0-9]{8}|[5-9][0-9]{9})\b'
    print('Error léxico: entero con valor superior al máximo')
    print('\tLínea:', t.lineno)
    print('\tCadena:', t.value)
    t.lexer.skip(1)

def t_INVALID_FLOAT(t):
    r'(\d+\.(?!\d))|((?<!\d)\.\d+)'
    print('Error léxico: sintaxis ilegal para números flotantes')
    print('\tLínea:', t.lineno)
    print('\tCadena:', t.value)
    t.lexer.skip(1)

def t_IDENTIFIER(t):
    r'(System\.out\.println)|(_+[a-zA-Z0-9]+)|([a-zA-Z][_a-zA-Z0-9]*)'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'\"([^\"\n]|\\.)*\"'
    return t

def t_COMMENT(t):
    r'\/\/.*'
    pass
	
def t_MULTILINE_COMMENT(t):
    r'(?s:/\*.*?\*/)'
    t.lexer.lineno += t.value.count('\n')

def t_INTEGER_LITERAL(t):
    r'\b0*([1-3]?[0-9]{1,9}|41[0-9]{8}|428[0-9]{7}|4293[0-9]{6}|42948[0-9]{5}|429495[0-9]{4}|4294966[0-9]{3}|42949671[0-9]{2}|429496728[0-9]|429496729[0-5])\b'
    t.value = int(t.value)
    return t

def t_FLOAT_LITERAL(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def main():
    if (len(sys.argv) < 2):
        print("Forma de uso:")
        print("\tpython3 main.py [ENTRADA]")
        return
    filename = sys.argv[1]
    inputStr = open(filename, "r").read()
    lexer = lex.lex()
    lexer.input(inputStr)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    parser = yacc.yacc()
    for lineStr in inputStr.split('\n'):
        print('Probando', lineStr)
        parser.parse(inputStr)

if __name__ == "__main__":
    main()
