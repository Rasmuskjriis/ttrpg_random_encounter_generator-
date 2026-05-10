import ply.lex as lex

from typedef import Dice

tokens = (
    "NUMBER",
    "RANGE",
    "DICE",
    "SEPARATOR",
    "COMMA",
    "LABEL",

)

t_SEPARATOR = r"\||:"
t_COMMA = r","

def t_RANGE(t):
    r"\d+-\d+"
    begin, _, end = t.value.partition("-")
    t.value = (int(begin), int(end))
    return t

def t_DICE(t):
    r"\d*d\d+"
    amount, _, sides = t.value.partition("d")
    amount = "1" if amount == "" else amount
    t.value = Dice(int(amount), int(sides))
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_LABEL(t):
    r"[a-zA-Z0-9_][a-zA-Z0-9_ \t]*"
    t.value = t.value
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    # Test of lexer
    with open("default_table", "r") as f:
        data = f.read()

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break
        print(tok)