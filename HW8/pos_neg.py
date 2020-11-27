with open('./negative-words.txt', 'r+', encoding = "ISO-8859-1") as f1:
	s = f1.readlines()
	neg_words = []
	for x in s:
		if ';' not in x and x != '\n':
			neg_words.append(x.split()[0])

with open('./positive-words.txt', 'r+', encoding = "ISO-8859-1") as f2:
	s = f2.readlines()
	pos_words = []
	for x in s:
		if ';' not in x and x != '\n':
			pos_words.append(x.split()[0])
