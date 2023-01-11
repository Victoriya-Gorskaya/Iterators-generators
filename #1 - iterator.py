import requests

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

class FlatIterator:

    def __init__(self, list_of_lists_1):
        self.list_of_lists_1 = list_of_lists_1

    def __iter__(self):
        self.outer_list_cursor = 0  # курсор основного списка
        self.inner_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):
        self.inner_list_cursor += 1
        if self.inner_list_cursor == len(self.list_of_lists_1[self.outer_list_cursor]): 
            self.outer_list_cursor += 1
            self.inner_list_cursor = 0

        if self.outer_list_cursor == len(self.list_of_lists_1):
            raise StopIteration

        return self.list_of_lists_1[self.outer_list_cursor][self.inner_list_cursor]
    
if __name__ == '__main__':
    for item1 in FlatIterator(list_of_lists_1):
        print(item1)
        
        

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()