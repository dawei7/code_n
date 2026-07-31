def solve(s: str) -> int:
    counts = [0] * 26
    for char in s:
        counts[ord(char) - ord("a")] += 1

    vowels = {0, 4, 8, 14, 20}
    max_vowel = max(counts[index] for index in vowels)
    max_consonant = max(
        counts[index] for index in range(26) if index not in vowels
    )
    return max_vowel + max_consonant
