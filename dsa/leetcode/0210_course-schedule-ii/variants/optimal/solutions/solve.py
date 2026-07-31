from collections import deque


def solve(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1
    queue = deque(course for course in range(numCourses) if indegree[course] == 0)
    order: list[int] = []
    while queue:
        prerequisite = queue.popleft()
        order.append(prerequisite)
        for course in graph[prerequisite]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append(course)
    return order if len(order) == numCourses else []
