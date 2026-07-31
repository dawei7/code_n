def solve(s: str) -> int:
    vowels = 0
    consonants = 0

    for char in s:
        if char in "aeiou":
            vowels += 1
        elif "a" <= char <= "z":
            consonants += 1

    return vowels // consonants if consonants else 0
