import re
import os


# ex1
def extract_words(text):
    # return [word for word in text.split(' ') if word.isalnum()]
    return re.findall('[A-Za-z0-9]+', text)


# ex2
def match_regex(regex, text, length):
    matched = re.findall(regex, text)
    matched_length = []
    for m in matched:
        if len(m) == length:
            matched_length.append(m)
    return matched_length


# ex3
def matching_strings(text, regex_list):
    matched = []
    for r in regex_list:
        matched.append(re.findall(r, text))
    final_list = list(set([i for m in matched for i in m]))
    return final_list


# ex4
def match_attributes(path_to_xml_file, attributes):
    matches = []
    with open(path_to_xml_file) as f:
        lines = f.readlines()
        regex = '<.*'
        for key, value in attributes.items():
            regex += key + '=\"' + value + '\" '
        regex = regex[:-1]
        regex += '.*>.*'
        pattern = re.compile(regex)
        for line in lines:
            match = re.search(pattern, line)
            if match is not None:
                matches.append(match.group(0))
    return matches


# ex5
def match_one_attribute(path_to_xml_file, attributes):
    matches = []
    with open(path_to_xml_file) as f:
        lines = f.readlines()
        regex = '<.*'
        regex += '('
        for key, value in attributes.items():
            regex += key + '=\"' + value + '\"' + '|'
        regex = regex[:-1]
        regex += ')'
        regex += '.*>.*'
        pattern = re.compile(regex)
        for line in lines:
            match = re.search(pattern, line)
            if match is not None:
                matches.append(match.group(0))
    return matches


# ex6
def censored_words(text):
    matched_words = re.findall('[aeiou]\w*[aeiou]', text)
    for word in matched_words:
        censored_word = ''
        for index, letter in enumerate(word):
            if index % 2 == 0:
                censored_word += '*'
            else:
                censored_word += letter
        text = text.replace(word, censored_word)
    return text

# ex7
# https://ro.wikipedia.org/wiki/Cod_numeric_personal_(Rom%C3%A2nia)
def cnp(s):
    matched = re.match('[1-8]{1}[00-99]{2}[01-12]{2}[01-31]{2}[01-52]{2}[001-999]{3}[0-9]{1}', s)
    matched = matched.group(0)
    if matched is not None:
        v = validate(matched)
        if str(v) == matched[-1]:
            return True
    return False

def validate(cnp):
    const = '279146358279'
    sum = 0
    for i, d in enumerate(cnp[:12]):
        cdi = int(const[i])
        sum += cdi * int(d)
    sum %= 11
    if sum < 10:
        return sum
    return 1


def match_files(dirpath, regex):
    matched_file_names = []
    matched_file_contents = []
    final_list = []
    # file names
    for root, subdirectories, files in os.walk(dirpath):
        for file in files:
            if re.match(regex, file):
                matched_file_names.append(os.path.join(root, file))
    # file contents
    for root, subdirectories, files in os.walk(dirpath):
        for file in files:
            f = open(os.path.join(root, file), 'r')
            for line in f:
                if re.match(regex, line):
                    matched_file_contents.append(os.path.join(root, file))
    matched_file_contents = set(matched_file_contents)
    common_list = list(matched_file_contents.intersection(matched_file_names))
    matched_file_names = [f for f in matched_file_names if f not in common_list]
    matched_file_contents = [f for f in matched_file_contents if f not in common_list]
    for f in common_list:
        final_list.append(f'>>{f}')
    for f in matched_file_names:
        final_list.append(f)
    for f in matched_file_contents:
        final_list.append(f)
    return final_list



if __name__ == '__main__':
    # print(extract_words('This is a test1 123'))
    # print(match_regex('\d+', 'Color from pixel 20,30 is 123', 3))
    # print(matching_strings('Color from pixel 20,30 is 123', ['\d+', '\w+']))
    # print(match_attributes('C:\\Users\\Cosmin1213\\Desktop\python_labs\\lab6_test\\ex4.xml', {"class": "url", "name": "url-form", "data-id": "item"}))
    # print(match_one_attribute('C:\\Users\\Cosmin1213\\Desktop\python_labs\\lab6_test\\ex4.xml', {"class": "url", "name": "url-form", "data-id": "item"}))
    # print(censored_words('This is an example'))
    print(cnp('1981123226740'))
    # print(match_files('C:\\Users\\Cosmin1213\\Desktop\python_labs\\lab6_test', '\d+'))