import spacy

nlp = spacy.load('pt_core_news_md')

x = input("Ficheiro de Texto: ")
#(Obra/Camilo-A_Brasileira_de_Prazins.txt)

y = nlp(open(x).read())

c = 0
for z in y:
	if z.pos_ == "VERB":
		print(f'"{z}" do verbo: "{z.lemma_}"')
		c = c + 1

print("Número total de verbos:", c)

