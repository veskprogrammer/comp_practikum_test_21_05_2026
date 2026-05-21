import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/companies/gnivc/news/1037538/'

def parse_article():
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Название статьи (обычно в <h1>)
    title_tag = soup.find('h1')
    title = title_tag.text.strip() if title_tag else "Не найдено"
    
    # Автор (ищем по классам, характерным для Habr)
    author_tag = soup.find('a', class_='tm-user-info__user')
    if not author_tag:
        author_tag = soup.find('span', class_='tm-user-info__user')
    author = author_tag.text.strip() if author_tag else "Не найден"
    
    # Дата публикации
    date_tag = soup.find('time')
    date = date_tag.get('title') or date_tag.text.strip() if date_tag else "Не найдена"
    
    print(f"Название: {title}")
    print(f"Автор: {author}")
    print(f"Дата: {date}")

if __name__ == "__main__":
    parse_article()
