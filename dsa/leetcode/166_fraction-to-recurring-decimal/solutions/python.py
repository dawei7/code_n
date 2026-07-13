def solve(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    negative = (numerator < 0) != (denominator < 0)
    numerator = abs(numerator)
    denominator = abs(denominator)
    integer, remainder = divmod(numerator, denominator)
    prefix = ("-" if negative else "") + str(integer)
    if remainder == 0:
        return prefix

    digits: list[str] = []
    positions: dict[int, int] = {}
    while remainder != 0:
        if remainder in positions:
            start = positions[remainder]
            digits.insert(start, "(")
            digits.append(")")
            break
        positions[remainder] = len(digits)
        digit, remainder = divmod(remainder * 10, denominator)
        digits.append(str(digit))
    return prefix + "." + "".join(digits)
