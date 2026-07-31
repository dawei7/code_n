def solve(s: str) -> str:
    words = (
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    )
    converted = []
    index = 0
    while index < len(s):
        for word, digit in words:
            if s.startswith(word, index):
                converted.append(digit)
                index += len(word)
                break
        else:
            index += 1
    return "".join(converted)
