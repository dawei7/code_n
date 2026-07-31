class TodoList:
    def __init__(self):
        self.next_task_id = 1
        self.tasks = {}

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        task_id = self.next_task_id
        self.next_task_id += 1
        self.tasks[task_id] = [userId, taskDescription, dueDate, set(tags), False]
        return task_id

    def getAllTasks(self, userId: int) -> List[str]:
        pending = [task for task in self.tasks.values() if task[0] == userId and not task[4]]
        pending.sort(key=lambda task: task[2])
        return [task[1] for task in pending]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        pending = [task for task in self.tasks.values() if task[0] == userId and not task[4] and tag in task[3]]
        pending.sort(key=lambda task: task[2])
        return [task[1] for task in pending]

    def completeTask(self, userId: int, taskId: int) -> None:
        task = self.tasks.get(taskId)
        if task is not None and task[0] == userId and not task[4]:
            task[4] = True
