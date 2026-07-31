def solve(n: int, knows_matrix: list[list[bool]]) -> int:
    def knows(first: int, second: int) -> bool:
        return knows_matrix[first][second]

    candidate = 0
    for person in range(1, n):
        if knows(candidate, person):
            candidate = person
    for person in range(n):
        if person == candidate:
            continue
        if knows(candidate, person) or not knows(person, candidate):
            return -1
    return candidate
