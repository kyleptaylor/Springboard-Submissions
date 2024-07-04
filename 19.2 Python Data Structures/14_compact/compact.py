def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # new_lst = []
    # for el in lst:
    #     if el:
    #         new_lst.append(el)

    # return new_lst

    return [val for val in lst if val]