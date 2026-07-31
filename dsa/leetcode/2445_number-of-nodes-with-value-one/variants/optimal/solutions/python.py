def solve(n: int, queries: list[int]) -> int:
    parity = [0] * (n + 1)
    for node in queries:
        parity[node] ^= 1

    answer = 0
    for node in range(1, n + 1):
        if node > 1:
            parity[node] ^= parity[node // 2]
        answer += parity[node]

    return answer
