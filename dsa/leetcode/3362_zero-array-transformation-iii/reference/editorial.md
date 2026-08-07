[TOC]

## Solution

---

### Approach: Greedy + Priority Queue

#### Intuition

First, we consider the element at index $0$ in $\textit{nums}$. If $\textit{nums}[0] > 0$, we must find at least $\textit{nums}[0]$ elements in $\textit{queries}$ with left endpoints of $0$ to retain so that $\textit{nums}[0]$ can be reduced to $0$. Now, which elements of $\textit{nums}[0]$ should we choose? Greedily, we should select those with the largest right endpoints. After this selection, we move on to $\textit{nums}[1]$. The elements selected in the previous step may not include index $1$, and we need to remove them. This can be accomplished using the difference array $\textit{deltaArray}$.

At this point, the cumulative number of operations may not be enough to reduce $\textit{nums}[1]$ to $0$, and we need to select elements from $\textit{queries}$, similar to the previous step. We can select the elements with the largest right endpoints from the portion of unselected elements whose left endpoints are $\leq 1$ until the number of operations satisfies the condition to reduce $\textit{nums}[1]$ to $0$. This calculation can be efficiently handled using a priority queue (or $\textit{heap}$).

As we traverse $\textit{nums}$, we continuously insert the right endpoints of the $\textit{queries}$ corresponding to the left endpoints into the $\textit{heap}$. When the number of operations is insufficient, we keep extracting the largest right endpoint from the $\textit{heap}$ until the required number of operations is met. After completing the traversal, the size of the $\textit{heap}$ represents the number of $\textit{queries}$ that can be deleted.

#### Implementation

```python
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$ and $m$ be the length of $\textit{queries}$.

- Time complexity: $O(n + m \times \log{m})$.

  Sorting the $\textit{queries}$ takes $O(m \log{m})$ time. Each insertion and deletion from the priority queue (which tracks the endpoints) requires $O(\log{m})$ time.

- Space complexity: $O(n + m)$.

  We need to store both the difference array and the priority queue, which require $O(n)$ and $O(m)$ space, respectively.