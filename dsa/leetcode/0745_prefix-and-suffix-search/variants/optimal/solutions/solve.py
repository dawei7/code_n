class WordFilter:
    def __init__(self, words: list[str]):
        self.lookup = {}
        for index, word in enumerate(words):
            for prefix_end in range(len(word) + 1):
                prefix = word[:prefix_end]
                for suffix_start in range(len(word) + 1):
                    self.lookup[(prefix, word[suffix_start:])] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get((pref, suff), -1)


def solve(operations: list[str], arguments: list[list]) -> list[int | None]:
    word_filter = None
    results = []
    for operation, args in zip(operations, arguments):
        if operation == "WordFilter":
            word_filter = WordFilter(args[0])
            results.append(None)
        elif operation == "f":
            results.append(word_filter.f(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return results
