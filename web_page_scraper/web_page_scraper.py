import requests
from bs4 import BeautifulSoup
import string
import os

def sanitize_filename(title):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_title = title.translate(translator)
    cleaned_title = cleaned_title.replace(" ", "_")
    return cleaned_title

def save_article(url, filename):
    try:
        article_response = requests.get(url)
        article_response.raise_for_status()
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        body_content = article_soup.find('div', class_='c-article-body')
        if body_content:
            text_content = body_content.get_text(separator='\n', strip=True)
            text_content = text_content.replace(" ", "")

            with open(filename, 'wb') as f:
                f.write(text_content.encode('utf-8'))
            return True
        else:
            print(f"Article content not found in <div class='c-article-body'> for: {url}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error downloading article from {url}: {e}")
        return False
    except Exception as e:
        print(f"Error processing article from {url}: {e}")
        return False

def main():
    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        saved_articles = []
        article_elements = soup.find_all('article')

        for article_element in article_elements:
            article_type_span = article_element.find('span', {'data-test': 'article.type'})
            if article_type_span and article_type_span.text.strip() == 'News':
                link_tag = article_element.find('a', {'data-track-action': 'view article'})
                if link_tag and 'href' in link_tag.attrs:
                    article_url = "https://www.nature.com" + link_tag['href']
                    title_tag = article_element.find('h3')
                    if title_tag:
                        article_title = title_tag.text.strip()
                        sanitized_title = sanitize_filename(article_title).replace(" ", "")
                        filename = f"{sanitized_title}.txt"
                        if save_article(article_url, filename):
                            saved_articles.append(filename)
                            print(f"Saved article: {filename}")

        print("\nSaved articles:", saved_articles)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the main page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()