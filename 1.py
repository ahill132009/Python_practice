import time
import os
import string
import csv
from bs4 import BeautifulSoup
import requests
import json
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

t1 = time.time()

punctuation_symbols = list(string.punctuation)
escape_chrctrs = ['\t', '\n']

# Adding some symbols to punctuation symbols list
brckts = ['\u00ab', '\u00bb', '\u2014', '\u201c', '\u201d', '\u2116', '\u2026', '\u2048', '\u2013'] 
for brckt in brckts: 
	punctuation_symbols.append(brckt)
punctuation_symbols.remove('-') # проблема удаления наречий со знаком "-" типа "по-новому"

txt = open('dom.txt','r')
with open('./dom.txt', 'r') as f: # 1
	text = f.read()
	text = text.lower() # 2

	lst1 = [] # 3
	for char in text:
		if char not in punctuation_symbols:
			# пробуем не писать символ '-' если он стоит в середине предложения, т.е. с пробелами по краям
			if char == '-': 
				if text[text.index(char) + 1] != ' ' and text[text.index(char) - 1] != ' ':
					lst1.append(char)
				else:
					lst1.append(' ')
			else:
				lst1.append(char)
		else:
			lst1.append(' ')
	text = ''.join(lst1)	


	frequency_dict = {} # 4
	word_list = text.split(' ')
	for word in word_list:
		word  = ''.join(c for c in word if c not in escape_chrctrs)
		if word not in frequency_dict:
			frequency_dict[word] = 1  
		else:
		 frequency_dict[word] += 1
	frequency_dict.pop('') # удалим подсчет знака ''
	
	# Отсортируем значения из словаря
	word_freq = []
	for key, value in frequency_dict.items():
	    word_freq.append((value, key))
	word_freq.sort(reverse=True)

	# Запишем частотный словарь в csv
	with open('frequency_dict.csv', 'w') as csv_f:
		writer = csv.writer(csv_f)
		for key, value in frequency_dict.items():
			writer.writerow([key, value])

	# Текст, разделенный на отдельные слова
	text_splitted = []
	for word in text.split(' '):
		word  = ''.join(c for c in word if c not in escape_chrctrs)
		text_splitted.append(word)
	text_splitted = list(filter(None, text_splitted))

	# Лемматизированный текст
	text_lemmatized = [] # 5
	for word in text_splitted:
		text_lemmatized.append(morph.parse(word)[0].normal_form)

	# Никак не получалось сделать через модуль re из-за сложности с кодированием кириллического алфавита
	# Леммы с 'oo' 
	text_lemmatized_oo = [] # 6
	for word in text_lemmatized:
		for ltr in range(len(word[:-1])):
			if word[ltr] == 'о' and word[ltr+1] == 'о':
				text_lemmatized_oo.append(word)


	url = 'http://lib.ru/POEZIQ/PESSOA/lirika.txt' # 7
	res = requests.get(url)
	html_page = res.content
	soup = BeautifulSoup(html_page, 'html.parser')
	html_text = soup.find_all(text=True)

	list_of_html_symbols = []
	for line in html_text:
		for smbl in line:
			if smbl not in escape_chrctrs and smbl not in punctuation_symbols:
				list_of_html_symbols.append(smbl)

	word_list_html = str(''.join(list_of_html_symbols)).split(' ')

	#8
	frequency_dict_html = {} 
	for word in word_list_html:
		if word not in frequency_dict_html:
			frequency_dict_html[word] = 1  
		else:
		 	frequency_dict_html[word] += 1
	frequency_dict_html.pop('-') # удалим подсчет знака '-'

	#9
	with open ('./frequency', 'w') as output_f:
		json.dump(frequency_dict_html, output_f)

t2 = time.time()
print(f'Operations took {t2-t1} sec')