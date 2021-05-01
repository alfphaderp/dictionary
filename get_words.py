from bs4 import BeautifulSoup
import urllib.request
import pickle

def get_words(letter, page):
    try:
        url = f'https://www.dictionary.com/list/{letter}/{page}'
        site = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(site, 'html.parser')
        
        words = []
        for elements in soup.findAll('a', {'class': 'e3scdxh3'}):
            if not elements.string.endswith(' synonyms '):
                words.append(str(elements.string))
        return words
    except:
        return []

all_words = []
for letter in '0abcdefghijklmnopqrstuvwxyz':
    page_num = 1
    words = get_words(letter, page_num)
    while words:
        all_words.extend(words)
        page_num += 1
        words = get_words(letter, page_num)
    print(f'done with {letter}')

with open('words.txt', 'w') as file:
    pickle.dump(all_words, file)