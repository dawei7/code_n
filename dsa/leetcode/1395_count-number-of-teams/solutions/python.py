"""Optimal solution for LeetCode 1395: Count Number of Teams."""


def solve(rating: list[int]) -> int:
    total = 0
    n = len(rating)
    for mid in range(n):
        left_less = left_greater = right_less = right_greater = 0
        for i in range(mid):
            if rating[i] < rating[mid]:
                left_less += 1
            else:
                left_greater += 1
        for i in range(mid + 1, n):
            if rating[i] < rating[mid]:
                right_less += 1
            else:
                right_greater += 1
        total += left_less * right_greater + left_greater * right_less
    return total
