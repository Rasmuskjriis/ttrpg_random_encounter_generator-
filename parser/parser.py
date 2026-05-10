import ply.yacc as yacc
from lexer import tokens

from typedef import Table

def p_tables(p):
    """tables : table
              | tables table"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        print(p)
        p[1].append(p[2])
        p[0] = p[1]

def p_table(p):
    """table : DICE SEPARATOR LABEL rows"""
    p[0] = Table(p[1], p[3], p[4])

def p_rows(p):
    """rows : row
            | rows row"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_row(p):
    """row  : NUMBER SEPARATOR entries
            | RANGE SEPARATOR entries"""
    p[0] = (p[1], p[3])

def p_entries(p):
    """entries : entry
               | entries COMMA entry"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_entry(p):
    """entry : LABEL
             | NUMBER LABEL
             | DICE LABEL"""
    if len(p) == 2:
        p[0] = (1, p[1])
    else:
        p[0] = (p[1], p[2])

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    # Test of parser
    with open("default_table", "r") as f:
        data = f.read()

    result = parser.parse(data)
    for table in result:
        print(table)