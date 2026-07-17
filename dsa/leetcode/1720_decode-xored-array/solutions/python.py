def solve(encoded: list[int], first: int) -> list[int]:
    decoded = [first]
    for value in encoded:
        decoded.append(decoded[-1] ^ value)
    return decoded
