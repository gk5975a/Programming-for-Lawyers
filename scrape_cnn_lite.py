import requests
from bs4 import BeautifulSoup
import time

BASE_URL = 'https://lite.cnn.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def get_article_links(session):
    """Return a set of article URLs found on the main page."""
    try:
        r = session.get(BASE_URL, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"Failed to load {BASE_URL}: {e}")
        return []
    soup = BeautifulSoup(r.text, 'html.parser')
    links = set()
    for a in soup.select('a.article-link, a.ticker-link, a.headline'):  # Adjust selectors as needed
        href = a.get('href')
        if href and href.startswith('/'):
            links.add('https://lite.cnn.com' + href)
        elif href and href.startswith('http'):
            links.add(href)
    return list(links)

def fetch_article(session, url):
    try:
        r = session.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"Failed to load article {url}: {e}")
        return None
    soup = BeautifulSoup(r.text, 'html.parser')
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else 'No Title'
    # CNN Lite usually has article body in <article> or <div class='body'>
    body = ''
    article_tag = soup.find('article')
    if article_tag:
        body_p = article_tag.find_all('p')
        body = '\n'.join(p.get_text(strip=True) for p in body_p)
    else:
        body = soup.get_text(strip=True)
    return title, body

def main(save_path='scrape.txt', max_articles=100):
    session = requests.Session()
    article_urls = get_article_links(session)
    if not article_urls:
        print("No article links found.")
        return
    articles_collected = 0
    with open(save_path, 'w', encoding='utf-8') as f:
        for url in article_urls:
            if articles_collected >= max_articles:
                break
            result = fetch_article(session, url)
            if result:
                title, body = result
                f.write(f"Title: {title}\n")
                f.write(f"URL: {url}\n")
                f.write(f"Body:\n{body}\n")
                f.write("\n---\n\n")
                articles_collected += 1
                print(f"Collected {articles_collected}: {title}")
                time.sleep(0.5)  # polite delay
    print(f"Finished. {articles_collected} articles saved to {save_path}")

if __name__ == '__main__':
    main()
