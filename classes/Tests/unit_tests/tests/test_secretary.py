import unittest

from classes.Tests.unit_tests.tasks_from_the_first_module import get_name, get_directory, add


class TestDocumentFunctions(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"}, ]

        self.directories = {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': []}

    def test_get_name_existing_document(self):
        """Поиск имени для существующего документа"""
        self.assertEqual(get_name("10006"), "Аристарх Павлов")
        self.assertEqual(get_name("11-2"), "Геннадий Покемонов")

    def test_get_name_non_existing_document(self):
        """Поиск имени для несуществующего документа"""
        self.assertEqual(get_name("0000"), "Документ не найден")
        self.assertEqual(get_name(""), "Документ не найден")

    def test_get_directory_existing_document(self):
        """Поиск полки для существующего документа"""
        self.assertEqual(get_directory("10006"), "2")
        self.assertEqual(get_directory("11-2"), "1")

    def test_get_directory_non_existing_document(self):
        """Поиск полки для несуществующего документа"""
        self.assertEqual(get_directory("0000"), "Полки с таким документом не найдено")
        self.assertEqual(get_directory(""), "Полки с таким документом не найдено")

    def test_add_duplicate_document(self):
        """Попытка добавить документ с существующим номером"""
        # Сохраняем исходное состояние
        initial_doc_count = len(self.documents)
        initial_dir_count = len(self.directories['1'])

        # Пытаемся добавить дубликат
        add("passport", "2207 876234", "Дубликат", 1)

        # Проверяем что документ не добавился повторно
        self.assertEqual(len(self.documents), initial_doc_count)
        self.assertEqual(len(self.directories['1']), initial_dir_count)


if __name__ == '__main__':
    unittest.main()
