from itertools import chain, zip_longest


def solve(word1: list[str], word2: list[str]) -> bool:
    first = chain.from_iterable(word1)
    second = chain.from_iterable(word2)
    return all(left == right for left, right in zip_longest(first, second))
