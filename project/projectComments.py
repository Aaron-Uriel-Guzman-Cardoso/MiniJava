import ply.lex as lex

tokens = (
	'COMMENT_SL',
	'COMMENT_ML'
)

t_ignore = " \t"

def t_COMMENT_SL(t):
	r'[a-z]+'
	
def t_COMMENT_ML(t):
	r'[A-Z]+'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	t.lexer.skip(1)
	
lexer = lex.lex()

f = open("file.txt", "r")
data = f.read()
lexer.input(data)
#print(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)