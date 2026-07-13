def solve(heights: list[int]) -> int:
    stack: list[tuple[int, int]] = []
    best = 0
    for index, height in enumerate(heights + [0]):
        start = index
        while stack and stack[-1][1] > height:
            start, previous_height = stack.pop()
            best = max(best, previous_height * (index - start))
        stack.append((start, height))
    return best
