# ex1
def sets(a, b):
    return set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)


# ex2
def frequency_list(string):
    freq = {}
    for s in string:
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1
    return freq


# ex3 : TODO
def nested_dictionaries(a, b):
    diff = []
    def compare_structures(a, b):
        if not type(a) == type(b):
            diff.append((a, b))
        elif type(a) is str or not hasattr(a, '__iter__'):
            if a != b:
                diff.append((a, b))
        else:
            if type(a) is dict:
                if len(a) != len(b):
                    diff.append((a, b))
                else:
                    for key in a:
                        try:
                            compare_structures(a[key], b[key])
                        except KeyError:
                            diff.append((a, b))
                            break
            elif type(a) in [list, tuple, set, frozenset]:
                if len(a) != len(b):
                    diff.append((a, b))
                else:
                    for x, y in zip(a, b):
                        compare_structures(x, y)
    compare_structures(a, b)
    return diff


# ex4
def build_xml_element(tag, content, **elements):
    output = '<' + tag + ' '
    for element in elements:
        output += element + '=\"' + elements[element] + '\"'
    output += '> ' + content + '</' + tag + '>'
    return output


# ex5
def validate_dict(validation_rules, dictionary):
    for rule in validation_rules:
        if not validated(dictionary, rule):
            return False
    return True


def validated(dictionary, rule):
    key = rule[0]
    prefix = rule[1]
    middle = rule[2]
    suffix = rule[3]
    dict_value = dictionary[key]
    for i in range(len(prefix)):
        if prefix[i] != dict_value[i]:
            return False
    for i in range(0, len(suffix), -1):
        if suffix[i] != dict_value[i]:
            return False
    if middle in dict_value and middle[0] != dict_value[0] and middle[-1] != dict_value[-1]:
        return True
    else:
        return False


# ex6
def uniques_and_duplicates(input_set):
    d = {}
    uniques = 0
    for i in input_set:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key, value in d.items():
        if value == 1:
            uniques += 1
    return uniques, len(d) - uniques


# ex7
def sets_dictionary(*args):
    my_lambda = lambda x, y: {f'{x} | {y}': x | y, f'{x} & {y}': x & y, f'{x} - {y}': x - y, f'{y} - {x}': y - x}
    my_dict = {}
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            my_dict.update(my_lambda(args[i], args[j]))
    return my_dict


# ex8
def looping_path(mapping):
    # input_dict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    keys = []
    key = 'start'
    value = mapping[key]
    while value not in keys and key != value:
        keys.append(value)
        key = value
        value = mapping[key]
    return keys



# ex9
def args_and_kwargs(*args, **kwargs):
    counter = 0
    for arg in args:
        for k, v in kwargs.items():
            if arg == v:
                counter += 1
    return counter


if __name__ == '__main__':
    # print(sets([1, 2, 3, 4, 5], [4, 5, 6, 7]))
    # print(frequency_list('Ana has apples.'))
    # print(nested_dictionaries({1: 1}, {2: 2, 3: {4: 4}}))
    # print(build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link "))
    # print(validated({'word1': 'abcdefghijklmnopqrstuvwxyz'}, ('word1', 'abc', 'defgh', 'yz')))
    # print(uniques_and_duplicates([1, 2, 3, 4, 4, 4, 5, 6, 7]))
    # print(sets_dictionary({1, 2}, {2, 3}))
    print(looping_path({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    # print(args_and_kwargs(1, 2, 3, 4, x=1, y=2, z=3, w=5))
