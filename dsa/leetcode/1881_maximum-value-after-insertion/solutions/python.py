def solve(n: str, x: int) -> str:
    digit = str(x)
    if n[0] == "-":
        for index in range(1, len(n)):
            if n[index] > digit:
                return n[:index] + digit + n[index:]
    else:
        for index, current in enumerate(n):
            if current < digit:
                return n[:index] + digit + n[index:]
    return n + digit
