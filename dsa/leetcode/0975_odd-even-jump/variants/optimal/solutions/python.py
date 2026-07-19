"""Optimal app-local solution for LeetCode 975."""


def solve(arr):
    n = len(arr)

    def destinations(order):
        result = [-1] * n
        stack = []
        for index in order:
            while stack and stack[-1] < index:
                result[stack.pop()] = index
            stack.append(index)
        return result

    higher = destinations(sorted(range(n), key=lambda i: (arr[i], i)))
    lower = destinations(sorted(range(n), key=lambda i: (-arr[i], i)))

    odd = [False] * n
    even = [False] * n
    odd[-1] = True
    even[-1] = True

    for i in range(n - 2, -1, -1):
        if higher[i] != -1:
            odd[i] = even[higher[i]]
        if lower[i] != -1:
            even[i] = odd[lower[i]]

    return sum(odd)
