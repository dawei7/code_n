"""Optimal app-local solution for LeetCode 444."""

from collections import deque


def solve(nums: list[int], sequences: list[list[int]]) -> bool:
    graph = {value: set() for value in nums}
    indegree = {value: 0 for value in nums}
    observed = set()

    for sequence in sequences:
        for value in sequence:
            if value not in graph:
                return False
            observed.add(value)
        for left, right in zip(sequence, sequence[1:]):
            if right not in graph[left]:
                graph[left].add(right)
                indegree[right] += 1

    if len(observed) != len(nums):
        return False

    available = deque(value for value in nums if indegree[value] == 0)
    for expected in nums:
        if len(available) != 1 or available.popleft() != expected:
            return False
        for neighbor in graph[expected]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                available.append(neighbor)
    return True
