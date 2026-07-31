def solve(instructions: list[str], values: list[int]) -> int:
    score = 0
    index = 0
    visited: set[int] = set()

    while 0 <= index < len(instructions) and index not in visited:
        visited.add(index)
        if instructions[index] == "add":
            score += values[index]
            index += 1
        else:
            index += values[index]

    return score
