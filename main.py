import requests
from bs4 import BeautifulSoup

#URL IMDB favorites of the moments
url = "https://www.imdb.com/chart/moviemeter/?ref_=watch_tpks_chtmvm"


class Extract:
    def __init__(self):
        pass
    

    def soup(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content,"html.parser")
        return soup

    
    def favorites_imdb(self):
        soup = self.soup(url)
        content_fav = soup.find_all('td',attrs={'class':'titleColumn'})
        cont = 1

        for i in content_fav:
            sub = i.find('a').text
            print(f'{cont} ',sub)
            if cont == 21:
                break
            cont += 1



if __name__ == '__main__':
    cl = Extract()
    cl.favorites_imdb()
                
