import types

list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

def flat_generator(list_of_lists_2):
    nested_list = True
    while nested_list:
        auxiliary_list = []
        nested_list = False
        for i in list_of_lists_2:
            if isinstance(i, list):
                auxiliary_list.extend(i)
                nested_list = True
            else:
                auxiliary_list.append(i)
        list_of_lists_2 = auxiliary_list
    for i in list_of_lists_2:
        yield i

for item in flat_generator(list_of_lists_2):
    print(item)

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()