MOD = 1_000_000_007
ALPHABET_SIZE = 26


def _multiply_matrices(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    product = [[0] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
    for source in range(ALPHABET_SIZE):
        product_row = product[source]
        for middle, left_value in enumerate(left[source]):
            if left_value == 0:
                continue
            for destination, right_value in enumerate(right[middle]):
                product_row[destination] = (
                    product_row[destination] + left_value * right_value
                ) % MOD
    return product


def _multiply_vector(vector: list[int], matrix: list[list[int]]) -> list[int]:
    product = [0] * ALPHABET_SIZE
    for source, count in enumerate(vector):
        if count == 0:
            continue
        for destination, ways in enumerate(matrix[source]):
            product[destination] = (product[destination] + count * ways) % MOD
    return product


def solve(s: str, t: int, nums: list[int]) -> int:
    transition = [[0] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
    for source, length in enumerate(nums):
        for shift in range(1, length + 1):
            transition[source][(source + shift) % ALPHABET_SIZE] = 1

    counts = [0] * ALPHABET_SIZE
    for char in s:
        counts[ord(char) - ord("a")] += 1

    while t > 0:
        if t & 1:
            counts = _multiply_vector(counts, transition)
        transition = _multiply_matrices(transition, transition)
        t >>= 1

    return sum(counts) % MOD
