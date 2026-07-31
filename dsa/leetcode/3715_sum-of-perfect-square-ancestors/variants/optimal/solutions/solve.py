def solve(n: int, edges: list[list[int]], nums: list[int]) -> int:
    limit = max(nums)
    smallest_prime = [0] * (limit + 1)

    for prime in range(2, limit + 1):
        if smallest_prime[prime] != 0:
            continue
        smallest_prime[prime] = prime
        if prime * prime <= limit:
            for multiple in range(prime * prime, limit + 1, prime):
                if smallest_prime[multiple] == 0:
                    smallest_prime[multiple] = prime

    kernel = [1] * (limit + 1)
    for value in range(2, limit + 1):
        prime = smallest_prime[value]
        quotient = value // prime
        if quotient % prime == 0:
            kernel[value] = kernel[quotient // prime]
        else:
            kernel[value] = kernel[quotient] * prime

    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    active = {}
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
