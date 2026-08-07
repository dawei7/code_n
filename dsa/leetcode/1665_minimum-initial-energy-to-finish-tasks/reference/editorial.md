### Approach 1: Greedy (Difference Increasing)

#### Intuition

The core idea is to lend the budget from tasks with smaller differences to tasks with larger differences, thereby minimizing the initial energy as much as possible.

For example, suppose there are two tasks: $\textit{tasks}[0] = [3,3]$ and $\textit{tasks}[1] = [3,x]$. If we need to consume a total of 6 units of energy to complete these two tasks (in the order of task 1 followed by task 0), then the value of $x$ in task 1 can range from 3 to 6.

This suggests that when the minimum energy required to start a task is equal to the actual energy consumed, the task can be completed as long as the current energy is sufficient, without imposing additional constraints. In this situation, the minimum required energy can be viewed as a transferable quota that can be “lent” to other tasks to help meet their minimum starting requirements.

Based on this idea, we sort the tasks in ascending order according to the difference between the minimum required energy $\textit{minimum}[i]$ and the actual energy consumed $\textit{actual}[i]$. By placing tasks with smaller differences first and those with larger differences later, we effectively allocate more quota to tasks that need it most, thereby minimizing the initial energy.

- Each time we process a task, we first add the energy it consumes to $\textit{ans}$. This ensures that we have accounted for completing all previously processed tasks.
- If the accumulated energy is still less than the minimum required to start the current task, we update $\textit{ans}$ to match this required minimum, ensuring the task can be completed.

The final value of $\textit{ans}$ represents the minimum initial energy required to complete all tasks.

#### Implementation

```python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for task in tasks:
            ans = max(ans + task[0], task[1])
        return ans
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{tasks}$.

- Time complexity: $O(n \log n)$.

  The dominant cost is sorting, while the traversal takes $O(n)$ time.

- Space complexity: $O(\log n)$.

  This is due to the recursive call stack used during sorting.

---

### Approach 2: Greedy (Difference Decreases)

#### Intuition

The core idea is to prioritize tasks with larger differences to reduce wasted energy.

If the initial energy is fixed, then a larger difference $\textit{remain} = \textit{minimum}[i] - \textit{actual}[i]$ for a task means more energy will remain after completing it. Based on this observation, we process tasks with larger $\textit{remain}$ values first and leave those with smaller values for later. This helps minimize energy loss across all tasks.

Thus, we sort the tasks in descending order of $\textit{remain}$ and process them sequentially:

- We use $\textit{ans}$ to track the required initial energy and $\textit{remain}$ to track the remaining energy after completing tasks.
- For each task, if the current remaining energy is at least the minimum required, we can complete it without increasing $\textit{ans}$. Otherwise, we must add $\textit{task}[1] - \textit{remain}$ to $\textit{ans}$.
- If the task is completed using existing energy, the new remaining energy becomes $\textit{remain} - \textit{task}[0]$. If we need to replenish energy, we first raise $\textit{remain}$ to $\textit{task}[1]$, and after completing the task, it becomes $\textit{task}[1] - \textit{task}[0]$.

The final value of $\textit{ans}$ is the minimum initial energy required.

#### Implementation

```python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        ans = 0
        remain = 0
        for task in tasks:
            if remain <= task[1]:
                ans += task[1] - remain
            remain = max(task[1] - task[0], remain - task[0])
        return ans
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{tasks}$.

- Time complexity: $O(n \log n)$.

  The dominant cost is sorting, while the traversal takes $O(n)$ time.

- Space complexity: $O(\log n)$.

  This is due to the recursive call stack used during sorting.

---