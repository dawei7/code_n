"""Optimal app-local solution for LeetCode 937."""


def solve(logs):
    letters = []
    digits = []
    for log in logs:
        identifier, content = log.split(" ", 1)
        if content[0].isdigit():
            digits.append(log)
        else:
            letters.append((content, identifier, log))
    letters.sort(key=lambda record: (record[0], record[1]))
    return [record[2] for record in letters] + digits
