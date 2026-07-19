def solve(sentence1: str, sentence2: str) -> bool:
    first = sentence1.split()
    second = sentence2.split()
    if len(first) > len(second):
        first, second = second, first

    prefix = 0
    while prefix < len(first) and first[prefix] == second[prefix]:
        prefix += 1

    suffix = 0
    while (
        suffix < len(first) - prefix
        and first[-1 - suffix] == second[-1 - suffix]
    ):
        suffix += 1

    return prefix + suffix == len(first)
