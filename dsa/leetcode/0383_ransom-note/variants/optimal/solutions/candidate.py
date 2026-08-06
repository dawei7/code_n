def solve(ransomNote: str, magazine: str) -> bool:
    available = [0] * 26
    base = ord("a")

    for character in magazine:
        available[ord(character) - base] += 1

    for character in ransomNote:
        i = ord(character) - base
        if available[i] == 0:
            return False
        available[i] -= 1

    return True
