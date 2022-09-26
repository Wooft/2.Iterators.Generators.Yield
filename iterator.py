class FlatIterator():
    def __init__(self, some_list: list):
        self.list = []
        def unpackage(some_list: list):
            counter = 0
            while counter < len(some_list):
                if isinstance(some_list[counter], list):
                    mylist = unpackage(some_list[counter])
                    for elements in mylist:
                        yield elements
                else:
                    yield some_list[counter]
                counter += 1
        flat_list = unpackage(some_list)
        for items in flat_list:
            self.list.append(items)

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):
        self.nested_list_cursor += 1

        if self.nested_list_cursor == len(self.list):
            raise StopIteration

        return self.list[self.nested_list_cursor]
