


def solve():
    def largestRectangleArea(N: int, A: list[int]) -> int:
        stack = []
        max_area = 0
        i = 0

        while i < N:
            if not stack or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = A[tp] * width
                if area > max_area:
                    max_area = area

        while stack:
            tp = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = A[tp] * width
            if area > max_area:
                max_area = area

        return max_area


if __name__ == "__main__":
    solve()
