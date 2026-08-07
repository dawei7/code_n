### Approach 1: Segment Tree

#### Intuition

The question is essentially asking whether there exists a blank interval of length at least $\textit{sz}$ that is completely contained within the range $[0, x]$.

To help maintain these blank intervals, we define $p[i]$ as the position of the nearest obstacle to the left of $i$. Then, $d[i] = i - p[i]$ represents the length of the maximum blank interval ending at position $i$.

For each query with parameters $x$ and $\textit{sz}$, the problem becomes determining whether there exists an index $i \le x$ such that $d[i] \ge \textit{sz}$. In other words, we need to check whether the maximum value of $d[i]$ in the interval $[0, x]$ is at least $\textit{sz}$.

We do not need to maintain every individual point. Instead, we only need to maintain the lengths of the intervals. The next question is where to store these interval lengths so that queries can be processed efficiently.

Observe that each query consists of several complete intervals and at most one incomplete interval truncated by $x$. We can store the length of each interval at its right endpoint. Specifically, we store $d[r]$ at the right endpoint $r$, where for every complete interval, $d[r]$ equals the distance to the nearest obstacle on the left.

The remaining problem is how to maintain the $d$ array dynamically. We can use a segment tree to support point updates and range maximum queries.

Let $\textit{pre}$ and $\textit{nxt}$ denote the positions of the nearest obstacles to the left and right of $x$, respectively. When inserting an obstacle at position $x$, we need to update both $d[x]$ and $d[\textit{nxt}]$.

During a query, the interval $[0, \textit{pre}]$ consists entirely of complete intervals, so we can directly query it using the segment tree. The remaining incomplete interval $[\textit{pre}, x]$ is handled separately by comparing its length with $\textit{sz}$.

We also need to efficiently determine the nearest obstacles on both sides of $x$, which requires maintaining an ordered structure during insertions. A balanced binary search tree can be used for this purpose.

#### Implementation


```python
class Solution:
    def __init__(self):
        self.seg = []
        self.st = SortedList()
        self.mx = 50000

    def update(self, idx: int, val: int, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = val
            return

        mid = (l + r) >> 1
        if idx <= mid:
            self.update(idx, val, p << 1, l, mid)
        else:
            self.update(idx, val, p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int, p: int, l: int, r: int) -> int:
        if L <= l and r <= R:
            return self.seg[p]

        mid = (l + r) >> 1
        res = 0
        if L <= mid:
            res = max(res, self.query(L, R, p << 1, l, mid))
        if R > mid:
            res = max(res, self.query(L, R, p << 1 | 1, mid + 1, r))

        return res

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        self.mx = 50000
        self.seg = [0] * (self.mx << 2)
        self.st = SortedList([0, self.mx])
        self.update(self.mx, self.mx, 1, 0, self.mx)
        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = min(len(self.st) - 1, self.st.bisect_right(x))

                r = self.st[idx]
                l = self.st[idx - 1] if idx > 0 else self.st[0]
                self.update(x, x - l, 1, 0, self.mx)
                self.update(r, r - x, 1, 0, self.mx)
                self.st.add(x)
            else:
                x, sz = q[1], q[2]
                idx = min(len(self.st) - 1, self.st.bisect_right(x))
                pre = self.st[0] if idx == 0 else self.st[idx - 1]

                max_space = max(x - pre, self.query(0, pre, 1, 0, self.mx))
                ans.append(max_space >= sz)

        return ans
```


#### Complexity Analysis

Let $q$ be the length of $\textit{queries}$, and let $M$ be the maximum value of $x$.

- Time complexity: $O(q \log q + q \log M)$.
  
  Each balanced tree operation requires $O(\log q)$ time, and each segment tree update or query requires $O(\log M)$ time.

- Space complexity: $O(M+q)$.
  
  The segment tree requires $O(M)$ space, while the balanced tree stores at most $O(q)$ obstacles.
---

### Approach 2: Fenwick Tree

#### Intuition

Similar to a segment tree, a Fenwick tree can also be used to maintain interval maximums. However, after adding an obstacle, interval lengths may decrease, and a Fenwick tree cannot efficiently support such range updates. Therefore, we need a different perspective.

Instead of processing the queries forward, we process them in reverse order. Initially, we assume that all obstacles already exist. Then, while traversing the queries backward, we remove obstacles one by one, causing adjacent intervals to merge into larger intervals.

Let $d[r]$ denote the distance from $r$ to the nearest obstacle on its left. Let $\textit{pre}$ and $\textit{nxt}$ represent the positions of the nearest obstacles to the left and right of $x$, respectively. Then:

$$
d[r] = r - \textit{pre}
$$

When deleting an obstacle at position $x$, the two original intervals $[\textit{pre}, x]$ and $[x, \textit{nxt}]$ merge into a single interval $[\textit{pre}, \textit{nxt}]$, whose length becomes:

$$
\textit{nxt} - \textit{pre}
$$

Since interval lengths only increase during this reverse process, we can use a Fenwick tree to maintain prefix maximums efficiently.

#### Implementation


```python
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = 50000

        st = SortedList([0, mx])
        for q in queries:
            if q[0] == 1:
                st.add(q[1])

        bt = [0] * (mx + 1)

        def update(x: int, v: int) -> None:
            while x < len(bt):
                if v > bt[x]:
                    bt[x] = v
                x += x & -x

        def query(x: int) -> int:
            res = 0
            while x > 0:
                if bt[x] > res:
                    res = bt[x]
                x -= x & -x
            return res

        pre = 0
        for x in st:
            if x == 0:
                continue
            update(x, x - pre)
            pre = x

        ans = []
        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]
                idx = st.bisect_left(x)
                if idx < len(st) and st[idx] == x:
                    pre_val = x
                else:
                    pre_val = st[idx - 1]
                max_space = query(pre_val)
                max_space = max(max_space, x - pre_val)
                ans.append(max_space >= sz)
            else:
                x = q[1]
                idx = st.bisect_left(x)
                pre_val = st[idx - 1]
                nxt = st[idx + 1]
                update(nxt, nxt - pre_val)
                st.discard(x)

        return ans[::-1]
```


#### Complexity Analysis

Let $q$ be the length of $\textit{queries}$, and let $M$ be the maximum value of $x$.

- Time complexity: $O(q \log q + q \log M)$.
  
  While processing queries in reverse order, each balanced tree operation requires $O(\log q)$ time, and each Fenwick tree update or prefix maximum query requires $O(\log M)$ time.

- Space complexity: $O(M + q)$.
  
  The Fenwick tree requires $O(M)$ space, and the balanced tree stores at most $O(q)$ obstacles.

---