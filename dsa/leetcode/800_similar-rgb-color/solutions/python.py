def solve(color: str) -> str:
    result = ["#"]
    for start in (1, 3, 5):
        value = int(color[start : start + 2], 16)
        digit = format((value + 8) // 17, "x")
        result.append(digit * 2)
    return "".join(result)
