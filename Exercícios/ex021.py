# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
from urllib import request

try:
    site = urllib.request.urlopen("https://pudim.com.br/")
    print("O site está acessível no momento!")
except:
    print("O site não está acessível no momento!")