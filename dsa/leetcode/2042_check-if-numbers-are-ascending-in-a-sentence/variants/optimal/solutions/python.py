def solve(s: str) -> bool:
    previous = 0

    for token in s.split():
        if token.isdigit():
            current = int(token)
            if current <= previous:
                return False
            previous = current

    return True
