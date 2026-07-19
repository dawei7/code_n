def solve(heights: list[int]) -> list[int]:
    answer = [0] * len(heights)
    stack: list[int] = []

    for index in range(len(heights) - 1, -1, -1):
        while stack and heights[index] > stack[-1]:
            stack.pop()
            answer[index] += 1

        if stack:
            answer[index] += 1

        stack.append(heights[index])

    return answer
