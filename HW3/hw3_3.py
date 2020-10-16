from corus import load_corpora
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import csv
import pickle


class UnigramMorphAnalyzer:

	def __init__(self, path_to_corpora):
		self.path_to_corpora = path_to_corpora
		self.records = load_corpora(self.path_to_corpora)
		self.ending_stats = {}
		self.loaded_pickle = None
		self.test_corpora = None

	def __getitem__(self, idx):
		return self.ending_stats[idx]

	@staticmethod
	def ending_of_word(word):
		# Return ending of the word, depending on the length of the word
		if len(word) < 4:
			ending = word[-(len(word)):]
		else:
			ending = word[-4:]
		return ending

	def train(self):
		# Write csv with word-pos pairs
		with open('corpora_words_grams.csv', 'w+', newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			writer.writerow(['Text', 'Part of speech'])
			for rec_part in self.records:
					if rec_part.pars:	
						for x in rec_part.pars[0].sents[0].tokens:
						# Check for [] where [txt] should be
							if x.forms[0].text:
								writer.writerow([x.forms[0].text, x.forms[0].grams[0]])

		df = pd.read_csv('corpora_words_grams.csv', sep='\t')
		X = df.iloc[:, 0]
		y = df.iloc[:, 1]
		X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

		train_corpora = zip(X_train, y_train)
		self.test_corpora = zip(X_test, y_test)

		ending_train = ''
		for word_train, pos_train in train_corpora:
			ending_train = self.ending_of_word(word_train)
			while ending_train:
				# Sometimes [] where should be [text] appear
				if ending_train in self.ending_stats:
					if pos_train in self.ending_stats[ending_train]:
						self.ending_stats[ending_train][pos_train] += 1
					if pos_train not in self.ending_stats[ending_train]:
						self.ending_stats[ending_train][pos_train] = 1
				elif ending_train not in self.ending_stats:
					self.ending_stats[ending_train] = {pos_train:1}
				wrd_letters = list(ending_train)
				wrd_letters.remove(ending_train[0])
				ending_train = ''.join(wrd_letters)
		return self.ending_stats

	def predict(self, token):
		predict_ending = self.ending_of_word(token)
		try:
			self.string = ""
			self.sum_vals = sum([v for v in self.ending_stats[predict_ending].values()])
			for k, v in self.ending_stats[predict_ending].items():
				self.string += f'Present ending is {predict_ending}. ' \
				f'The probability of being {k} is {round(v/self.sum_vals, 3)}\n'
			return self.string
		except KeyError:
			return f'There is no such ending as "{predict_ending}" in the dictionary'
	
	def save(self, pickle_name):
		with open(pickle_name, 'wb') as p:
			pickle.dump(self.ending_stats, p)
		return f'{pickle_name} is successfully written'

	def load(self, pickle_name):
		with open(pickle_name, 'rb') as p:
			self.loaded_pickle = pickle.load(p)
		return f'{pickle_name} is successfully loaded'

	def eval_argmax(self):
		ending = ''
		self.positives = 0
		self.negatives = 0
		for test_word, pos in self.test_corpora:
			if len(test_word) < 4:
				ending = test_word[-(len(test_word)):]
				try:
					max_pos = max(self.ending_stats[ending], key=self.ending_stats[ending].get)
					if pos == max_pos:
						self.positives += 1
					else:
						self.negatives += 1
				except KeyError:
					continue

			else:
				ending = test_word[-4:]	
				try:
					max_pos = max(self.ending_stats[ending], key=self.ending_stats[ending].get)
					if pos == max_pos:
						self.positives += 1
					else:
						self.negatives += 1
				except KeyError:
					continue

		return f'Accuracy of the model is: {round((self.positives/(self.positives + self.negatives) * 100), 2)} %'

	def eval_distrib(self):
		ending = ''
		self.positives = 0
		self.negatives = 0
		for test_word_d, pos_d in self.test_corpora:
			print(test_word_d, pos_d)
			if len(test_word_d) < 4:
				ending = test_word_d[-(len(test_word_d)):]
				try:
					ngood = self.ending_stats[ending][pos_d]
					nbad = sum([v for k,v in self.ending_stats[ending].items()]) - self.ending_stats[ending][pos_d]
					if np.random.hypergeometric(ngood, nbad, 1) == 1:
						self.positives += 1
					else:
						self.negatives += 1
				except KeyError:
					continue

			else:
				ending = test_word_d[-4:]	
				try:
					ngood = self.ending_stats[ending][pos_d]
					nbad = sum([v for k,v in self.ending_stats[ending].items()]) - self.ending_stats[ending][pos_d]
					if np.random.hypergeometric(ngood, nbad, 1) == 1:
						self.positives += 1
					else:
						self.negatives += 1
				except KeyError:
					continue

		return f'Accuracy of the model is: {round((self.positives/(self.positives + self.negatives) * 100), 2)} %'
