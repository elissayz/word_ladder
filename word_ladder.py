#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    from collections import deque
    import copy

    dictionary = []
    with open(dictionary_file, 'r') as f:
        p_dict = f.read()
        dictionary = p_dict.split()

    begin_stack = []
    begin_stack.append(start_word)
    queue = deque()
    queue.append(begin_stack)
    past_words = []

    if start_word == end_word:
        return begin_stack
    if len(start_word) != len(end_word):
        return None

    while queue:
        stack = queue.popleft()
        for i in dictionary:
            if _adjacent(i, stack[-1]):
                if i == end_word:
                    stack.append(i)
                    return stack
                if i not in past_words:
                    stack_copy = copy.copy(stack)
                    stack_copy.append(i)
                    queue.append(stack_copy)
                    past_words.append(i)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    if not ladder:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False

    difference = 0

    for d1, d2 in zip(word1, word2):
        if d1 != d2:
            difference += 1

    if difference == 1:
        return True
    else:
        return False
