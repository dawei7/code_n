### Approach: Two Pointer + Exponential Increment

#### Intuition

"[3532. Path Existence Queries in a Graph I](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/)" is the predecessor of this problem. Unlike the predecessor, the array $\textit{nums}$ is **unordered**, and each query asks for the **shortest distance** between two nodes.

For convenience, let $n$ be the length of $\textit{nums}$. We say that two nodes are **connected** if there exists a path between them.

From the predecessor problem, we know that after sorting $\textit{nums}$, if two adjacent nodes in the sorted order differ by at most `maxDiff`, then they are directly connected. Consequently, every connected component forms a contiguous interval in the sorted array. For each node, we define its **adjacent interval** as the maximal contiguous interval containing that node in which every pair of adjacent values differs by at most `maxDiff`.

Using a two-pointer algorithm, we can compute the left endpoint of the adjacent interval for every node. To facilitate answering queries, we first sort $\textit{nums}$. Let $\textit{pos}[i]$ denote the position of $\textit{nums}[i]$ in the sorted array, and let $\textit{idx}[i]$ denote the original index of the $i$-th element in the sorted array. These two arrays provide a bidirectional mapping between the original and sorted orders.

Now consider a query between nodes $x$ and $y$. Convert them to their positions in the sorted array, $\textit{pos}[x]$ and $\textit{pos}[y]$. Assume $x$ is to the left of $y$ after sorting (otherwise, simply swap them).

A straightforward approach is to repeatedly jump from $y$ to the left endpoint of its adjacent interval until it reaches or passes $x$. The number of jumps equals the shortest distance between the two nodes. However, performing these jumps one at a time is too slow when there are many queries.

To accelerate the process, we use **binary lifting**. Let $f[x][i]$ denote the node reached after making $2^i$ leftward jumps from node $x$, where $0 \le i \le \lfloor \log_2 n \rfloor$. For each query, we greedily enumerate the powers of two from largest to smallest. Whenever jumping $2^i$ steps still leaves $y$ strictly to the right of $x$, we perform that jump. After all jumps are processed, there are two possibilities:

* If $x$ and $y$ are connected, then $y$ will be exactly one jump away from reaching or passing $x$, so the answer is the accumulated number of jumps plus one.
* Otherwise, $y$ has already reached the left endpoint of its connected component and can no longer move left, so no path exists.

Note that if $x$ and $y$ are initially the same node, the answer is `0`.

#### Implementation


```python
class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        idx = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for i, v in enumerate(idx):
            pos[v] = i

        m = n.bit_length()
        f = [[0] * m for _ in range(n)]

        left = 0
        for i in range(n):
            while left < i and nums[idx[i]] - nums[idx[left]] > maxDiff:
                left += 1
            f[i][0] = left

        for j in range(1, m):
            for i in range(n):
                f[i][j] = f[f[i][j - 1]][j - 1]

        res = []
        for query in queries:
            x, y = pos[query[0]], pos[query[1]]
            if x > y:
                x, y = y, x

            if x == y:
                res.append(0)
                continue

            step = 0
            for i in range(m - 1, -1, -1):
                if f[y][i] > x:
                    y = f[y][i]
                    step += 1 << i

            if f[y][0] <= x:
                res.append(step + 1)
            else:
                res.append(-1)

        return res
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $q$ be the number of queries.

- Time complexity: $O(n \log n + q \log n)$.

- Space complexity: $O(n \log n)$.

---