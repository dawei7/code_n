def solve(n):
    modulus = 1_000_000_007
    count = 1

    for orders in range(1, n + 1):
        count = count * orders * (2 * orders - 1) % modulus

    return count
