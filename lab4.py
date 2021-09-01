import os
import sys


# ex1
def file_extensions(directory):
    extensions = []
    for file in os.listdir(directory):
        filename, ext = os.path.splitext(file)
        extensions.append(ext[1:])
    extensions.sort()
    return list(dict.fromkeys(extensions))


# ex2
def absolute_paths(directory, file):
    f = open(file, 'w')
    for file_ in os.listdir(directory):
        filename, ext = os.path.splitext(file_)
        if filename.startswith('A'):
            f.write(file_ + '\n')
    f.close()


# ex3
def file_or_directory(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, 'rb+')
        f.seek(f.tell() - 20, 2)
        last_characters = f.read()
        return last_characters
    elif os.path.isdir(my_path):
        extensions = {}
        for dirpath, dirs, files in os.walk(my_path):
            for file in files:
                filename, ext = os.path.splitext(file)
                if ext in extensions:
                    extensions[ext] += 1
                else:
                    extensions[ext] = 1
        extensions_list = [(k, v) for k, v in extensions.items()]
        extensions_list.sort(reverse=True, key=lambda x: x[1])
        return extensions_list


# ex4
def file_extensions_cl(argv):
    directory = str(argv[1])
    print(directory)
    extensions = []
    for file in os.listdir(directory):
        filename, ext = os.path.splitext(file)
        extensions.append(ext[1:])
    extensions.sort()
    return list(dict.fromkeys(extensions))


# ex5
def target_to_search(target, to_search):
    if os.path.isfile(target):
        f = open(target, 'r')
        if to_search in f.read():
            f.close()
            return True
    elif os.path.isdir(target):
        files_to_search = []
        for dirpath, dirs, files in os.walk(target):
            for file in files:
                filename = os.path.join(dirpath, file)
                try:
                    f = open(filename, 'r')
                    if to_search in f.read():
                        files_to_search.append(filename)
                    f.close()
                except Exception as e:
                    # print(filename, e)
                    pass
        return files_to_search
    else:
        raise ValueError('Not a file or directory')


# ex6
filenames = []
def target_to_search_callback(target, to_search, callback):
    if os.path.isfile(target):
        try:
            with open(target) as f:
                if to_search in f.read():
                    filenames.append(target)
        except Exception as e:
            callback(e)

    elif os.path.isdir(target):
        for filename in os.listdir(target):
            full_path = os.path.join(target, filename)
            target_to_search_callback(full_path, to_search, callback)

def callback_function(e):
    print(e)


# ex7
def file_details(file_path):
    info = {}
    info['full_path'] = os.path.abspath(file_path)
    info['file_size'] = os.path.getsize(file_path)
    info['file_extension'] = os.path.splitext(file_path)[1]
    if os.access(file_path, os.R_OK):
        info['can_read'] = True
    else:
        info['can_read'] = False
    if os.access(file_path, os.W_OK):
        info['can_write'] = True
    else:
        info['can_write'] = False
    return info


# ex8
def absolute_file_paths(dir_path):
    abs_paths = []
    for root, subFolders, files in os.walk(dir_path):
        for file in files:
            abs_paths.append(os.path.join(root, file))
    return abs_paths


if __name__ == '__main__':
    # print(file_extensions('D:\\Downloads'))
    # print(absolute_paths('D:\\Downloads', 'C:\\Users\\Cosmin1213\\Desktop\\python_labs\\lab4_files\\ex2.txt'))
    # print(file_or_directory('C:\\Users\\Cosmin1213\\Desktop\\python_labs\\lab4_files\\ex2.txt'))
    # print(file_or_directory('D:\\Downloads'))
    # print(file_extensions_cl(sys.argv))  # ex4 -> run from terminal
    print(target_to_search('C:\\Users\\Cosmin1213\\Desktop\\python_labs\\lab4_files\\ex2.txt', 'rar'))
    print(target_to_search('C:\\Users\\Cosmin1213\\Desktop\\python_labs', 'rar'))
    target_to_search_callback('C:\\Users\\Cosmin1213\\Desktop\\python_labs', 'rar', callback_function)
    print(filenames)
    # print(file_details('lab4_files\\ex2.txt'))
    # print(absolute_file_paths('D:\\Downloads'))

