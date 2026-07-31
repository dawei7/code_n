from typing import List


def solve(m: int, n: int, head) -> List[List[int]]:
    matrix = [[-1] * n for _ in range(m)]
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while head is not None and top <= bottom and left <= right:
        for column in range(left, right + 1):
            if head is None:
                return matrix
            matrix[top][column] = head.val
            head = head.next
        top += 1

        for row in range(top, bottom + 1):
            if head is None:
                return matrix
            matrix[row][right] = head.val
            head = head.next
        right -= 1

        if top <= bottom:
            for column in range(right, left - 1, -1):
                if head is None:
                    return matrix
                matrix[bottom][column] = head.val
                head = head.next
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                if head is None:
                    return matrix
                matrix[row][left] = head.val
                head = head.next
            left += 1

    return matrix
