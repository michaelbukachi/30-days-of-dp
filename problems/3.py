"""
Word break problem implementation
"""


def has_valid_words(dictionary, input_str):
    n = len(input_str)
    dictionary = set(dictionary)
    valid_words = [False] * n

    for i in range(n):
        if input_str[:i+1] in dictionary:
            valid_words[i] = True

        if valid_words[i]:
            for j in range(i+1, n):
                if input_str[i+1:j+1] in dictionary:
                    valid_words[j] = True

    return valid_words[-1]


if __name__ == '__main__':
    assert has_valid_words(['arrays', 'dynamic', 'heaps', 'IDeserve', 'learn', 'learning', 'linked', 'list', 'platform',
                            'programming', 'stacks', 'trees'], 'IDeservelearningplatform')
    assert has_valid_words(['IDeservelearningplatform'], 'IDeservelearningplatform')
