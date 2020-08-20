#!/home/pdfexe/anaconda3/envs/spider/bin/python

import urllib.request as request
import sys
from bs4 import BeautifulSoup

html = request.urlopen(f'https://www.merriam-webster.com/dictionary/{sys.argv[1]}').read()

soup = BeautifulSoup(html, 'html.parser')
rough_box = soup.find_all('div', {'id': 'dictionary-entry-1'})

definitions = rough_box[0].find_all('span', {'class': 'dtText'})

for definition in definitions:
    print(definition.text)


print('-------------------------------------------------')
