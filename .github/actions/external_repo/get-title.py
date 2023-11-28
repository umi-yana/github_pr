import requests
import bs4

url = 'https://www.flinters-base.co.jp/'

r = requests.get(url)
html_text = bs4.BeautifulSoup(r.text, 'html.parser')
print(html_text.title.text)