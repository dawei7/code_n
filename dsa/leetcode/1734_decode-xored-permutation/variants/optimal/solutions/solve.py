def solve(encoded: list[int]) -> list[int]:
    n = len(encoded) + 1
    first = 0
    for value in range(1, n + 1):
        first ^= value
    for index in range(1, len(encoded), 2):
        first ^= encoded[index]

    permutation = [first]
    for value in encoded:
        permutation.append(permutation[-1] ^ value)
    return permutation
