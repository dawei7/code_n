def solve(column_number: int) -> str:
    title: list[str] = []
    while column_number > 0:
        column_number, remainder = divmod(column_number - 1, 26)
        title.append(chr(ord("A") + remainder))
    return "".join(reversed(title))
