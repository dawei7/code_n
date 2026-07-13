from collections import deque


def solve(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1
    queue = deque(course for course in range(num_courses) if indegree[course] == 0)
    order: list[int] = []
    while queue:
        prerequisite = queue.popleft()
        order.append(prerequisite)
        for course in graph[prerequisite]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append(course)
    return order if len(order) == num_courses else []
