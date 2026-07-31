def solve(tasks: list[list[int]]) -> int:
    tasks.sort(key=lambda task: task[1] - task[0], reverse=True)
    initial = 0
    energy = 0

    for actual, minimum in tasks:
        if energy < minimum:
            initial += minimum - energy
            energy = minimum
        energy -= actual

    return initial
