import ply.yacc as yacc
import sys
from lex import tokens, literals
"""
Dic -> E*
E ->  Categoria LINHA_B Linguas* LINHA_B Genero LINHA_B DIVISOR
Categoria -> CATEGORIA ':' Items
Items -> PA Id+ ',' Items | Item PF
Genero -> GENERO ':' PA ID+ PF 
Linguas -> ID_LING ':' PA ID+ PF LINHA_B
"""


def p_1(p):
    "Dic : E"
    return p


def p_2(p):
    "E :  Categoria LINHA_B Linguas LINHA_B Genero LINHA_B DIVISOR E "
    return p


def p_2_1(p):
    "E :  Categoria LINHA_B Linguas LINHA_B Genero LINHA_B DIVISOR "
    return p


def p_3(p):
    "Categoria : CATEGORIA ':' Items"
    return p


def p_4(p):
    "Items : PA Item PF"
    return p


def p_4_1(p):
    "Item :  ID "


def p_4_2(p):
    "Item :  ID ',' Item "
    return p


def p_5(p):
    "Genero : GENERO ':' PA ID PF "
    return p


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


def main():
    f = open("medicina.txt", "r")
    parser.parse(f.read())
    f.close()
    if (parser.sucess):
        print("Sucesso")
    else:
        print("Falha")


main()
