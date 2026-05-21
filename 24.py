import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

def parse_first_quote():
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Первая цитата
    quote_tag = soup.find('span', class_='text')
    quote = quote_tag.text.strip() if quote_tag else "Цитата не найдена"
    
    # Имя автора
    author_tag = soup.find('small', class_='author')
    author = author_tag.text.strip() if author_tag else "Автор не найден"
    
    print(f'Цитата: {quote}')
    print(f'Автор: {author}')

if __name__ == "__main__":
    parse_first_quote()
