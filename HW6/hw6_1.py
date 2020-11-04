import requests 
import sys
from collections import Counter
import re

# Delete token from code later
auth = ('a...', '8b1...')


def main():
	users = [str(x) for x in sys.argv[1:]]
	users_dict = dict(zip([x for x in range(len(users))], users))
	print(f'Current dict is {users_dict}\n')
	input_string = re.split(r'[., ]',input('Choose users from list to show (you may choose several): '))
	print('\n')

	# методы класса
	u = GitHubUser(input_string, users_dict)
	# u.name_description()
	# print(u.language())
	# print(u.most_popular_lang())
	# print(u.most_followers())
	# print(u.max_repos())

class GitHubUser:
	def __init__(self, input_string, users_dict):
		self.input_string = input_string
		self.users_dict = users_dict

	def _dergaem_req(self, nmb):
		foo_usr = self.users_dict[int(nmb)].split('/')[-1]
		req = requests.get(f'https://api.github.com/users/{foo_usr}/repos', auth=auth)
		foo_git_json = req.json()
		return foo_git_json, foo_usr

	def name_description(self):
		for nmb in self.input_string:
			git_json, usr = self._dergaem_req(nmb)
			print(f'Names and descriptions for user {usr}', '\n')
			for i in git_json:
				print(i['name'], '\t','\t', i['description'])
			print('\n')	

	def language(self):
		for nmb in self.input_string:
			git_json, usr = self._dergaem_req(nmb)
			print(f'Names and descriptions for user {usr}', '\n')
			counter_lang_user = Counter(i['language'] for i in git_json)
			return f'{counter_lang_user}\n'		

	def max_repos(self):
		max_repo = Counter({'Nobody': 0})
		for nmb in self.input_string:
			git_json, usr = self._dergaem_req(nmb)
			if list(max_repo.elements()) == []:
				max_repo = Counter({usr: len(git_json)})
			else:
				if len(git_json) > list(max_repo.elements())[0]:
					max_repo = Counter({usr: len(git_json)})
		return f'User {list(max_repo.elements())[0]} has' \
		f'the highest number of repos -- {max_repo.most_common()[0][1]}\n'

	def most_popular_lang(self):
		counter_most_pop_lang = Counter()
		for nmb in self.input_string:
			git_json, _ = self._dergaem_req(nmb)
			for i in git_json:
				counter_most_pop_lang[i['language']] += 1
		return f'Most popular language is {counter_most_pop_lang.most_common(1)[0][0]} ' \
				f'with result {counter_most_pop_lang.most_common(1)[0][1]}'

	# github api не отдаёт больше 30
	def most_followers(self):
		most_fols = Counter({'Nobody': 0})
		for nmb in self.input_string:
			usr = self.users_dict[int(nmb)].split('/')[-1]
			req = requests.get(f'https://api.github.com/users/{usr}/followers', auth=auth)
			num_of_followers = len(req.json()) 
			if num_of_followers > most_fols.most_common(1)[0][1]:
				most_fols.update({usr: num_of_followers})
		return f'{most_fols.most_common(1)[0][0]} has the highest number num_of_followers' \
			f'of followers -- {most_fols.most_common(1)[0][1]}'



if __name__ == '__main__':
	main()