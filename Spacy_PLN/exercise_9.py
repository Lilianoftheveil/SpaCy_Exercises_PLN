import spacy
from collections import Counter 

nlp = spacy.load('pt_core_news_md')

x = input("Ficheiro de Texto: ")

y = nlp(open(x).read())

per_list = []

loc_list = []

for z in y.ents:
	if z.label_ == "PER":
		per_list.append(z.text)
	elif z.label_ == "LOC":
		loc_list.append(z.text)

print(f"Personagens que mais aparecem no livro, e suas ocorrências: {Counter(per_list).most_common(5)}")
print(f"Lugares que mais aparecem no livro, e suas ocorrências: {Counter(loc_list).most_common(5)}")
