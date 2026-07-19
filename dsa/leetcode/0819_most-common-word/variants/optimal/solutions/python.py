def solve(paragraph: str, banned: list[str]) -> str:
    banned_words = set(banned)
    frequencies: dict[str, int] = {}
    letters: list[str] = []
    most_common = ""
    highest_frequency = 0

    for character in paragraph.lower() + " ":
        if character.isalpha():
            letters.append(character)
            continue
        if not letters:
            continue

        word = "".join(letters)
        letters.clear()
        if word in banned_words:
            continue

        frequency = frequencies.get(word, 0) + 1
        frequencies[word] = frequency
        if frequency > highest_frequency:
            most_common = word
            highest_frequency = frequency

    return most_common
