def solve(heights: list[int]) -> int:
    stack: list[tuple[int, int]] = []
    best = 0
    for i, height in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > height:
            start, previous_height = stack.pop()
            best = max(best, previous_height * (i - start))
        stack.append((start, height))
    return best
