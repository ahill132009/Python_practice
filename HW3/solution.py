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
		f = open(self.path, 'r+')
		f.write(self.text)
		f.close
		return 'Text was successfully written'

	def count(self):
		word_count = 0
		line_count = 0
		file_contents = open(self.path, 'r').read()
		word_count += len(word_tokenize(file_contents))
		line_count = len(file_contents.splitlines())
		return f'Number of lines is {line_count}\nNumber of words is {word_count}'

	def __add__(self, other):
		self_dir_path = ''.join(os.path.split(self.path)[:-1])
		other_dir_path = ''.join(os.path.split(other.path)[:-1])
		file1 = open(self.path, 'r').read()
		file2 = open(other.path, 'r').read()
		new_file_address = self_dir_path + '/concatenated_file.txt'
		resulted_file = open(new_file_address, 'w+')
		resulted_file.write(file1)
		resulted_file.write('\n')
		resulted_file.write(file2)
		resulted_file.close()
		return f"Texts from {self.path} and {other.path} were written in {new_file_address}"

	def __str__(self):
		# Prints file path 
		return f"Path to file is {''.join(os.path.split(self.path)[:-1])}"

