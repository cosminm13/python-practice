# ex1
def fibonacci_n(n):
    numbers = [0, 1]
    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-2])
    return numbers


# ex2
def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 1 / 2) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes(numbers):
    # primes = []
    # for n in numbers:
    #     if prime(n):
    #         primes.append(n)
    # return primes
    return list(filter(prime, numbers))


# ex3
def sets(a, b):
    print(f"Intersection: {set(a) & set(b)}")
    print(f"Union: {set(a) | set(b)}")
    print(f"A - B: {set(a) - set(b)}")
    print(f"B - A: {set(b) - set(a)}")


# ex4
def compose(notes, moves, start):
    song = [notes[start]]
    current_position = start
    for i in range(0, len(moves), 1):
        current_position += moves[i]
        if current_position >= len(notes):
            current_position -= len(notes)
        song.append(notes[current_position])
    return song


# ex5
def zero_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j < i:
                matrix[i][j] = 0
    return matrix


# ex6
def count_elements(x, *args):
    dictionary = {}
    correct = []
    for l in args:
        for e in l:
            if e in dictionary:
                dictionary[e] += 1
            else:
                dictionary[e] = 1
    for key in dictionary:
        if dictionary[key] == x:
            correct.append(key)
    return correct


# ex7
def greatest_palindrome(integers):
    palindrome_list = []
    for n in integers:
        if str(n) == str(n)[::-1]:
            palindrome_list.append(n)
    return len(palindrome_list), max(palindrome_list)


# ex8
def divisible_ascii(x=1, strings=[], flag=False):
    div = []
    for s in strings:
        if flag:
            for c in s:
                if ord(c) % x == 0:
                    div.append(c)
        else:
            for c in s:
                if ord(c) % x != 0:
                    div.append(c)
    return div


# ex9
def spectators(matrix):
    l = []
    for i, col in enumerate(zip(*matrix)):
        for j, height in enumerate(col[1:], start=1):
            if height < max(col[0:j]):
                l.append((j, i))
    return l


# ex10
def concatenate(*lists):
    my_zip = []

    for index in range(max(len(l) for l in lists)):
        my_zip.append(tuple(map(lambda x: myf(x, index), lists)))
        # tup = tuple(myf(l, index) for l in lists)
        # my_zip.append(tup)

    return my_zip

def myf(li: list, index):
    try:
        return li[index]
    except:
        return None


# ex11
def sort_tuples(tuples_list):
    tuples_list.sort(key=lambda x: x[1][2])
    return tuples_list


# ex12
def rhyming_words(words):
    endings = {}
    for word in words:
        rhyme = word[-2::]
        if rhyme in endings:
            endings[rhyme].append(word)
        else:
            endings[rhyme] = [word]
    return list(endings.values())


if __name__ == '__main__':
    print(fibonacci_n(10))
    print(print_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(sets([1, 2, 3, 4, 5], [4, 5, 6, 7]))
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print(zero_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(count_elements(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
    print(greatest_palindrome([12343, 12321, 858, 66, 95]))
    print(divisible_ascii(2, ["test", "hello", "lab002"], False))
    print(spectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
    print(concatenate([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
    print(sort_tuples([('abc', 'bcd'), ('abc', 'zza')]))
    print(rhyming_words(['ana', 'banana', 'carte', 'arme', 'parte']))
