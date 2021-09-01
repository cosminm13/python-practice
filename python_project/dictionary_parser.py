import json
import words_scraper


def generate_json(url_list):
    """Append missing categories and their words to the JSON file.
    """
    try:
        with open('words_dictionary.json', 'r+') as f:
            data = json.load(f)
    except Exception as e:
        print('Could not load file into JSON!')
        data = {}
    # print(data)
    loaded_json = data
    for url in url_list:
        if words_scraper.get_category(
                url) not in data:  # Check if the category already exists in JSON and scrape the page otherwise
            scraped_url = words_scraper.scrape_category(url)
            loaded_json.update({scraped_url[0]: scraped_url[1]})  # Append scraped page to JSON
    # print(json.dumps(loaded_json))
    try:
        with open('words_dictionary.json', 'w') as json_file:
            json.dump(loaded_json, json_file)  # write JSON to file
    except Exception as e:
        print('Could not write to file!')
    return 'Successfully generated JSON!'


def get_categories():
    """Return a list of categories from the existing JSON file."""
    categories = []
    try:
        with open('words_dictionary.json', 'r+') as f:
            data = json.load(f)
    except Exception as e:
        print('Could not load file into JSON!')
    for k, v in data.items():
        categories.append(k)
    return categories


def get_words_from_category(category):
    """Return a list of words from a given category."""
    try:
        with open('words_dictionary.json', 'r+') as f:
            data = json.load(f)
    except Exception as e:
        print('Could not load file into JSON!')
    for k, v in data.items():
        if k == category:
            return v

# if __name__ == '__main__':
#     url = ['https://www.enchantedlearning.com/wordlist/food.shtml',
#            'https://www.enchantedlearning.com/wordlist/house.shtml',
#            'https://www.enchantedlearning.com/wordlist/furniture.shtml']
#     print(generate_json(url))
#     print(get_categories())
#     print(get_words_from_category(' Food Vocabulary Word List '))
