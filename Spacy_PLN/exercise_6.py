pont_list = ["...", ".", "?", "!"]

x = input("Ficheiro de Texto: ")
#(Obra/Camilo-A_Brasileira_de_Prazins.txt)

y = open(x).read()

pont = 0 

char = 0

for z in y:
	if z in pont_list:
		pont = pont + 1
	elif z not in pont_list:
		char = char + 1

print(f"Comprimento médio das frases do livro são: {round(char / pont)} caracteres.")
