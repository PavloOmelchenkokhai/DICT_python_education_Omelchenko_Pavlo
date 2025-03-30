import requests
from bs4 import BeautifulSoup
import string
import os

def sanitize_filename(title):
    """Очищає назву для використання як імені файлу."""
    translator = str.maketrans('', '', string.punctuation)
    cleaned_title = title.translate(translator)
    cleaned_title = cleaned_title.replace(" ", "_")
    return cleaned_title

def get_article_content(article_url, article_type):
    """Виділяє вміст статті на основі її типу."""
    try:
        article_response = requests.get(article_url)
        article_response.raise_for_status()
        article_soup = BeautifulSoup(article_response.content, 'html.parser')

        if article_type == 'News':
            body_content = article_soup.find('div', class_='c-article-body')
            if body_content:
                return body_content.get_text(separator='\n', strip=True).replace(" ", "")
        elif article_type == 'Research Highlight':
            body_content = article_soup.find('div', class_='article-item__body')
            if body_content:
                return body_content.get_text(separator='\n', strip=True).replace(" ", "")
        elif article_type == 'News & Views':
            body_content = article_soup.find('div', class_='c-article-body') or article_soup.find('div', class_='c-article-section')
            if body_content:
                return body_content.get_text(separator='\n', strip=True).replace(" ", "")
        elif article_type == 'Comment':
            body_content = article_soup.find('div', class_='c-article-body')
            if body_content:
                return body_content.get_text(separator='\n', strip=True).replace(" ", "")
        elif article_type == 'Nature Briefing':
            body_content_parts = article_soup.find_all('p')
            if body_content_parts:
                text_content = "\n".join([p.get_text(strip=True) for p in body_content_parts]).replace(" ", "")
                return text_content

        print(f"Content structure for '{article_type}' not found or not handled for: {article_url}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error downloading article from {article_url}: {e}")
        return None
    except Exception as e:
        print(f"Error processing article from {article_url}: {e}")
        return None

def save_article(content, filename, page_dir):
    """Зберігає вміст статті у файл у вказаному каталозі."""
    if content:
        filepath = os.path.join(page_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(content.encode('utf-8'))
        return True
    return False

def main():
    try:
        num_pages = int(input("Enter the number of pages to scrape: "))
        article_type = input("Enter the type of articles to search for: ")

        base_url = "https://www.nature.com/nature/articles"
        year = "2022"

        for page_num in range(1, num_pages + 1):
            page_url = f"{base_url}?sort=PubDate&year={year}&page={page_num}"
            page_dir = f"Page_{page_num}"
            os.makedirs(page_dir, exist_ok=True)
            print(f"\nProcessing page: {page_num}")

            try:
                response = requests.get(page_url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                article_elements = soup.find_all('article')

                for article_element in article_elements:
                    type_span = article_element.find('span', {'data-test': 'article.type'})
                    if type_span and type_span.text.strip() == article_type:
                        link_tag = article_element.find('a', {'data-track-action': 'view article'})
                        title_tag = article_element.find('h3')
                        if link_tag and 'href' in link_tag.attrs and title_tag:
                            article_url = "https://www.nature.com" + link_tag['href']
                            article_title = title_tag.text.strip()
                            sanitized_title = sanitize_filename(article_title).replace(" ", "")
                            filename = f"{sanitized_title}.txt"
                            content = get_article_content(article_url, article_type)
                            if save_article(content, filename, page_dir):
                                print(f"  Saved '{article_title}' in {page_dir}")

            except requests.exceptions.RequestException as e:
                print(f"Error accessing page {page_num}: {e}")
            except Exception as e:
                print(f"Error processing page {page_num}: {e}")

        print("\nFinished processing all pages.")

    except ValueError:
        print("Invalid input for the number of pages. Please enter an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()