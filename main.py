from iterator import FlatIterator
from Generator import unpackage

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
	[[1, 2, 3], ['a', 'b', 'c'], [None, False]],
	2
]


if __name__ == '__main__':
    flat_generator = unpackage(nested_list)
    for item in flat_generator:
        print(item)