from collections import Counter


def solve(word1: str, word2: str) -> bool:
    first = Counter(word1)
    second = Counter(word2)
    distinct_first = len(first)
    distinct_second = len(second)

    for outgoing_first in first:
        for outgoing_second in second:
            if outgoing_first == outgoing_second:
                if distinct_first == distinct_second:
                    return True
                continue

            after_first = distinct_first - (first[outgoing_first] == 1) + (outgoing_second not in first)
            after_second = distinct_second - (second[outgoing_second] == 1) + (outgoing_first not in second)
            if after_first == after_second:
                return True

    return False
