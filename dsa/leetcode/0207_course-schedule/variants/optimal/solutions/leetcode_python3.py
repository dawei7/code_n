from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        completed = 0
        while queue:
            prerequisite = queue.popleft()
            completed += 1
            for course in graph[prerequisite]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        return completed == numCourses
