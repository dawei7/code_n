MORSE = (
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..",
)


def solve(words: list[str]) -> int:
    transformations = {
        "".join(MORSE[ord(char) - ord("a")] for char in word)
        for word in words
    }
    return len(transformations)
