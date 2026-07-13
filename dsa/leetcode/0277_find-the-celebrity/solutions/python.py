def solve(n: int, knows_matrix: list[list[bool]]) -> int:
    candidate = 0
    for person in range(1, n):
        if knows_matrix[candidate][person]:
            candidate = person
    for person in range(n):
        if person == candidate:
            continue
        if knows_matrix[candidate][person] or not knows_matrix[person][candidate]:
            return -1
    return candidate
