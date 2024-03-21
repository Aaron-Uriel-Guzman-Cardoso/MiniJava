import ply.lex as lex

tokens = (
    'KEYWORD_CLASS',
    'KEYWORD_PUBLIC',
    'KEYWORD_STATIC',
    'KEYWORD_VOID',
    'KEYWORD_STRING',
    'KEYWORD_RETURN',
    'KEYWORD_EXTENDS',
    'KEYWORD_INT',
    'KEYWORD_BOOLEAN',
    'KEYWORD_FLOAT',
    'KEYWORD_IF',
    'KEYWORD_ELSE',
    'KEYWORD_WHILE',
    'KEYWORD_TRUE',
    'KEYWORD_FALSE',
    'KEYWORD_THIS',
    'KEYWORD_NEW',
    'KEYWORD_BREAK',
    'KEYWORD_CONTINUE',
    'KEYWORD_SWITCH',
    'KEYWORD_CASE',
    'KEYWORD_DEFAULT',
    'KEYWORD_LENGTH',
    'KEYWORD_NULL',
    'KEYWORD_SYSTEMOUTPRINTLN',
    'AGROUP_LBRACKETS',
    'AGROUP_RBRACKETS',
    'AGROUP_LPARENTHESES',
    'AGROUP_RPARENTHESES',
    'AGROUP_LBRACES',
    'AGROUP_RBRACES',
    'OPERATOR_EQUALS',
    'OPERATOR_AND',
    'OPERATOR_OR',
    'OPERATOR_LESSTHAN',
    'OPERATOR_MORETHAN',
    'OPERATOR_LESSEQUAL',
    'OPERATOR_MOREEQUAL',
    'OPERATOR_PLUS',
    'OPERATOR_MINUS',
    'OPERATOR_MULTIPLY',
    'OPERATOR_DIVIDE',
    'OPERATOR_DOT',
    'OPERATOR_UNEQUAL',
    'OPERATOR_COMMA',
    #'IDENTIFIER',
    #'STRING',
    #'POS_INTEGER',
    #'FLOAT',
    'COMMENTS_SL',
    'COMMENTS_ML',
     'WRONGCARID'
)

t_KEYWORD_CLASS = r'class'

t_KEYWORD_PUBLIC = r'public'

t_KEYWORD_STATIC = r'static'

t_KEYWORD_VOID = r'void'

t_KEYWORD_STRING = r'String'

t_KEYWORD_RETURN = r'return'

t_KEYWORD_EXTENDS = r'extends'

t_KEYWORD_INT = r'int'

t_KEYWORD_BOOLEAN = r'boolean'

t_KEYWORD_FLOAT = r'float'

t_KEYWORD_IF = r'if'

t_KEYWORD_ELSE = r'else'

t_KEYWORD_WHILE = r'while'

t_KEYWORD_TRUE = r'true'

t_KEYWORD_FALSE = r'false'

t_KEYWORD_THIS = r'this'

t_KEYWORD_NEW = r'new'

t_KEYWORD_BREAK = r'break'

t_KEYWORD_CONTINUE = r'continue'

t_KEYWORD_SWITCH = r'switch'

t_KEYWORD_CASE = r'case'

t_KEYWORD_DEFAULT = r'default'

t_KEYWORD_LENGTH = r'length'

t_KEYWORD_NULL = r'null'

t_KEYWORD_SYSTEMOUTPRINTLN = r'System.out.println'

t_AGROUP_LBRACKETS = r'\['

t_AGROUP_RBRACKETS = r'\]'

t_AGROUP_LPARENTHESES = r'\('

t_AGROUP_RPARENTHESES = r'\)'

t_AGROUP_LBRACES = r'\{'

t_AGROUP_RBRACES = r'\}'

t_OPERATOR_EQUALS = r'='

t_OPERATOR_AND = r'&'

t_OPERATOR_OR = r'\|'

t_OPERATOR_LESSTHAN = r'<'

t_OPERATOR_MORETHAN = r'>'

t_OPERATOR_LESSEQUAL = r'<='

t_OPERATOR_MOREEQUAL = r'>='

t_OPERATOR_PLUS = r'\+'

t_OPERATOR_MINUS = r'\-'

t_OPERATOR_MULTIPLY = r'\*'

t_OPERATOR_DIVIDE = r'/'

t_OPERATOR_DOT = r'\.'

t_OPERATOR_UNEQUAL = r'!='

t_OPERATOR_COMMA = r','

def t_COMMENTS_SL(t):
	r'\/\/.*'
	
def t_COMMENTS_ML(t):
	r'\/\*[\w*\W*]*\*\/'

def t_WRONGCARID(t):
	r'(\b)?(\w*[^\w |;\n]+\w*)+(\b)?/gm'
	return (t)

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

f = open("ejemplo1.txt", "r")
data = f.read()
lexer.input(data)
#print(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
