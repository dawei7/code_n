def solve(sentence: str) -> str:
    vowels = frozenset("aeiouAEIOU")
    converted: list[str] = []

    for index, word in enumerate(sentence.split(), start=1):
        base = word if word[0] in vowels else word[1:] + word[0]
        converted.append(base + "ma" + "a" * index)

    return " ".join(converted)
