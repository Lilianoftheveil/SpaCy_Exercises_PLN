import spacy
from collections import Counter 

nlp = spacy.load('pt_core_news_md')

x = input("Ficheiro de Texto: ")
#ex.: Obra/Camilo-A_Brasileira_de_Prazins.txt

y = nlp(open(x).read())

entities_list = []

for z in y.ents:
	if z.label_ == "PER" or z.label_ == "LOC" or z.label_ == "MISC" or z.label_ == "ORG":
		entities_list.append(z.text)

print(Counter(entities_list).most_common())
