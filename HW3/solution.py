from nltk.tokenize import word_tokenize
import os.path

class FileReader:

	def __init__(self, path):
		self.path = path

	def read(self):
		try: 
			return open(self.path).read()
		except FileNotFoundError:
			return '\n'

	def write(self, text):
		self.text = text
		with open(self.path, 'r+') as f:
			f.write(self.text)
		return 'Text was successfully written'

	def count(self):
		self.line_count = 0
		self.word_count = 0
		with open(self.path, 'r') as f:
			for line in f:
				self.line_count += 1
				self.word_count += len(word_tokenize(line))
		return f'Number of lines is {self.line_count}\nNumber of words is {self.word_count}'

	def __add__(self, other):
		with open(self.path) as f1, open(other.path) as f2, open('./concatenated_file.txt', 'w+') as new_file:
			new_file.write(f'{f1.read()}\n{f2.read()}')
			return FileReader('./concatenated_file.txt')

	def __str__(self):
		return f"Path to file is {''.join(os.path.split(self.path)[:-1])}"
