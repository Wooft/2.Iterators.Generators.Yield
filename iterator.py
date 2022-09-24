class FlatIterator():
    def __init__ (self, some_list: list):
        self.list = some_list
        self.counter = 0

    def __iter__(self):
        self.counter -= 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.list):
            raise StopIteration
        if isinstance(self.list[self.counter], list):
            return 'list'
        else:
            return self.list[self.counter]

