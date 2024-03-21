import ply
import ply.lex

tokens = (
    'IDENTIFIER',
    'INTEGER_LITERAL',
    'FLOAT_LITERAL',
)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Token ilegal encontrado: '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'
t_IDENTIFIER = r'\b[_][0-9a-zA-Z]|[a-zA-Z]+[_0-9a-zA-Z]*\b'
t_INTEGER_LITERAL = r'/\b0*([1-3][0-9]{1,9}|41[0-9]{8}|428[0-9]{7}|4293[0-9]{6}|42948[0-9]{5}|429495[0-9]{4}|4294966[0-9]{3}|42949671[0-9]{2}|429496728[0-9]|429496729[0-5])\b/gm'
t_FLOAT_LITERAL = r'[0-9]+\.[0-9]+'

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
