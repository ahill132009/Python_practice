from corus import load_corpora
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import csv
import pickle
import random
import json


class UnigramMorphAnalyzer:

	def __init__(self, path_to_corpora):
		self.path_to_corpora = path_to_corpora
		self.records = load_corpora(self.path_to_corpora)
		self.ending_stats = {}
		self.name_of_csv = 'word_pos.csv'
		self.stopwords = {}

	def __getitem__(self, idx):
		return self.ending_stats[idx]

	@staticmethod
	def count_probability(dict_of_pos):
		dict_with_probs = {}
		sum_vals = sum([v for v in dict_of_pos.values()])
		for k, v in dict_of_pos.items():
			dict_with_probs[k] = round(v/sum_vals*100, 2)
		return dict_with_probs		

	def stopwords_foo(self, path_to_stopwords):
		with open(path_to_stopwords, 'rb') as f:
			self.stopwords = json.load(f)
		print('Stopwords were written')
		return self.stopwords

	def make_csv(self, name_of_csv):
		self.name_of_csv = name_of_csv
		# Write csv with word-pos pairs
		with open(self.name_of_csv, 'w+', newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			writer.writerow(['Text', 'Part of speech'])
			for rec_part in self.records:
					if rec_part.pars:	
						for x in rec_part.pars[0].sents[0].tokens:
						# Check for [] where [txt] should be
							if x.forms[0].text:
								writer.writerow([x.forms[0].text, x.forms[0].grams[0]])
		print(f'CSV file successfully written')

	def split_corpora(self):
		df = pd.read_csv(self.name_of_csv, sep='\t')
		X = df.iloc[:, 0]
		y = df.iloc[:, 1]
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, shuffle=False)
		return self.X_train, self.X_test, self.y_train, self.y_test

	def train(self):
		for word_train, pos_train in zip(self.X_train, self.y_train):
			ending = word_train[-4:] if len(word_train) >= 4 else word_train
			if self.stopwords.get(ending) is not None:
				self.ending_stats[ending] = self.stopwords[ending]
			for _ in range(len(ending)):
				pos_dict = self.ending_stats.get(ending)
				if pos_dict is None:
					self.ending_stats[ending] = {pos_train:1}
				else:
					if pos_train not in pos_dict:
						pos_dict[pos_train] = 1
					else:
						pos_dict[pos_train] += 1
				ending = ending[1:]

	def _argmax(self, argmax_ending_dict):
		return max(argmax_ending_dict, key=argmax_ending_dict.get)

	def _distrib(self, argmax_ending_dict):
		return random.choices(list(argmax_ending_dict.keys()), weights=argmax_ending_dict.values())[0]

	def predict(self, token, method):
		assert method in ['argmax', 'distrib']
		ending = token[-4:] if len(token) >= 4 else token
		for _ in range(len(ending)):
			pred = self.ending_stats.get(ending)
			if pred is None:
				ending = ending[1:]
				continue
			pred = self.count_probability(pred)
			if method == 'argmax':
				return self._argmax(pred)
			else:
				return self._distrib(pred)
	
	def eval(self, method):
		assert method in ['argmax', 'distrib']
		correct, total = 0, 0
		for word, pos_true in zip(self.X_test, self.y_test):
			pred = self.predict(word, method=method)
			if pred == pos_true:
				correct += 1
			total += 1
		return correct / total

	def save(self, pickle_name):
		with open(pickle_name, 'wb') as p:
			pickle.dump(self.ending_stats, p)
		print(f'{pickle_name} is successfully written')

	def load(self, pickle_name):
		with open(pickle_name, 'rb') as p:
			self.loaded_pickle = pickle.load(p)
		print(f'{pickle_name} is successfully loaded')










