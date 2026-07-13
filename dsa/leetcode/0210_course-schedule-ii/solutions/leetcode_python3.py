from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        order = []
        while queue:
            prerequisite = queue.popleft()
            order.append(prerequisite)
            for course in graph[prerequisite]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return order if len(order) == numCourses else []
