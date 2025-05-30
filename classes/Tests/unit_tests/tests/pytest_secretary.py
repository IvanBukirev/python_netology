from classes.Tests.unit_tests.tasks_from_the_first_module import get_name, get_directory, documents


# Тесты для функции get_name
def test_get_name_existing_document():
    assert get_name("10006") == "Аристарх Павлов"
    assert get_name("11-2") == "Геннадий Покемонов"


def test_get_name_non_existing_document():
    assert get_name("несуществующий номер") == "Документ не найден"


# Тесты для функции get_directory
def test_get_directory_existing_document():
    assert get_directory("10006") == "2"
    assert get_directory("11-2") == "1"


def test_get_directory_non_existing_document():
    assert get_directory("несуществующий номер") == "Полки с таким документом не найдено"
    assert get_directory("") == "Полки с таким документом не найдено"  # Пустой ввод


# Проверка документа без полки (в данных нет такого, но проверим)
def test_get_directory_document_without_shelf():
    # Добавим временно документ без полки
    new_doc = {"type": "test", "number": "000", "name": "Тест"}
    documents.append(new_doc)
    assert get_directory("000") == "Полки с таким документом не найдено"
    documents.pop()  # Возвращаем исходные данные
