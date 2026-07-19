"""Optimal app-local solution for LeetCode 907."""


def solve(arr):
    modulus = 1_000_000_007
    stack = []
    total = 0

    for right in range(len(arr) + 1):
        current = arr[right] if right < len(arr) else -1
        while stack and arr[stack[-1]] >= current:
            middle = stack.pop()
            left = stack[-1] if stack else -1
            total += arr[middle] * (middle - left) * (right - middle)
        stack.append(right)

    return total % modulus
