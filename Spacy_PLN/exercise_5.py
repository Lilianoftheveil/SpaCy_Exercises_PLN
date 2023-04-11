import spacy

nlp = spacy.load('pt_core_news_md')

pont_list = ["...", ".", "?", "!"]

x = input("Ficheiro de Texto: ")
#(Obra/Camilo-A_Brasileira_de_Prazins.txt)

y = open(x).read()

c = 0
for z in y:
	if z in pont_list:
		c = c + 1

print(f"Número total de tokens: {len(nlp(y))}") 

print(f"Número total de frases: {c}")
