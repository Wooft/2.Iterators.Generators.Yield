class FlatIterator():
    def __init__ (self, some_list: list):
        self.list = some_list
        self.start = 0

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor > len(self.list) - 1:
            raise StopIteration
        if isinstance(self.list[self.cursor], list):
            return