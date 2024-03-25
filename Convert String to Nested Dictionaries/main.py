"""
URL: https://www.geeksforgeeks.org/python-convert-string-to-nested-dictionaries/

This is my solution which actually is better in terms of auxulary space than the answer provided in the forum (they provided solution with O(n) auxulary space, here its O(1))

Complexity: O(n)
Auxulary space: O(1)
Time to code: 7 minutes

Think about the reverse of the list. We first start with the inner-most dictionary: {'for': 'geeks'}
Then we pop the next key, and the value will be what we already calculated, so we get: {'best': {'for': 'geeks'}}
And so on. The most important tip is: we only calculate inner-most dictionary and its the next value for the next dictionary.
"""

def convert_to_dict(s: str):
    s = s.split("_")
    prev_value = None
    while s:
        if prev_value is None:
            value = s.pop()
        else:
            value = prev_value
        key = s.pop()
        prev_value = {key: value}
    return prev_value
    

if __name__ == "__main__":
    string = 'gfg_is_best_for_geeks'
    assert convert_to_dict(string) == {'gfg': {'is': {'best': {'for': 'geeks'}}}}

    string = 'one_two_three'
    assert convert_to_dict(string) == {'one': {'two': 'three'}}

