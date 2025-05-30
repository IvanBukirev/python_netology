"""
Задание «Квадратное уравнение»
"""


def discriminant(a, b, c):
    """
    Функция для нахождения дискриминанта
    """

    return b ** 2 - 4 * a * c


def solution(a, b, c):
    """
    Функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        return 'корней нет'
    elif d == 0:
        return (-b) / (2 * a)
    else:
        # (-b±√D)/2a
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


"""
Задание «Голосование»
"""


def vote(votes):
    if not isinstance(votes, list):
        raise TypeError("Input must be a list")

    if len(votes) == 0:
        raise ValueError("Input list cannot be empty")

    counts = {}
    for item in votes:
        counts[item] = counts.get(item, 0) + 1

    return max(counts, key=counts.get)


"""
Задание «Секретарь»
 """


documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"}, ]

directories = {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': []}

def get_name(doc_number):
        """
        Принимает номер документа и выводит имя человека, которому он принадлежит. Если такого документа не существует,
        вывести “Документ не найден”
        """
        for dct in documents:
            if doc_number == dct['number']:
                return dct['name']
        return 'Документ не найден'

def get_directory(doc_number):
        """
        Принимает номер документа и выводит номер полки, на которой он находится.
         Если такой документ не найден, на полках вывести “Полки с таким документом не найдено”.
        """
        for shelf, docs in directories.items():
            if doc_number in docs:
                return shelf
        return 'Полки с таким документом не найдено'

def add(document_type, number, name, shelf_number):
        """
        Функция, которая добавит новый документ в каталог и перечень полок.
        """
        # Проверка на дубликат номера документа
        if any(doc['number'] == number for doc in documents):
            print("Документ с таким номером уже существует!")
            return

        # Добавление на полку (создание полки если нужно)
        shelf = str(shelf_number)
        if shelf not in directories:
            directories[shelf] = []

        directories[shelf].append(number)
        documents.append({"type": document_type, "number": number, "name": name})


