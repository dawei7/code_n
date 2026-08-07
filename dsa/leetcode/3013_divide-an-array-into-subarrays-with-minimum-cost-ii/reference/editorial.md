### Approach: Ordered Set

#### Intuition

According to the problem statement, we need to split the given array $\textit{nums}$ into $k$ **continuous and non-overlapping** subarrays such that the starting index of the **second** subarray is **no more than** $\textit{dist}$ away from the starting index of the $\textit{k}$-th subarray. The **cost** of each subarray is defined as its first element, and we are required to return the **minimum** possible total cost.

From the problem statement, we can infer that once the first elements of the $k$ subarrays are chosen, the division of the array is uniquely determined. Regardless of how the array is split, the first element of the first subarray must be $\textit{nums}[0]$, and the remaining $k - 1$ subarrays must have their first elements selected from the range $\textit{nums}[1]$ to $\textit{nums}[n - 1]$.

We enumerate the first element of the last subarray, denoted by $\textit{nums}[i]$. Since the starting index of the second subarray is at a distance of **no more than** $\textit{dist}$ from the starting index of the $\textit{k}$-th subarray, the starting index of the second subarray cannot be less than $i - \textit{dist}$. Therefore, we need to select $k - 2$ elements from the index range $[i - \textit{dist}, i - 1]$ as the first elements of the remaining subarrays.

This naturally forms a sliding window of length $\textit{dist}$. By the greedy principle, to minimize the total cost, we should choose the smallest $k - 2$ elements within this window.

As the window slides, we only need to maintain the smallest $k - 2$ values in the current window. This idea is similar to that used in the [480. Sliding Window Median](https://leetcode.cn/problems/sliding-window-median/description/) problem. Here, we maintain two ordered sets. The first set $\textit{st}_1$ stores the smallest $k - 2$ elements, while the second set $\textit{st}_2$ stores the remaining elements. The maintenance rules are as follows:

+ Add an element: If the new element $x$ is greater than or equal to the smallest element in $\textit{st}_2$, insert $x$ into $\textit{st}_2$; otherwise, insert it into $\textit{st}_1$. Then, rebalance the two sets so that $\textit{st}_1$ contains exactly the smallest $k - 2$ elements.

+ Delete element: If the element to be removed exists in $\textit{st}_1$, remove it from $\textit{st}_1$; otherwise, remove it from $\textit{st}_2$. After removal, rebalance the sets to restore the invariant.

+ Adjust the sets: To ensure that $\textit{st}_1$ always contains exactly the smallest $k - 2$ elements, move the smallest elements from $\textit{st}_2$ to $\textit{st}_1$ when $\textit{st}_1$ has fewer than $k - 2$ elements, and move the largest elements from $\textit{st}_1$ to $\textit{st}_2$ when it has more than $k - 2$ elements.

+ Compute the sum of elements: Maintain the sum of all elements in $\textit{st}_1$, updating it whenever elements are added or removed.

For each enumerated last subarray starting at index $i$, the total cost is $\textit{nums}[0] + \textit{sum} + \textit{nums}[i]$. The minimum of these values is the final answer.

#### Implementation

```python
class Container:
    def __init__(self, k: int):
        self.k = k
        self.st1 = SortedList()
        self.st2 = SortedList()
        self.sm = 0

    def adjust(self):
        while len(self.st1) < self.k and len(self.st2) > 0:
            x = self.st2[0]
            self.st1.add(x)
            self.st2.remove(x)
            self.sm += x

        while len(self.st1) > self.k:
            x = self.st1[-1]
            self.st2.add(x)
            self.st1.remove(x)
            self.sm -= x

    # insert element x
    def add(self, x: int):
        if len(self.st2) > 0 and x >= self.st2[0]:
            self.st2.add(x)
        else:
            self.st1.add(x)
            self.sm += x
        self.adjust()

    # delete element x
    def erase(self, x: int):
        if x in self.st1:
            self.st1.remove(x)
            self.sm -= x
        elif x in self.st2:
            self.st2.remove(x)
        self.adjust()

    # sum of the first k smallest elements
    def sum(self) -> int:
        return self.sm

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        cnt = Container(k - 2)
        for i in range(1, k - 1):
            cnt.add(nums[i])

        ans = cnt.sum() + nums[k - 1]
        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                cnt.erase(nums[j])
            cnt.add(nums[i - 1])
            ans = min(ans, cnt.sum() + nums[i])

        return ans + nums[0]
```

#### Complexity Analysis

Let $n$ be the length of the given array.

- Time complexity: $O(n \log n)$.

  Each insertion, deletion, and adjustment operation on the ordered sets takes $O(\log n)$ time. Since at most $n$ such operations are performed, the total time complexity is $O(n \log n)$.

- Space complexity: $O(n)$.

  The ordered sets together can store up to $n$ elements.

---