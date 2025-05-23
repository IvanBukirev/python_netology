import types

"""
Задача.1 - Итератор по списку списков.
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_cursor = 0
        self.inner_cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_cursor < len(self.list_of_list):
            current_list = self.list_of_list[self.outer_cursor]
            if self.inner_cursor < len(current_list):
                item = current_list[self.inner_cursor]
                self.inner_cursor += 1
                return item
            else:
                self.outer_cursor += 1
                self.inner_cursor = 0
        raise StopIteration


def test_1():
    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
                                              ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None], ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None]


"""
Задача.2 - Генератор по списку списков.
"""


def flat_generator(list_of_lists):
    for inner_list in list_of_lists:
        for item in inner_list:
            yield item


def test_2():
    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(flat_generator(list_of_lists_1),
                                              ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None], ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


"""
Задача.3 - Итератор любой вложенности.
"""


class FlatIteratorAnyLevel:

    def __init__(self, list_of_list):
        self.stack = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_iter = self.stack[-1]
            try:
                item = next(current_iter)
            except StopIteration:
                self.stack.pop()
                continue
            if isinstance(item, list):
                self.stack.append(iter(item))
            else:
                return item
        raise StopIteration


def test_3():
    list_of_lists_2 = [[["a"], ["b", "c"]], ["d", "e", [["f"], "h"], False], [1, 2, None, [[[[["!"]]]]], []]]

    for flat_iterator_item, check_item in zip(FlatIteratorAnyLevel(list_of_lists_2),
                                              ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"]):
        assert flat_iterator_item == check_item

    assert list(FlatIteratorAnyLevel(list_of_lists_2)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None,
                                                           "!"]


"""
Задача.4 - Генератор любой вложенности.
"""


def flat_generator_any_level(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, list):
            yield from flat_generator_any_level(item)
        else:
            yield item


def test_4():
    list_of_lists_2 = [[["a"], ["b", "c"]], ["d", "e", [["f"], "h"], False], [1, 2, None, [[[[["!"]]]]], []], ]

    for flat_iterator_item, check_item in zip(flat_generator_any_level(list_of_lists_2),
                                              ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"], ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_any_level(list_of_lists_2)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None,
                                                               "!"]

    assert isinstance(flat_generator_any_level(list_of_lists_2), types.GeneratorType)


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
