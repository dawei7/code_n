from collections import defaultdict


def solve(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    unvisited = set(wordList)
    if endWord not in unvisited:
        return []

    parents: dict[str, list[str]] = defaultdict(list)
    current_level = {beginWord}
    while current_level and endWord not in current_level:
        unvisited.difference_update(current_level)
        next_level: set[str] = set()
        for word in current_level:
            for index, original in enumerate(word):
                for replacement in "abcdefghijklmnopqrstuvwxyz":
                    if replacement == original:
                        continue
                    candidate = word[:index] + replacement + word[index + 1:]
                    if candidate not in unvisited:
                        continue
                    parents[candidate].append(word)
                    next_level.add(candidate)
        current_level = next_level

    if endWord not in current_level:
        return []

    result: list[list[str]] = []
    reverse_path = [endWord]

    def build(word: str) -> None:
        if word == beginWord:
            result.append(reverse_path[::-1])
            return
        for parent in parents[word]:
            reverse_path.append(parent)
            build(parent)
            reverse_path.pop()

    build(endWord)
    return result
