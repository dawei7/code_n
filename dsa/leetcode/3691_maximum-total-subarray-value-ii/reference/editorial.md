### Approach 1: Sparse Table + Max Heap

#### Intuition

This problem is an advanced version of "[3689. Maximum Total Subarray Value I](https://leetcode.com/problems/maximum-total-subarray-value-i/)", with the additional requirement that we must select $k$ different subarrays.

For a fixed left endpoint $l$, as the right endpoint $r$ increases, the maximum value in the subarray $\textit{nums}[l..r]$ can only increase (or remain unchanged), while the minimum value can only decrease (or remain unchanged). Therefore, the subarray value $\max(\textit{nums}[l..r]) - \min(\textit{nums}[l..r])$ is monotonically non-decreasing.

For each left endpoint $l$, this gives us a monotonically increasing sequence of length $n-l$, where the $i$-th element represents the value of $\textit{nums}[l..l+i]$, namely $\max(\textit{nums}[l..l+i]) - \min(\textit{nums}[l..l+i])$.

The problem can therefore be reformulated as follows:
> Given $n$ monotonically increasing sequences, find the sum of the largest $k$ elements across all sequences.

For example, if $\textit{nums} = [3,1,4,1]$, then the sequence corresponding to $l = 1$ is `[0,3,3]` (representing the values of subarrays `[1]`, `[1,4]`, and `[1,4,1]`). Similarly, the sequence corresponding to $l = 2$ is `[0,3]`, and so on.

Since the last element of each sequence is its maximum value, we can efficiently extract the global maximum using a max heap. Whenever we remove the current maximum element from a sequence, the next candidate from that sequence is simply the previous element.

Thus, we can solve this subproblem using a max heap:

1. Initially, insert the last element of every sequence (corresponding to $r = n - 1$), together with its coordinates $(l, r)$, into the max heap.
2. Repeat $k$ times:
  - Remove the top element $(v, l, r)$ from the heap.
  - Add $v$ to the answer.
  - If $r > l$, insert the previous element from the same sequence, namely $(l, r - 1)$.

To evaluate the value of any subarray $[l, r]$ efficiently, we need to query its maximum and minimum values. We can preprocess a sparse table (ST table) to support these queries in $O(1)$ time.

The sparse table stores:
- $\text{stMax}[i][j]$: the maximum value in the interval starting at index $i$ with length $2^j$.
- $\text{stMin}[i][j]$: the minimum value in the interval starting at index $i$ with length $2^j$.

To query an interval $[l, r]$, let $j = \lfloor\log_2(r-l+1)\rfloor$

The interval can then be covered by two overlapping intervals of length $2^j$, allowing us to compute the maximum and minimum values in $O(1)$ time. Building the sparse table requires $O(n \log n)$ preprocessing time.

#### Implementation

```python
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        logn = n.bit_length()
        stMax = [[0] * logn for _ in range(n)]
        stMin = [[0] * logn for _ in range(n)]
        for i in range(n):
            stMax[i][0] = stMin[i][0] = nums[i]
        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                stMax[i][j] = max(stMax[i][j - 1], stMax[i + step][j - 1])
                stMin[i][j] = min(stMin[i][j - 1], stMin[i + step][j - 1])

        def queryMax(l: int, r: int) -> int:
            j = (r - l + 1).bit_length() - 1
            return max(stMax[l][j], stMax[r - (1 << j) + 1][j])

        def queryMin(l: int, r: int) -> int:
            j = (r - l + 1).bit_length() - 1
            return min(stMin[l][j], stMin[r - (1 << j) + 1][j])

        pq = [
            (-(queryMax(l, n - 1) - queryMin(l, n - 1)), l, n - 1)
            for l in range(n)
        ]
        heapq.heapify(pq)
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            if r > l:
                heapq.heappush(
                    pq, (-(queryMax(l, r - 1) - queryMin(l, r - 1)), l, r - 1)
                )
        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $k$ be the number of selected non-empty subarrays.

- Time complexity: $O(n \log n + k \log n)$.

  Building the sparse table requires $O(n \log n)$ time. Initializing the heap requires $O(n \log n)$ time. Each heap insertion and removal operation takes $O(\log n)$ time, and we perform at most $k$ such iterations.

- Space complexity: $O(n \log n)$.

  The sparse table requires $O(n \log n)$ space, while the heap requires $O(n)$ space.

---

### Approach 2: Segment Tree + Max Heap

#### Intuition

Approach 1 uses a sparse table to support $O(1)$ range maximum and minimum queries, but it requires $O(n \log n)$ preprocessing space. Alternatively, we can replace the sparse table with a segment tree, reducing the space complexity to $O(n)$.

A segment tree is a binary tree structure in which each node stores the maximum and minimum values of its corresponding interval. It supports range maximum and minimum queries in $O(\log n)$ time.

The overall algorithm remains the same as in Approach 1:

1. Build a segment tree that stores the maximum and minimum values for every interval.
2. For each left endpoint $l$, insert the value of the subarray $\textit{nums}[l..n-1]$ into a max heap.
3. Repeat $k$ times:
  - Remove the top element from the heap.
  - Add its value to the answer.
  - If $r > l$, insert the value of $\textit{nums}[l..r-1]$ into the heap.

The only difference from Approach 1 is that interval maximum and minimum queries are now performed using the segment tree instead of the sparse table.

#### Implementation

```python
class SegTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.maxv = [0] * (4 * self.n)
        self.minv = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node: int, l: int, r: int, nums: List[int]):
        if l == r:
            self.maxv[node] = self.minv[node] = nums[l]
            return
        m = (l + r) // 2
        self.build(node * 2, l, m, nums)
        self.build(node * 2 + 1, m + 1, r, nums)
        self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])
        self.minv[node] = min(self.minv[node * 2], self.minv[node * 2 + 1])

    def queryMax(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.maxv[node]
        m = (l + r) // 2
        res = -(10**18)
        if ql <= m:
            res = max(res, self.queryMax(node * 2, l, m, ql, qr))
        if qr > m:
            res = max(res, self.queryMax(node * 2 + 1, m + 1, r, ql, qr))
        return res

    def queryMin(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.minv[node]
        m = (l + r) // 2
        res = 10**18
        if ql <= m:
            res = min(res, self.queryMin(node * 2, l, m, ql, qr))
        if qr > m:
            res = min(res, self.queryMin(node * 2 + 1, m + 1, r, ql, qr))
        return res

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = SegTree(nums)
        pq = [
            (
-(
                    seg.queryMax(1, 0, n - 1, l, n - 1)
- seg.queryMin(1, 0, n - 1, l, n - 1)
                ),
                l,
                n - 1,
            )
            for l in range(n)
        ]
        heapq.heapify(pq)
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            if r > l:
                heapq.heappush(
                    pq,
                    (
-(
                            seg.queryMax(1, 0, n - 1, l, r - 1)
- seg.queryMin(1, 0, n - 1, l, r - 1)
                        ),
                        l,
                        r - 1,
                    ),
                )
        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $k$ be the number of selected non-empty subarrays.

- Time complexity: $O((n + k) \log n)$.

  Building the segment tree requires $O(n)$ time. Each interval query requires $O(\log n)$ time. We perform a total of $O(n + k)$ interval queries, and all heap operations together require $O((n + k)\log n)$ time.

- Space complexity: $O(n)$.

  Both the segment tree and the heap require $O(n)$ space.

---