from typing import List


def strip_words(iterable: List[str]) -> List[str]:
    return [word.strip() for word in iterable]


def factorial(number: int) -> int:
    if number == 2:
        return number
    else:
        return factorial(number - 1) * number


def permutations(elements: []) -> []:
    if len(elements) == 1:
        return [elements]
    else:
        element = elements.pop()
        old_permutations = permutations(elements)

        new_permutations = []

        for old_permutation in old_permutations:
            new_permutation_len = len(old_permutation) + 1
            index = 0

            while index < new_permutation_len:

                new_permutation = old_permutation.copy()
                new_permutation.insert(index, element)
                new_permutations.append(new_permutation)

                index += 1
        return new_permutations
