def solve(target):
    if not target:
        return 0
    total = max(0, target[0])
    for i in range(1, len(target)):
        if target[i] > target[i - 1]:
            total += target[i] - target[i - 1]
    return total
