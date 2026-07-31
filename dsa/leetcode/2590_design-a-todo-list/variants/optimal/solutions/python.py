class TodoList:
    def __init__(self):
        self.next_task_id = 1
        self.tasks = {}

    def addTask(
        self,
        userId: int,
        taskDescription: str,
        dueDate: int,
        tags: list[str],
    ) -> int:
        task_id = self.next_task_id
        self.next_task_id += 1
        self.tasks[task_id] = [userId, taskDescription, dueDate, set(tags), False]
        return task_id

    def getAllTasks(self, userId: int) -> list[str]:
        pending = [
            task for task in self.tasks.values()
            if task[0] == userId and not task[4]
        ]
        pending.sort(key=lambda task: task[2])
        return [task[1] for task in pending]

    def getTasksForTag(self, userId: int, tag: str) -> list[str]:
        pending = [
            task for task in self.tasks.values()
            if task[0] == userId and not task[4] and tag in task[3]
        ]
        pending.sort(key=lambda task: task[2])
        return [task[1] for task in pending]

    def completeTask(self, userId: int, taskId: int) -> None:
        task = self.tasks.get(taskId)
        if task is not None and task[0] == userId and not task[4]:
            task[4] = True


def solve(commands: list[str], inputs: list[list[object]]) -> list[object]:
    todo = None
    results = []

    for command, arguments in zip(commands, inputs):
        if command == "TodoList":
            todo = TodoList()
            results.append(None)
        elif command == "addTask":
            results.append(todo.addTask(*arguments))
        elif command == "getAllTasks":
            results.append(todo.getAllTasks(*arguments))
        elif command == "getTasksForTag":
            results.append(todo.getTasksForTag(*arguments))
        else:
            todo.completeTask(*arguments)
            results.append(None)

    return results
