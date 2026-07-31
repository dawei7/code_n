def solve(words: list[str]) -> str:
    def difference(word: str) -> tuple[int, ...]:
        return tuple(
            ord(word[index + 1]) - ord(word[index])
            for index in range(len(word) - 1)
        )

    first = difference(words[0])
    second = difference(words[1])
    third = difference(words[2])
    common = first if first == second or first == third else second

    for word in words:
        if difference(word) != common:
            return word

    return ""
