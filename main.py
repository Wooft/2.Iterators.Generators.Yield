from iterator import FlatIterator

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
	[[1, 2, 3], ['a', 'b', 'c'], [None, False]],
	2
]

def unpackage(some_list: list):
    counter = 0
    while counter < len(some_list):
        if isinstance(some_list[counter], list):
            for elements in some_list[counter]:
                yield elements
        else:
            yield some_list[counter]
        # yield some_list[counter]
        counter += 1

flat_generator = unpackage(nested_list)

for item in flat_generator:
    print(item)