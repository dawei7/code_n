def solve(s: str) -> str:
    vowels = set("aeiou")
    words = s.split()
    target = sum((character in vowels for character in words[0]))
    for index in range(1, len(words)):
        if sum((character in vowels for character in words[index])) == target:
            words[index] = words[index][::-1]
    return " ".join(words)
