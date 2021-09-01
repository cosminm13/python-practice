import requests
from bs4 import BeautifulSoup


def get_category(URL):
    """Extract the category's name from a given URL from one of these categories:
    https://www.enchantedlearning.com/wordlist/
    """
    page_html = requests.get(URL).content
    soup = BeautifulSoup(page_html, 'html.parser')
    category_name = str(soup.find(class_='body-title__title').contents[0])
    return category_name


def scrape_category(URL):
    """Extract the category name and words from a given URL from one of these categories:
    https://www.enchantedlearning.com/wordlist/
    If the words contain HTML tags or non-alphanumeric characters, they will be removed.
    """
    try:
        page_html = requests.get(URL).content
    except Exception as e:
        print('Could not fetch page!')
    soup = BeautifulSoup(page_html, 'html.parser')
    category_name = str(soup.find(class_='body-title__title').contents[0])
    words_soup = soup(class_='wordlist-item')

    words = []
    for word in words_soup:
        words.append(word.contents)
    words = [word for sublist in words for word in sublist]

    # Remove words that don't match the format
    for word in words:
        if 'bs4.element.Tag' in str(type(word)):
            words.remove(word)
    words = [str(word) for word in words]
    for word in words:
        if 'href' in word:
            words.remove(word)
    return category_name, words

# if __name__ == '__main__':
#     food_url = 'https://www.enchantedlearning.com/wordlist/food.shtml'
#     food_words = scrape_category(food_url)
#     print(food_words)
