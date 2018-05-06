from bs4 import BeautifulSoup
import urllib.request


resp = urllib.request.urlopen("https://www.bhphotovideo.com")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    print(link['href'])