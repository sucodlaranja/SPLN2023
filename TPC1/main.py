import re

texto = open('medicina.xml', 'r').read()


def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'___', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)

    return texto


def marcaE(texto):
    texto = re.sub(r'<text.* font="19"><b>\s*(\d+.*)</b></text>',
                   r'###C \1', texto)
    texto = re.sub(r'<text.* font="19"><b>\s*(\S.+)</b></text>',
                   r'###R \1', texto)

    return texto


def marcaLinguas(texto):
    texto = re.sub(r'<text.* font="\d+">(\s*pt\s*)</text>', r'###L pt', texto)
    texto = re.sub(r'<text.* font="\d+">(\s*en\s*)</text>', r'###L en', texto)
    texto = re.sub(r'<text.* font="\d+">(\s*es\s*)</text>', r'###L es', texto)
    texto = re.sub(r'<text.* font="\d+"><i>\s*(\S.*)</i></text>',
                   r'###P \1', texto)

    return texto


def marcaVid(texto):
    texto = re.sub(r'<text.* font="\d+">(\s*Vid.-.*)</text>',
                   r'###V \1', texto)
    return texto


texto = remove_header_footer(texto)
texto = marcaE(texto)
texto = marcaLinguas(texto)
texto = marcaVid(texto)
texto = re.sub(r'<.*>', r'', texto)


def makeDict(texto):
    dicionario = {}
    activeLang = ''
    activeWord = ''

    fileJson = open('medicina.json', 'w')
    for line in texto.split('\n'):

        if line.startswith('###C'):
            activeLang = ''
            word = re.sub(
                r'###C\s*\d+(.*)\s*[f|m]', r'\1', line).replace(" ", "")
            activeWord = word

            dicionario[word] = {}
        elif line.startswith('###R'):
            activeLang = ''
            word = re.sub(r'###R\s*(.*)', r'\1', line).replace(" ", "")
            activeWord = word
            dicionario[activeWord] = {}
        elif line.startswith('###L'):
            activeLang = re.sub(r'###L\s*(.*)', r'\1', line)
            if (activeWord):
                dicionario[activeWord][activeLang] = []
            pass
        elif line.startswith('###P'):
            if (activeLang != '' and activeWord != ''):
                dicionario[activeWord][activeLang].append(line[5:].strip())
        elif line.startswith('###V'):
            if (activeWord):
                dicionario[activeWord]['Vid'] = line.split(
                    '-')[1].replace(' ', '')
    fileJson.write(str(dicionario))


makeDict(texto)
