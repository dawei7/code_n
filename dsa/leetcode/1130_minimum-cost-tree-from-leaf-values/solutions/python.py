def solve(arr):
    stack = [float("inf")]
    total = 0
    for value in arr:
        while stack[-1] <= value:
            mid = stack.pop()
            total += mid * min(stack[-1], value)
        stack.append(value)
    while len(stack) > 2:
        total += stack.pop() * stack[-1]
    return total
