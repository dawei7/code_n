def solve(
    sentence1: list[str],
    sentence2: list[str],
    similarPairs: list[list[str]],
) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    direct = set()
    for left, right in similarPairs:
        direct.add((left, right))
        direct.add((right, left))

    return all(
        first == second or (first, second) in direct
        for first, second in zip(sentence1, sentence2)
    )
