from collections import deque


def solve(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1
    queue = deque(course for course in range(num_courses) if indegree[course] == 0)
    completed = 0
    while queue:
        prerequisite = queue.popleft()
        completed += 1
        for course in graph[prerequisite]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append(course)
    return completed == num_courses
