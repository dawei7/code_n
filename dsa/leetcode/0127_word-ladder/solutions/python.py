from collections import deque


def solve(begin_word: str, end_word: str, word_list: list[str]) -> int:
    unvisited = set(word_list)
    if end_word not in unvisited:
        return 0
    queue = deque([(begin_word, 1)])
    unvisited.discard(begin_word)
    while queue:
        word, length = queue.popleft()
        for index, original in enumerate(word):
            for replacement in "abcdefghijklmnopqrstuvwxyz":
                if replacement == original:
                    continue
                candidate = word[:index] + replacement + word[index + 1:]
                if candidate not in unvisited:
                    continue
                if candidate == end_word:
                    return length + 1
                unvisited.remove(candidate)
                queue.append((candidate, length + 1))
    return 0
