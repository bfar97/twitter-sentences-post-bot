import bs4 as bs
import urllib.request

req = urllib.request.Request(url="https://www.brainyquote.com/topics/smart",data=b'None',headers={'User-Agent':'forhire-scrapper made by /u/BernardoRodrigues'})
source = urllib.request.urlopen(req).read()
soup = bs.BeautifulSoup(source, 'lxml')

k = soup.find_all("a", "b-qt")
sentences = []

for i in k:
    sentences.append(i.string)
