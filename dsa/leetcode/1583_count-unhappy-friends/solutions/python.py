def solve(n: int, preferences: list[list[int]], pairs: list[list[int]]) -> int:
    rank = [[0] * n for _ in range(n)]
    for friend in range(n):
        for position, other in enumerate(preferences[friend]):
            rank[friend][other] = position

    partner = [0] * n
    for left, right in pairs:
        partner[left] = right
        partner[right] = left

    unhappy = 0
    for friend in range(n):
        current = partner[friend]
        for preferred in preferences[friend]:
            if preferred == current:
                break
            if rank[preferred][friend] < rank[preferred][partner[preferred]]:
                unhappy += 1
                break
    return unhappy
