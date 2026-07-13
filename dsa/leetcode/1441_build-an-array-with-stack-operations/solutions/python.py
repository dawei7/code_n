def solve(target, n):
    result = []
    current = 1
    for value in target:
        while current < value and current <= n:
            result.extend(["Push", "Pop"])
            current += 1
        if current <= n:
            result.append("Push")
            current += 1
    return result
