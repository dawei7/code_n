def solve(s: str) -> str:
    def vowel_count(word: str) -> int:
        return sum(word.count(vowel) for vowel in "aeiou")

    words = s.split(" ")
    target_count = vowel_count(words[0])
    transformed = [words[0]]

    for word in words[1:]:
        transformed.append(word[::-1] if vowel_count(word) == target_count else word)

    return " ".join(transformed)
