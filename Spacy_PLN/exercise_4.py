import spacy
from collections import Counter 

apt = spacy.load('pt_core_news_md')

x = input("Ficheiro de Texto: ")
#(Obra/Camilo-A_Brasileira_de_Prazins.txt)

y = apt(open(x).read())

verbs = []
for z in y:
	if z.pos_ == 'VERB':
		verbs.append(z.text)

print(Counter(verbs).most_common())
