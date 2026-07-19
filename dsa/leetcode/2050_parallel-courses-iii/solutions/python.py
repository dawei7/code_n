from collections import deque


def solve(n: int, relations: list[list[int]], time: list[int]) -> int:
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for prerequisite, course in relations:
        prerequisite -= 1
        course -= 1
        graph[prerequisite].append(course)
        indegree[course] += 1

    finish = time.copy()
    queue = deque(course for course in range(n) if indegree[course] == 0)

    while queue:
        course = queue.popleft()
        for next_course in graph[course]:
            finish[next_course] = max(
                finish[next_course],
                finish[course] + time[next_course],
            )
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return max(finish)
