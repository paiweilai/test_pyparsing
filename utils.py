def replace_with(old_text, new_strings, intervals):
    indices = _get_split_indices(intervals)
    text_in_list = _split_list_by_indices(old_text, indices)
    text_without_old_strings = _remove_odd_elements(text_in_list)
    new_strings += ['']  # to make zip even
    result = _get_interleaved_lists(text_without_old_strings, new_strings)
    return ''.join(result).rstrip()


def _get_split_indices(intervals):
    indices = [start for (start, _) in intervals]
    indices += [end for (_, end) in intervals]
    return sorted(list(set(indices)))


def _split_list_by_indices(alist, indices):
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]


def _remove_odd_elements(alist):
    return alist[0::2]


def _get_interleaved_lists(list1, list2):
    return [x for pair in zip(list1, list2) for x in pair]
