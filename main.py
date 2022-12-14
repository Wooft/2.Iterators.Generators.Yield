from iterator import FlatIterator
from Generator import unpackage

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
	[[1, 4, 7], [1, 2, 4]]
]


if __name__ == '__main__':

	for item in FlatIterator(nested_list):
		print(item)
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)


    # flat_generator = unpackage(nested_list)
    # for item in flat_generator:
    #     print(item)