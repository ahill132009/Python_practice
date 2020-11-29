from bs4 import BeautifulSoup as bs
import requests
import re
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}


with open('./links_of_containers', 'r') as f_open:
	for url in f_open:
		container_number = re.search(r'(?<=\?id=)\d.*?$', url)
		response = requests.get(url, headers=headers)
		links = re.findall(r'\bhttps:.*?html\b', response.text)

		with open(f'./links_articles_from_{container_number.group(0)}', 'w') as file_art:
			for link in links:
				file_art.write(link)
				file_art.write('\n')
		

print('Done')