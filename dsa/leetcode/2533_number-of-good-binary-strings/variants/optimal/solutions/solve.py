def solve(minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
    modulus = 1_000_000_007
    ways = [0] * (maxLength + 1)
    ways[0] = 1
    answer = 0

    for length in range(1, maxLength + 1):
        if length >= oneGroup:
            ways[length] += ways[length - oneGroup]
        if length >= zeroGroup:
            ways[length] += ways[length - zeroGroup]
        ways[length] %= modulus

        if length >= minLength:
            answer = (answer + ways[length]) % modulus

    return answer
