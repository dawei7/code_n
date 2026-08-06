from collections import Counter


def solve(s: str) -> list[str]:
    counts = Counter(s)
    odd = [character for character, count in counts.items() if count % 2]
    if len(odd) > 1:
        return []

    center = odd[0] if odd else ""
    half_counts = {character: count // 2 for character, count in counts.items() if count >= 2}
    characters = sorted(half_counts)
    half_length = sum(half_counts.values())
    path: list[str] = []
    palindromes: list[str] = []

    def generate() -> None:
        if len(path) == half_length:
            left = "".join(path)
            palindromes.append(left + center + left[::-1])
            return
        for character in characters:
            if half_counts[character] == 0:
                continue
            half_counts[character] -= 1
            path.append(character)
            generate()
            path.pop()
            half_counts[character] += 1

    generate()
    return palindromes
