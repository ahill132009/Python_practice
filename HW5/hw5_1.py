import itertools 
import pymorphy2
import random

morph = pymorphy2.MorphAnalyzer()


ADJF = []
NOUN = []

with open('./rus_shuffled.txt', 'r') as f:
	head = list(itertools.islice(f, 500))
	for wrd in head:
		wrd = wrd.strip('\n')
		p = morph.parse(wrd)[0]
		if p.tag.POS == 'NOUN':
			NOUN.append(p.normal_form)
		elif p.tag.POS == 'ADJF':
			ADJF.append(p.normal_form)
		else:
			continue


def get_pair():
	for adjf, noun in itertools.product(random.sample(ADJF,20), random.sample(NOUN,20)):
		noun_gender = morph.parse(noun)[0].tag.gender
		adjf = morph.parse(adjf)[0].inflect({noun_gender}).word
		yield  f'{adjf} {noun}'


gen = get_pair()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

