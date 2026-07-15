"""Optimal app-local solution for LeetCode 923."""


def solve(arr, target):
    modulus = 1_000_000_007
    counts = [0] * 101
    for value in arr:
        counts[value] += 1

    answer = 0
    for first in range(101):
        for second in range(first, 101):
            third = target - first - second
            if third < second or third > 100:
                continue

            if first == second == third:
                count = counts[first]
                answer += count * (count - 1) * (count - 2) // 6
            elif first == second:
                answer += counts[first] * (counts[first] - 1) // 2 * counts[third]
            elif second == third:
                answer += counts[first] * counts[second] * (counts[second] - 1) // 2
            else:
                answer += counts[first] * counts[second] * counts[third]

    return answer % modulus

