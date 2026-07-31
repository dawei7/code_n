def solve(n: int, k: int) -> list[int]:
    visited = [False] * n
    current = 0
    turn = 1
    while not visited[current]:
        visited[current] = True
        current = (current + turn * k) % n
        turn += 1
    return [index + 1 for index, received in enumerate(visited) if not received]
