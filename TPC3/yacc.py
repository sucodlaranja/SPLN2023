import ply.yacc as yacc
import sys
from lex import tokens, literals
"""
Dic -> E*
E ->  Categoria LINHA_B Linguas* Genero LINHA_B DIVISOR
Categoria -> CATEGORIA ':' Items
Items -> '[' Id ',' Items | Item ']'
Genero -> GENERO ':' '[' ID+ ']' 
Linguas -> ID_LING ':' '[' ID+ ']' LINHA_B
"""


def p_1(p):
    "Dic : E"
    return p


def p_2(p):
    "E :  Categoria LINHA_B Linguas Genero LINHA_B DIVISOR LINHA_B E "

    return p


def p_2_1(p):
    "E :  Categoria LINHA_B Linguas LINHA_B Genero LINHA_B DIVISOR "
    return p


def p_3(p):
    "Categoria : CATEGORIA ':' Items"
    return p


def p_4(p):
    "Items : '[' Item ']'"
    p[0] = p[2]


def p_4_1(p):
    "Item :  ID"
    p[0] = p[1]


def p_4_2(p):
    "Item :  ID ',' Item "
    p[0] = p[1] + p[3]


def p_5(p):
    "Genero : GENERO ':'  ID "
    p[0] = p[3]


def p_6(p):
    "Linguas : ID_LING ':'  ID  LINHA_B Linguas "
    return p


def p_6_1(p):
    "Linguas : ID_LING ':'  ID  LINHA_B "
    return p


def p_error(p):
    print('Syntax error: ', p)
    parser.success = False


parser = yacc.yacc()
parser.sucess = True

parser.html = """
<h1>Dictionary<br /></h1>
<ul>"""


def main():
    f = open("medicina.txt", "r")
    program = f.read()
    parser.parse(program)
    f.close()
    if parser.sucess:
        print("Sucesso")
        parser.html += "</ul>"
        open("medicina.html", "w").write(parser.html)

    else:
        print("Falha")


main()
