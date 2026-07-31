def solve(s: str) -> str:
    letters = [character for character in s if character.isalpha()]
    special_characters = [character for character in s if not character.isalpha()]

    return "".join(letters.pop() if character.isalpha() else special_characters.pop() for character in s)
