def solve(words: list[str]) -> list[str]:
    row_by_letter = {
        letter: row_index for row_index, row in enumerate(("qwertyuiop", "asdfghjkl", "zxcvbnm")) for letter in row
    }
    answer = []
    for word in words:
        lowered = word.lower()
        row = row_by_letter[lowered[0]]
        if all(row_by_letter[letter] == row for letter in lowered):
            answer.append(word)
    return answer
