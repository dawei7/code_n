def solve(logs: list[list[int]]) -> int:
    changes = [0] * 101
    for birth, death in logs:
        changes[birth - 1950] += 1
        changes[death - 1950] -= 1

    population = 0
    largest = 0
    answer = 1950
    for offset, change in enumerate(changes):
        population += change
        if population > largest:
            largest = population
            answer = 1950 + offset

    return answer
