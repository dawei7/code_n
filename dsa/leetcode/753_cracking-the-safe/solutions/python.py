def solve(n: int, k: int) -> str:
    modulus = k ** (n - 1)
    next_digit = [0] * modulus
    stack: list[tuple[int, int]] = [(0, -1)]
    digits: list[str] = []

    while stack:
        vertex, incoming_digit = stack[-1]
        digit = next_digit[vertex]
        if digit < k:
            next_digit[vertex] += 1
            next_vertex = (vertex * k + digit) % modulus
            stack.append((next_vertex, digit))
        else:
            stack.pop()
            if incoming_digit >= 0:
                digits.append(str(incoming_digit))

    return "".join(digits) + "0" * (n - 1)
