def solve(heights: list[list[int]]) -> list[list[int]]:
    rows = len(heights)
    columns = len(heights[0])
    answer = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        stack: list[int] = []
        for column in range(columns - 1, -1, -1):
            height = heights[row][column]
            while stack and stack[-1] < height:
                stack.pop()
                answer[row][column] += 1
            if stack:
                answer[row][column] += 1
                if stack[-1] == height:
                    stack.pop()
            stack.append(height)

    for column in range(columns):
        stack = []
        for row in range(rows - 1, -1, -1):
            height = heights[row][column]
            while stack and stack[-1] < height:
                stack.pop()
                answer[row][column] += 1
            if stack:
                answer[row][column] += 1
                if stack[-1] == height:
                    stack.pop()
            stack.append(height)

    return answer
