from collections import deque


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque(
            course
            for course in range(numCourses)
            if indegree[course] == 0
        )
        order = []

        while queue:
            prerequisite = queue.popleft()
            order.append(prerequisite)
            for course in graph[prerequisite]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        reachable = [set() for _ in range(numCourses)]
        for prerequisite in reversed(order):
            for course in graph[prerequisite]:
                reachable[prerequisite].add(course)
                reachable[prerequisite].update(reachable[course])

        return [
            course in reachable[prerequisite]
            for prerequisite, course in queries
        ]
