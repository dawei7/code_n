def solve(digits: str) -> list[str]:
    if not digits:
        return []

    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result: list[str] = []
    path: list[str] = []

    def build(i: int) -> None:
        if i == len(digits):
            result.append("".join(path))
            return

        for letter in letters[digits[i]]:
            path.append(letter)
            build(i + 1)
            path.pop()

    build(0)
    return result
