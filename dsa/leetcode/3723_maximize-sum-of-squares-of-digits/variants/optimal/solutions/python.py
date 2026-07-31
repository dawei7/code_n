def solve(num: int, sum: int) -> str:
    if sum > 9 * num:
        return ""

    nines, remainder = divmod(sum, 9)
    return (
        "9" * nines
        + (str(remainder) if remainder else "")
        + "0" * (num - nines - (remainder > 0))
    )
