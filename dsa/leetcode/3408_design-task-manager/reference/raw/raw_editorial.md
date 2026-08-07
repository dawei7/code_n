### Approach: Priority Queue + Hash Table

#### Intuition

We begin by using a hash table $\textit{taskInfo}$ to store the latest information for each task, including its priority and $\textit{userId}$, and we also insert this information into the max heap $\textit{heap}$ so that the highest-priority task can be retrieved efficiently. In languages without native support for a max heap, we can instead simulate one using a min heap with negative values.

When a new task is added, we record its details in $\textit{taskInfo}$ and push the corresponding $\textit{priority}$ and $\textit{taskId}$ into the heap. If a task’s priority changes, we update its entry in $\textit{taskInfo}$ and push the new pair into the heap as well, letting outdated entries be ignored later through lazy deletion. Tasks that are deleted are simply removed from $\textit{taskInfo}$, and any stale heap entries related to them are skipped during execution.

To execute the highest-priority task, we repeatedly pop from the top of the heap until we find one that still exists in $\textit{taskInfo}$ and whose priority matches. Once such a task is found, it is removed from $\textit{taskInfo}$ and its $\textit{userId}$ is returned. If no valid task remains, the operation ends with an empty result.

#### Implementation


```python
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskInfo = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.taskInfo[taskId] = [priority, userId]
            heappush(self.heap, [-priority, -taskId])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskInfo[taskId] = [priority, userId]
        heappush(self.heap, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskInfo[taskId][0] = newPriority
        heappush(self.heap, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        self.taskInfo.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heappop(self.heap)
            priority, taskId = -priority, -taskId
            if priority == self.taskInfo.get(taskId, [-1, -1])[0]:
                return self.taskInfo.pop(taskId)[1]
        return -1
```


#### Complexity Analysis

Let $n$ be the number of tasks at initialization and $m$ be the number of subsequent operations.

- Time complexity: Initialization takes $O(n \log n)$. $\textit{add}$ and $\textit{edit}$ each take $O(\log (n+m))$. $\textit{rmv}$ takes $O(1)$. $\textit{execTop}$ has an average cost of $O(\log (n+m))$.

- Space complexity: $O(n + m)$.

---