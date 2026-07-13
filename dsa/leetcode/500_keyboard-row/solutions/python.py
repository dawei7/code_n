"""Single-pass keyboard-row filtering for LeetCode 500."""


ROW_BY_LETTER = {
    letter: row_index
    for row_index, row in enumerate(("qwertyuiop", "asdfghjkl", "zxcvbnm"))
    for letter in row
}


def solve(words: list[str]) -> list[str]:
    answer: list[str] = []
    for word in words:
        lowered = word.lower()
        row = ROW_BY_LETTER[lowered[0]]
        if all(ROW_BY_LETTER[letter] == row for letter in lowered):
            answer.append(word)
    return answer
