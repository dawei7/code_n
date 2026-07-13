"""Length-ordered word-break DP for LeetCode 472."""


def solve(words: list[str]) -> list[str]:
    building_blocks: set[str] = set()
    concatenated: list[str] = []

    for word in sorted(words, key=len):
        if not word:
            continue
        reachable = [False] * (len(word) + 1)
        reachable[0] = True
        for start in range(len(word)):
            if not reachable[start]:
                continue
            for end in range(start + 1, len(word) + 1):
                if word[start:end] in building_blocks:
                    reachable[end] = True
        if reachable[-1]:
            concatenated.append(word)
        building_blocks.add(word)
    return concatenated
