import ply.lex as lex


tokens = ('ID', 'ID_LING', 'LINHA_B', 'DIVISOR',
          'GENERO', 'CATEGORIA')

literals = [':', '[', ']', '\n', '-', '+']


def t_ID_LING(t):
    r'es|en|pt|la|ga'
    return t


def t_LINHA_B(t):
    r'\n+'
    return t


def t_DIVISOR(t):
    r'---'
    return t


def t_GENERO(t):
    r'género'
    return t


def t_CATEGORIA(t):
    r'categoria'
    return t


def t_ID(t):
    r'[^#:+\n\[\],]+'
    return t

t_ignore = " \t"

def t_error(t):
    print(f"ERROR: Illegal char '{t.value[0]}' at position IDK")
    t.lexer.skip(1)


lexer = lex.lex()
