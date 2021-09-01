import re


# ex1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_variable_args(*args):
    num = float('inf')
    for i in range(1, len(args)):
        if gcd(args[0], args[i]) < num:
            num = gcd(args[0], args[i])
    return num


# ex2
def vowels(string):
    count = 0
    for c in string:
        if c in 'aeiouAEIOU':
            count += 1
    return count
    # return len([count for c in string if c in 'aeiouAEIOU'])


# ex3
def substring_count(string1, string2):
    return string1.count(string2)


# ex4
def upper_to_lower(string):
    result = ''
    for c in string:
        if c.isupper():
            result += '_'
            result += c.lower()
        else:
            result += c
    return result[1:]


# ex5
def matrix_spiral(matrix):
    final_string = ''
    while len(matrix):
        final_string += matrix[0]  # append first line
        matrix.pop(0)  # delete first line
        for i in range(len(matrix)):
            final_string += matrix[i][len(matrix)]  # append last column
        for i in range(len(matrix)):
            matrix[i] = matrix[i][:-1]  # delete last column
        final_string += matrix[len(matrix)-1][::-1]  # append last line
        matrix.pop()  # delete last line
        for i in range(len(matrix)):
            final_string += matrix[i-1][0]  # append first column
        for i in range(len(matrix)):
            matrix[i] = matrix[i][1::]  # remove first column
    # print(matrix)
    return final_string


# ex6
def is_palindrome(number):
    return str(number) == str(number)[::-1]


# ex7
def first_number(string):
    return re.search(r'\d+', string).group()


# ex8
def count_bits(number):
    base2 = ''
    while number:
        if number % 2 == 0:
            base2 += '0'
            number //= 2
        else:
            base2 += '1'
            number //= 2
    # return base2[::-1]
    return base2.count('1')


# ex9
def most_common(string):
    dict = {}
    for c in string:
        if c in dict and c.isalpha():
            dict[c] += 1
        else:
            dict[c] = 1
    max_occurrence = 0
    letter = ''
    for key, value in dict.items():
        if value > max_occurrence:
            max_occurrence = value
            letter = key
    return letter


# ex10
def count_words(string):
    return len(re.findall(r'\w+', string))


if __name__ == '__main__':
    # print(gcd_variable_args(15, 25, 30, 40))
    # print(vowels('This is a string.'))
    # print(substring_count('abcbcabc', 'abc'))
    # print(upper_to_lower('ThisIsAString'))
    print(matrix_spiral(['firs', 'n_lt', 'oba_', 'htyp']))
    # print(is_palindrome(123321))
    # print(first_number('An apple is 123 USD'))
    # print(count_bits(24))
    # print(most_common('an apple is not a tomato'))
    # print(count_words('I have Python exam'))
