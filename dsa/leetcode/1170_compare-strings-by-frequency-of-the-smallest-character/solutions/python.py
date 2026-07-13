from bisect import bisect_right


def _frequency(word):
    smallest = min(word)
    return word.count(smallest)


def solve(queries, words):
    word_scores = sorted(_frequency(word) for word in words)
    n = len(word_scores)
    return [n - bisect_right(word_scores, _frequency(query)) for query in queries]
