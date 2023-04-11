from jjcli import *

x = glob("Obra/*.txt")

pont_list = ["...", ".", "?", "!"]

pont = 0 

char = 0

for y in x:
	z = open(y).read()
	for a in z:
		if a in pont_list:
			pont = pont + 1
		elif a not in pont_list:
			char = char + 1

print(f"Comprimento médio das frases de todos os livros são: {round(char / pont)} caracteres.")
