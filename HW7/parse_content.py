from bs4 import BeautifulSoup as bs
import requests
import time
import re
import csv
import os
from tqdm import tqdm
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

# iterate over all containers in folder
# for container in os.listdir(os.getcwd()):

input_file_name = 'links_articles_from_1090274326'
with open('./' + input_file_name, 'r') as input_file, open('articles_from_1090274326.csv', 'w', newline='') as output_csv, \
	open('./' + input_file_name + '.cache', 'w') as cache:
    writer = csv.writer(output_csv)

    for base_url in tqdm(input_file):

		base_url = 'https://www.sports.ru/basketball/1090993313-dzheremi-lin-xochu-vernutsya-v-nba-i-dominirovat.html'
		response = requests.get(base_url, headers=headers)
		time.sleep(1)
		# print(response.text)

		soup = bs(response.content, 'lxml')
		if soup.string:
			soup.strong.clear()

		# заголовок
		headline = soup.select('[class~="h1_size_tiny"],h1[itemprop^="name"]')[0].string

		# date
		date = soup.select('[class~="time-block_lh30"]')[0].string

		# tags
		tags_bs = soup.find_all(class_="news-item__tags-line")
		tags = []
		for z in tags_bs[0].find_all('a'):
			tags.append(z.string)

		# comments_number
		comms = soup.find_all(class_='news-item__comments-link')[0]
		for x in comms.strings:
			comments_number = int(re.match(r'\d.*? ', x).group(0))

		# текст
		text = ''
		body_txt = soup.select_one('.news-item__content')
		for st in body_txt.stripped_strings:
			text += st.strip() + ' '

		# author
		author= soup.select("div[itemprop='author']")[0].select("span[itemprop='name']")[0].string

		rows = base_url, headline, date, tags, comments_number, str(author), text  


		writer.writerow(['Link', 'Headline', 'Date', 'Tags', 'Number of comments', 'Author', 'Text'])
		writer.writerow(rows)

		cache.write(f'Wrote {base_url} from {input_file_name}' + '\n')

