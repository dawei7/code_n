from math import isqrt


def solve(n: int, edges: list[list[int]], nums: list[int]) -> int:
    limit = max(nums)
    root = isqrt(limit)
    is_prime = bytearray(b"\x01") * (root + 1)
    is_prime[:2] = b"\x00\x00"

    for prime in range(2, isqrt(root) + 1):
        if is_prime[prime]:
            start = prime * prime
            is_prime[start::prime] = b"\x00" * (((root - start) // prime) + 1)

    primes = [value for value in range(2, root + 1) if is_prime[value]]
    kernel = list(range(limit + 1))

    for prime in primes:
        square = prime * prime
        power = square
        while power <= limit:
            kernel[power::power] = [
                value // square for value in kernel[power::power]
            ]
            power *= square

    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    active: dict[int, int] = {}
    answer = 0
    stack = [(0, -1, True)]

    while stack:
        node, parent, entering = stack.pop()
        key = kernel[nums[node]]

        if entering:
            answer += active.get(key, 0)
            active[key] = active.get(key, 0) + 1
            stack.append((node, parent, False))
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, True))
        else:
            active[key] -= 1

    return answer
