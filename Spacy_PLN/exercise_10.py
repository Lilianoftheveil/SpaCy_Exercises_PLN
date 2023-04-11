import spacy

from collections import Counter 
from jjcli import *

nlp = spacy.load('pt_core_news_md')

x = glob("Obra/*.txt")

per_list = []

c = 0

for y in x:
	z = nlp(open(y).read())
	c = c + 1
	for a in z.ents:
		if a.label_ == "PER":
			per_list.append(a.text)
	print(f"Livro: {c} \n")
	print(f"Personagens deste livro: {Counter(per_list).most_common()}\n")
	print("-" * 20 + "\n")
	per_list = []