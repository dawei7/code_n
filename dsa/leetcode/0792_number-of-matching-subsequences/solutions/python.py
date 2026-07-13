from collections import defaultdict


def solve(s: str, words: list[str]) -> int:
    waiting: dict[str, list[object]] = defaultdict(list)
    for word in words:
        iterator = iter(word)
        waiting[next(iterator)].append(iterator)

    matched = 0
    for character in s:
        advancing = waiting.pop(character, [])
        for iterator in advancing:
            next_character = next(iterator, None)
            if next_character is None:
                matched += 1
            else:
                waiting[next_character].append(iterator)
    return matched
