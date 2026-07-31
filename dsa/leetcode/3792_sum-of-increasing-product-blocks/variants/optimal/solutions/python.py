def solve(n: int) -> int:
    modulo = 1_000_000_007
    next_value = 1
    total = 0

    for block_length in range(1, n + 1):
        block_product = 1
        for _ in range(block_length):
            block_product = block_product * next_value % modulo
            next_value += 1
        total = (total + block_product) % modulo

    return total
