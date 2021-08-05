from bs4 import BeautifulSoup
import requests

URL = "https://parade.com/937586/parade/life-quotes/"

web_page = requests.get(URL)

soup = BeautifulSoup(web_page.text, "html.parser")

quote = [x.get_text(strip=True, separator=" ") for x in soup.select(
        'span[data-parade-type="promoarea"] .figure_block ~ p')]

all_quotes = [i for i in quote if i[0].isdigit()]
print("\n".join(all_quotes))



















# import json
# import re
#
# URL = "https://parade.com/937586/parade/life-quotes/"
# web_page = requests.get(URL)
# soup = BeautifulSoup(web_page.text, "html.parser")
# result = soup.find('script', attrs={'type': "application/id+json"})
# text = result.string
# data = json.load(text).get('articleBody')
# quotes = []
# for line in data.split('\n'):
#     if re.match(r'\d+\.', line):
#         quotes.append(line)
# print(quotes[0])
# print(quotes[-1])


# for tag in all_anchor_tags:
#     print(tag.get("href"))

# article_tag = soup.find('strong')
# print(article_tag.getText())
