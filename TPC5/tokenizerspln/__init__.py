#! /usr/bin/env python3
"""
Tokenizer for Harry Potter and the Philosopher's Stone
"""
__version__ = "0.0.3"
import re
import sys


def load_abrev():
    file = open('abrev.txt', 'r')
    txt = file.read()
    ln_list = txt.split('\n')
    dic_abrev = {}
    temp_lang = ""
    for line in ln_list:
        if (line[:1] == '#'):
            temp_lang = line[1:]
            dic_abrev[temp_lang] = []
        else:
            dic_abrev[temp_lang].append(line)
    return dic_abrev


def savePoems(match):
    arr_poems.append(match.group(1))


arr_poems = []
abrev_dic = load_abrev()
used_list = abrev_dic['pt']

if (len(sys.argv) > 1):
    used_list = abrev_dic[sys.argv[1]]


text = ""
with open('Harry_Potter_e_A_Pedra_Filosofal.txt', 'r') as file:
    text = file.read()




# 1. Marcar capítulos
regex_cap = r"— (CAP[IÍ]TULO|CHAPTER \w+) —$"
text = re.sub(regex_cap, r"# \1", text)


# 2. Separar parágrafos de linhas pequenas
regex_par = r'([.!?;])\n(([^.!?;]|[\u00C0-\u017F]))'
text = re.sub(regex_par, r'\1\n/PAR/ \2', text)

# 3. Juntar linhas da mesma frase
regex_ssl = r'([^.!?])\n+([^.!?])'
text = re.sub(regex_ssl, r'\1 \2', text)

# 4. Uma frase por linha

regex_sen = r'([^.!?][.!?])(\s|[^.])'
text = re.sub(regex_sen, r'\1\2\n', text)


for abrev in used_list:
    regex_abrv = rf'({abrev})\.(\s*)\n'
    text = re.sub(regex_abrv, r'\1.\2', text)


regex_poema = r"<poema>(.*?)</poema>"
text = re.sub(regex_poema, savePoems, text, flags=re.S)

print(text)
