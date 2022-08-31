#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    max_val = 0
    for key, value in sorted(a_dictionary.items()):
        if value >= max_val:
            max_val = value
            key = key

    return key
