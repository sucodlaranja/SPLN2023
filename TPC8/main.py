import sys
import requests
from bs4 import BeautifulSoup as bs


url = sys.argv[1]

conteudo = requests.get(url).text
tree = bs(conteudo, 'lxml')
links = tree.find_all('a')
for a in links:
    print(a['href'])
