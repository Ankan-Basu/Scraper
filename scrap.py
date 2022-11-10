import requests
from bs4 import BeautifulSoup

def scraper(query):
    # url = 'https://www.google.com/search?q=sikkim&rlz=1C1ONGR_enIN1025IN1025&oq=sikkim&aqs=chrome..69i57.1480j0j1&sourceid=chrome&ie=UTF-8'
    # url = 'https://www.google.com/search?q=darjeeling&rlz=1C1ONGR_enIN1025IN1025&oq=darjeeling&aqs=chrome..69i57j0i271l2.2536j0j9&sourceid=chrome&ie=UTF-8'

    url = f'https://www.google.com/search?q={query}'
    resp = requests.get(url)

    print(resp)

    soup = BeautifulSoup(resp.content, 'html.parser');

    x = soup.find_all('div', class_='egMi0 kCrYT')

    results = []
    cnt = 0
    with open('a.txt', 'w') as file:
        for elem in x:
            cnt += 1
            y = elem.children
            z = next(y)
            zzz = z.attrs['href']
            zz = z.find('div', class_='BNeawe vvjwJb AP7Wnd').string
            zzzz = str(zz) + '\n', str(zzz) + '\n', '\n\n'
            results.append(zzzz)

            if (cnt == 5):
                break
        
        for result in results:
            for elem in result:
                file.write(elem)

def query_generator(search_word):
    tmp = search_word.split()
    res ='+'.join(tmp)
    return res

if __name__ == '__main__':
    search_word = input('Enter search word: ')
    query = query_generator(search_word)
    scraper(query)
