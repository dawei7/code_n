def solve(s: str) -> str:
    candidates = {
        "z": (("zero", "0"),),
        "o": (("one", "1"),),
        "t": (("two", "2"), ("three", "3")),
        "f": (("four", "4"), ("five", "5")),
        "s": (("six", "6"), ("seven", "7")),
        "e": (("eight", "8"),),
        "n": (("nine", "9"),),
    }
    result = []
    cursor = 0
    while cursor < len(s):
        matched = False
        for word, digit in candidates.get(s[cursor], ()):
            if s.startswith(word, cursor):
                result.append(digit)
                cursor += len(word)
                matched = True
                break
        if not matched:
            cursor += 1
    return "".join(result)
