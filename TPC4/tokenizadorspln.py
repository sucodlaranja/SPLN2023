#!/usr/bin/env python3

import sys
import re
import fileinput


text = ""
for line in fileinput.input():
    print(line)

# 1. Marcar capítulos
# 2. Separar parágrafos de linhas pequenas
# 3. Juntar linhas da mesma frase 
# 4. Uma frase por linha


regex_cap = r"— (CAP[IÍ]TULO \w+) —$"
text = re.sub(regex_cap, r"# \1", text)

regex_nl = r"([a-z0-9,;-])\n\n([a-z0-9])"
text = re.sub(regex_nl, r"\1\n\2", text)


list_poemas = []


def guarda_poema(poema):
    list_poemas.append(poema)
    print(list_poemas)
    return f">>{len(list_poemas)}<<"


regex_poema = r"<poema>.*?</poema>"
text = re.sub(regex_poema, guarda_poema, text, flags=re.S)

regex_pont = r"(\w)([.,?!;\-])+"
text = re.sub(regex_pont, r"\1 \2", text)
print(text)
