def solve(tasks: list[list[int]]) -> int:
    ordered = sorted(tasks, key=lambda task: task[1] - task[0], reverse=True)
    initial = 0
    energy = 0

    for actual, minimum in ordered:
        if energy < minimum:
            initial += minimum - energy
            energy = minimum
        energy -= actual

    return initial
