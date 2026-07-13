def solve(column_title: str) -> int:
    total = 0
    for character in column_title:
        total = total * 26 + ord(character) - ord("A") + 1
    return total
