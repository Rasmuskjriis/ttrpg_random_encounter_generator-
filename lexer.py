import ply.lex as lex

tokens = (
    "INT",
    "DIE",
    "STRING",
    "VLINE",
    "COLON",
    "COMMA",
    "EOF"
)

t_VLINE = r"\|"
t_COLON = r":"
t_COMMA = r","

def t_STRING(t):
    r"\w+"
    t.value = t.value
    return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_DIE(t):
    r"d\d+"
    t.value = int(t.value[1:])
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

with open("default_table", "r") as f:
    data = f.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)