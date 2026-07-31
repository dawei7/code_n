def solve(date: str) -> str:
    return "-".join(format(int(part), "b") for part in date.split("-"))
