def solve(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    prefix = [0] * len(goal)
    matched = 0
    for index in range(1, len(goal)):
        while matched and goal[index] != goal[matched]:
            matched = prefix[matched - 1]
        if goal[index] == goal[matched]:
            matched += 1
            prefix[index] = matched

    matched = 0
    for char in s + s:
        while matched and char != goal[matched]:
            matched = prefix[matched - 1]
        if char == goal[matched]:
            matched += 1
            if matched == len(goal):
                return True
    return False
