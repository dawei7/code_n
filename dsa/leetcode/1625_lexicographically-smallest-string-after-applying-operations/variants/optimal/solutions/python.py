def solve(s: str, a: int, b: int) -> str:
    smallest = s
    seen = {s}
    stack = [s]
    while stack:
        current = stack.pop()
        smallest = min(smallest, current)

        digits = list(current)
        for index in range(1, len(digits), 2):
            digits[index] = str((int(digits[index]) + a) % 10)
        added = "".join(digits)
        if added not in seen:
            seen.add(added)
            stack.append(added)

        rotated = current[-b:] + current[:-b]
        if rotated not in seen:
            seen.add(rotated)
            stack.append(rotated)
    return smallest
