import heapq


class TaskManager:
    def __init__(self, tasks):
        self.tasks = {}
        self.heap = []
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, userId, taskId, priority):
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId, newPriority):
        user_id, _ = self.tasks[taskId]
        self.tasks[taskId] = (user_id, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId):
        del self.tasks[taskId]

    def execTop(self):
        while self.heap:
            negative_priority, negative_task_id = heapq.heappop(self.heap)
            task_id = -negative_task_id
            priority = -negative_priority
            current = self.tasks.get(task_id)
            if current is not None and current[1] == priority:
                del self.tasks[task_id]
                return current[0]
        return -1


def solve(operations, arguments):
    manager = None
    output = []

    for operation, values in zip(operations, arguments):
        if operation == "TaskManager":
            manager = TaskManager(*values)
            output.append(None)
        elif operation == "add":
            output.append(manager.add(*values))
        elif operation == "edit":
            output.append(manager.edit(*values))
        elif operation == "rmv":
            output.append(manager.rmv(*values))
        else:
            output.append(manager.execTop())

    return output
