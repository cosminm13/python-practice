import utils
import app


# ex2
def sum_kw(*args, **kwargs):
    total = 0
    for k, v in kwargs.items():
        total += v
    return total


# ex3
def vowels(string_input):
    vow = []
    for c in string_input:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            vow.append(c)
    return vow


def vowels_filter(c):
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False


# ex4
def dictionaries(*args, **kwargs):
    dicts = []
    for arg in args:
        if isinstance(arg, dict):
            if len(arg) >= 2:
                cont = True
                for key, value in arg.items():
                    if cont is True:
                        if len(str(key)) >= 3:
                            dicts.append(arg)
                            cont = False
    for k, v in kwargs.items():
        if isinstance(v, dict):
            if len(v) >= 2:
                cont = True
                for key, value in v.items():
                    if cont is True:
                        if len(str(key)) >= 3:
                            dicts.append(v)
                            cont = False
    return dicts


# ex5
def numbers_list(input_list):
    numbers = []
    for i in input_list:
        if type(i) is int or type(i) is float:
            numbers.append(i)
    return numbers


# ex6
def integers(int_list):
    even = []
    odd = []
    for i in int_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return list(zip(even, odd))


# ex7
def process(**kwargs):
    fibonacci = [0, 1]
    for i in range(2, 1000):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if 'filters' in kwargs:
        for f in kwargs['filters']:
            fibonacci = filter(f, fibonacci)
    filtered_fibonacci = list(fibonacci)
    if 'offset' in kwargs:
        filtered_fibonacci = filtered_fibonacci[kwargs['offset']:]
    if 'limit' in kwargs:
        filtered_fibonacci = filtered_fibonacci[:kwargs['limit']]
    return filtered_fibonacci

def sum_digits(x):
    return sum(map(int, str(x)))


# ex8
def print_arguments(function):
    def inner(*args, **kwargs):
        x = function(*args, **kwargs)
        print(f'Arguments are: {args}, {kwargs} and will return {x}')
        return x
    return inner

def multiply_by_two(x):
    return x * 2


def multiply_output(function):
    def inner(*args, **kwargs):
        x = function(*args, **kwargs)
        return x * 2
    return inner

@multiply_output
def multiply_by_three(x):
    return x * 3

# multiply_by_three = multiply_output(multiply_by_three)


def augment_function(function, decorators):
    def inner(*args, **kwargs):
        return function(*args, **kwargs)
    for decorator in decorators[::-1]:
        inner = decorator(inner)
    return inner


def add_numbers(a, b):
    return a + b


# ex9
def pairs_dict(pairs):
    l = []
    for pair in pairs:
        sum_pair = pair[0] + pair[1]
        prod_pair = pair[0] * pair[1]
        pow_pair = pow(pair[0], pair[1])
        l.append({'sum': sum_pair, 'prod': prod_pair, 'pow': pow_pair})
    return l


if __name__ == '__main__':
    # print(utils.process_item(125))  # ex1a
    # app.infinite_input()  #ex1b
    # print(sum_kw(1, 2, c=3, d=4))  # ex2a
    # sum_kw_lambda = lambda *args, **kwargs: sum(kwargs.values())
    # print(sum_kw_lambda(1, 2, c=3, d=4))  # ex2b
    # s = 'Programming in Python is fun'
    # vowles_lambda = lambda string2: [c for c in string2 if c.lower() in ['a', 'e', 'i', 'o', 'u']]
    # vowles_list_comprehension = [c for c in s if c.lower() in ['a', 'e', 'i', 'o', 'u']]
    # print(vowels(s))
    # print(vowles_lambda(s))
    # print(vowles_list_comprehension)
    # print(list(filter(vowels_filter, s)))  # ex3
    # print(dictionaries({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))  # ex4
    # print(numbers_list([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))  # ex5
    # print(integers([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))  # ex6
    # print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], offset=2, limit=2))  # ex7
    augmented_multiply_by_two = print_arguments(multiply_by_two) # ex8
    x = augmented_multiply_by_two(10)
    print(multiply_by_three(10))
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    y = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
    # print(pairs_dict([(5, 2), (19, 1), (30, 6), (2, 2)]))  # ex9
