def solve(words: list[str], separator: str) -> list[str]:
    result = []

    for word in words:
        for part in word.split(separator):
            if part:
                result.append(part)

    return result
