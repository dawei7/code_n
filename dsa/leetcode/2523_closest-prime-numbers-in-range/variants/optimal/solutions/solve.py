from math import isqrt


def solve(left: int, right: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (right + 1)
    is_prime[0] = 0
    if right >= 1:
        is_prime[1] = 0

    for prime in range(2, isqrt(right) + 1):
        if is_prime[prime]:
            start = prime * prime
            count = (right - start) // prime + 1
            is_prime[start : right + 1 : prime] = b"\x00" * count

    answer = [-1, -1]
    previous = -1

    for value in range(max(2, left), right + 1):
        if not is_prime[value]:
            continue
        if previous != -1 and (answer[0] == -1 or value - previous < answer[1] - answer[0]):
            answer = [previous, value]
        previous = value

    return answer
