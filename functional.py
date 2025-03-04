import os.path
import re
from datetime import datetime


def copy_file(file_name):
    """
    Функция принимает файл, создает его копию, и побайтово копируем содержание файла в копию
    """
    if os.path.isfile(file_name):
        file_copy = f"{os.path.splitext(file_name)[0]}_copy{os.path.splitext(file_name)[1]}"
        with open(file_name, 'rb') as f:
            with open(file_copy, 'wb') as f_copy:
                for line in f:
                    f_copy.write(line)
        print('File copied!')
    else:
        raise NotADirectoryError('There is no such directory!')


def delete_file(file_name):
    """
    Функция принимает файл, после чего удаляет его
    """
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        raise NotADirectoryError('There is no such directory!')


def count_files(dir_to_count):
    """
    Функция принимает на вход директорию,
    просто проходит по предметам в ней и
    проверяет, файл ли это, и если да...
    То увеличивает счетчик на 1.
    Возвращает счетчик.
    """
    counter = 0
    directory = os.path.normpath(dir_to_count)

    if os.path.exists(directory):
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(dir_to_count, item)):
                counter += 1
        print(f'There are currently: {counter} files in {directory}')
        return counter
    else:
        raise NotADirectoryError('There is no such directory!')


def re_search(pattern, dir=os.getcwd()):
    """
    Функция принимает на вход паттерн и директорию(опционально)
    Рекурсивно проходит по директории.
    Что подошло, добавляется в список, который потом выводится пользователю.
    """
    cur_dir = dir
    result = list()
    if os.path.exists(cur_dir):
        for root, d, files in os.walk(cur_dir):
            for file in files:
                if re.search(pattern, file):
                    result.append(os.path.join(root, file))
        for item in result:
            print(item + '\n')
        return result
    else:
        raise NotADirectoryError('There is no such directory!')


def date_file(path, recursive=False):
    """
    Тут у нас тоже функция в функции. И тоже, для лучшей читаемости.
    В date_to_name передаем путь к файлу, и сам файл.
    Получаем дату его создания, форматируем в строку, и добавляем в имя файла.
    В случе, если передаем в date_file просто путь к файлу, то с извлекаем из него корневую директорию, и его имя, и передаем их в date_to_name.
    В случае, если передаем в date_file папку, но без параметра с рекурсией, то с помощью listdir находим файл, и передаем путь(принятый path), и имя файла(item) в date_to_file
    В случае рекурсии, то же самое, но с помощью os.walk.
    """

    def date_to_name(path, file):
        date_of_creation = os.stat(path).st_ctime
        readable_date = datetime.fromtimestamp(date_of_creation).strftime('%Y_%m_%d')
        new_name = f"{readable_date}_{file}"
        os.rename(os.path.join(path, file), os.path.join(path, new_name))

    if os.path.exists(path):
        if os.path.isfile(path):
            file_name = os.path.split(path)[1]
            file_dir = os.getcwd() if os.path.split(path)[0] is '' else os.path.split(path)[0]
            date_to_name(file_dir, file_name)

        if os.path.isdir(path) and recursive == False:
            dir = os.listdir(path)
            for item in dir:
                if os.path.isfile(os.path.join(path, item)):
                    date_to_name(path, item)

        if os.path.isdir(path) and recursive == True:
            for root, dir, item in os.walk(path):
                for i in item:
                    date_to_name(root, i)
    else:
        raise NotADirectoryError('There is no such directory!')


def analyze(dir=os.getcwd()):
    """
    Тут нужно объясниться.
    Кто такой dir_analyze, и что он забыл вы этой функции?
    Сложно было вместо него рекурсивно вызвать функцию?
    Нет, не сложно, но ради красивого вывода, который не выводит каждый файл
    в каждой вложенной папке я решил вставить функцию в функцию.
    """
    total_size = 0
    result = list()
    print(f'Analyzing: {dir}')
    if os.path.exists(dir):
        def dir_analyze(dir):
            total_size = 0
            for item in os.listdir(dir):
                full_path = os.path.join(dir, item)
                if os.path.isfile(full_path):
                    file_size = os.path.getsize(full_path)
                    total_size += file_size
                elif os.path.isdir(full_path):
                    dir_size = dir_analyze(full_path)
                    total_size += dir_size
            return total_size

        for item in os.listdir(dir):
            full_path = os.path.join(dir, item)
            if os.path.isfile(full_path):
                file_size = os.path.getsize(full_path)
                result.append(f"-File {item} - {file_size}b")
                print(f"-File {item} - {file_size}b")
                total_size += file_size

            elif os.path.isdir(full_path):
                dir_size = dir_analyze(full_path)
                result.append(f'-Dir {full_path} - {dir_size}b')
                print(f'-Dir {full_path} - {dir_size}b')
                total_size += dir_size

        print(f"Total size of directory: {dir} - {total_size}b")
        return result
    else:
        raise NotADirectoryError('There is no such directory!')
