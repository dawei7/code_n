def solve(columnNumber: int) -> str:
    title: list[str] = []
    while columnNumber > 0:
        columnNumber, remainder = divmod(columnNumber - 1, 26)
        title.append(chr(ord("A") + remainder))
    return "".join(reversed(title))
