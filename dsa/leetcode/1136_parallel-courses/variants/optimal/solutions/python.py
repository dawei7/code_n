"""Optimal app-local solution for LeetCode 1136."""

from collections import deque


def solve(n: int, relations: list[list[int]]) -> int:
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for prerequisite, course in relations:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque(course for course in range(1, n + 1) if indegree[course] == 0)
    completed = 0
    semesters = 0
    while queue:
        semesters += 1
        for _ in range(len(queue)):
            course = queue.popleft()
            completed += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
    return semesters if completed == n else -1
