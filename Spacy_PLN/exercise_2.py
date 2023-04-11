from jjcli import *

#"Obra/Camilo-A_Brasileira_de_Prazins.txt"

cl = clfilter("")

c = 0

for linha in cl.input():
    if c <= 3:
        print(linha)
        c = c + 1
