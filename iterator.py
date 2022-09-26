class FlatIterator():
    def __init__ (self, some_list: list):
        self.list = some_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):
        self.nested_list_cursor += 1

        if self.nested_list_cursor == len(self.list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0

        if self.main_list_cursor == len(self.list):
            raise StopIteration

        return self.list[self.main_list_cursor][self.nested_list_cursor]
    #
