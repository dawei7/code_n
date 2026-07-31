import heapq
from typing import List


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.heap = []
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        user_id, _ = self.tasks[taskId]
        self.tasks[taskId] = (user_id, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            negative_priority, negative_task_id = heapq.heappop(self.heap)
            task_id = -negative_task_id
            priority = -negative_priority
            current = self.tasks.get(task_id)
            if current is not None and current[1] == priority:
                del self.tasks[task_id]
                return current[0]
        return -1
