from utils import process_item

def infinite_input():
    while 1:
        number = input()
        if str(number) == 'q':
            break
        if number.isdigit():
            print(process_item(int(number)))
