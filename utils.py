from lab2 import prime

def process_item(x):
    number = int(x) + 1
    while not prime(number):
        number += 1
    return number
