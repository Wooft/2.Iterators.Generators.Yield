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