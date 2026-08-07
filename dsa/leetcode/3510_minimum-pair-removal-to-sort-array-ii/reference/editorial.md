### Approach: Priority Queue + Lazy Deletion

#### Intuition

This problem is an enhanced version of [3507. Minimum Pair Removal to Sort Array I](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/). A naive simulation will time out for this data scale, so we need to optimize the three key logic steps in the original simulation: finding the minimum adjacent pair sum, checking the monotonicity of the current array, and merging the minimum adjacent pair.

**Maintain the minimum sum of adjacent number pairs**

Firstly, consider how to find the sum of the smallest adjacent number pair. It is easy to think of using a priority queue to maintain all adjacent pairs. We store references to adjacent number pairs in the priority queue. Assuming the current adjacent number pair popped out is $(i, j)$, after the merge operation, the elements originally located at $i - 1$ and $j + 1$ will form two new adjacent number pairs with the newly merged element. Therefore, these new number pairs need to be added to the priority queue. At the same time, the two number pairs originally formed by $(i - 1, i)$ and $(j, j + 1)$, if they exist, become dirty data in the priority queue. In this situation, it is common to apply the lazy deletion technique, that is, determine whether the popped data is dirty data during the pop operation, rather than immediately deleting the corresponding elements from the priority queue.

There are multiple ways to determine whether elements in a priority queue are dirty data. Here is one approach: assuming that pairs are always merged to the left, we maintain two pieces of information:

- Use a $\textit{merged}$ array to determine whether an element at a certain position has already been merged. Only when both elements are not merged are their references considered valid.
- When storing a pair of numbers, store the current pair and its sum. When popping the pair, even if both elements are valid, if the sum has changed, it is clearly dirty data.

There exists an extreme case where both elements in a pair are valid and the sum of the pair remains unchanged, yet the pair is still considered dirty data. It can be proven that this situation does not affect the correctness of the result, because even if the pair is dirty data, it remains the target of the current merge round.

**Maintain the monotonicity of the array**

Next, we determine the monotonicity of the array. It is not difficult to observe that the monotonicity of adjacent elements determines the overall monotonicity of the array. Therefore, we maintain a variable $\textit{decreaseCount}$, which represents the number of decreasing adjacent pairs in the current $\textit{nums}$. Clearly, when $\textit{decreaseCount}$ is $0$, $\textit{nums}$ is in a non-decreasing state.

We can maintain the changes in $\textit{decreaseCount}$ during the process of merging a pair $(i, j)$. We consider three cases:

- For the pair $(i, j)$, if it originally satisfies $\textit{nums}[i] > \textit{nums}[j]$, then $\textit{decreaseCount}$ should be decremented by one.
- If $i$ is not the first element, consider the change in monotonicity between $\textit{nums}[i - 1]$ and $\textit{nums}[i]$ before and after merging. If it changes from decreasing to non-decreasing, decrement $\textit{decreaseCount}$ by one; otherwise, increment it by one.
- Similarly, if $j$ is not the last element, apply the same logic to update the relationship between $\textit{nums}[j]$ and $\textit{nums}[j + 1]$.

At this point, $\textit{decreaseCount} = 0$ becomes the termination condition of the outer loop.

**Merge elements**

After the above processing, we no longer need to traverse $\textit{nums}$ directly. Instead, we only need to obtain the predecessor and successor of the current pair. Moreover, merging elements inevitably involves deletion in a linear structure. Therefore, using a doubly linked list to maintain $\textit{nums}$ is the most suitable choice.

After optimizing the above three logic steps, simulating the process of repeatedly finding the minimum adjacent pair and merging them according to the problem requirements allows us to solve the problem efficiently.

#### Implementation

```python
class Node:
    def __init__(self, value, left):
        self.value = value
        self.left = left
        self.prev = None
        self.next = None

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        class PQItem:
            def __init__(self, first, second, cost):
                self.first = first
                self.second = second
                self.cost = cost

            def __lt__(self, other):
                if self.cost == other.cost:
                    return self.first.left < other.first.left
                return self.cost < other.cost

        pq = []
        head = Node(nums[0], 0)
        current = head
        merged = [False] * len(nums)
        decrease_count = 0
        count = 0

        for i in range(1, len(nums)):
            new_node = Node(nums[i], i)
            current.next = new_node
            new_node.prev = current
            heapq.heappush(
                pq, PQItem(current, new_node, current.value + new_node.value)
            )

            if nums[i - 1] > nums[i]:
                decrease_count += 1

            current = new_node

        while decrease_count > 0:
            item = heapq.heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            if (
                merged[first.left]
                or merged[second.left]
                or first.value + second.value != cost
            ):
                continue
            count += 1

            if first.value > second.value:
                decrease_count -= 1

            prev_node = first.prev
            next_node = second.next
            first.next = next_node
            if next_node:
                next_node.prev = first

            if prev_node:
                if prev_node.value > first.value and prev_node.value <= cost:
                    decrease_count -= 1
                elif prev_node.value <= first.value and prev_node.value > cost:
                    decrease_count += 1

                heapq.heappush(
                    pq, PQItem(prev_node, first, prev_node.value + cost)
                )

            if next_node:
                if second.value > next_node.value and cost <= next_node.value:
                    decrease_count -= 1
                elif second.value <= next_node.value and cost > next_node.value:
                    decrease_count += 1
                heapq.heappush(
                    pq, PQItem(first, next_node, cost + next_node.value)
                )

            first.value = cost
            merged[second.left] = True

        return count
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n \log n)$.

  The merge operation can be performed at most $n - 1$ times. Each merge involves priority queue operations that take $O(\log n)$ time, while all other operations are constant time. Therefore, the overall time complexity is $O(n \log n)$.

- Space complexity: $O(n)$.

  The auxiliary data structures, including the doubly linked list and the priority queue, occupy $O(n)$ space.

---