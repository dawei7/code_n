[TOC]

### Approach Framework

**Intuition**

Intuitively, there are two operations: `update`, which updates our notion of the board (number line) after dropping a square; and `query`, which finds the largest height in the current board on some interval. We will work on implementing these operations.

**Coordinate Compression**

In the below approaches, since there are only up to $2 * len(positions)$ critical points, namely the left and right edges of each square, we can use a technique called *coordinate compression* to map these critical points to adjacent integers, as shown in the code snippets below.

For brevity, these snippets are omitted from the remaining solutions.

```python
coords = set()
for left, size in positions:
    coords.add(left)
    coords.add(left + size - 1)
index = {x: i for i, x in enumerate(sorted(coords))}
```

---
### Approach 1: Offline Propagation

**Intuition**

Instead of asking the question "What squares affect this query?", let's ask the question "What queries are affected by this square?"

**Algorithm**

Let $\text{qans}[i]$ be the maximum height of the interval specified by $\text{positions}[i]$. In the end, we'll return a running max of `qans`.

For each square $\text{positions}[i]$, the maximum height will get higher by the size of the square we drop. Then, for any future squares that intersect the interval `[left, right)` (where $left = \text{positions}[i][0], right = \text{positions}[i][0] + \text{positions}[i][1]$), we'll update the maximum height of that interval.

```python
class Solution(object):
    def fallingSquares(self, positions):
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in xrange(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `positions`. We use two for-loops, each of complexity $O(N)$.

* Space Complexity: $O(N)$, the space used by `qans` and `ans`.
<br>
<br>

---
### Approach 2: Brute Force with Coordinate Compression

**Intuition and Algorithm**

Let $N = len(positions)$. After mapping the board to a board of length at most $2* N \leq 2000$, we can brute force the answer by simulating each square's drop directly.

Our answer is either the current answer or the height of the square that was just dropped, and we'll update it appropriately.

```python
class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate Compression
        #index = ...

        heights = [0] * len(index)
        def query(L, R):
            return max(heights[i] for i in xrange(L, R+1))

        def update(L, R, h):
            for i in xrange(L, R+1):
                heights[i] = max(heights[i], h)

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N^2)$, where $N$ is the length of `positions`. We use two for-loops, each of complexity $O(N)$ (because of coordinate compression.)

* Space Complexity: $O(N)$, the space used by `heights`.
<br>
<br>

---
### Approach 3: Block (Square Root) Decomposition

**Intuition**

Whenever we perform operations (like `update` and `query`) on some interval in a domain, we could segment that domain with size $W$ into blocks of size $\sqrt{W}$.

Then, instead of a typical brute force where we update our array `heights` representing the board, we will also hold another array `blocks`, where $\text{blocks}[i]$ represents the $B = \lfloor \sqrt{W} \rfloor$ elements $heights[B*i], heights[B*i + 1], ..., heights[B*i + B-1]$.  This allows us to write to the array in $O(B)$ operations.

**Algorithm**

Let's get into the details.  We actually need another array, $\text{blocks}_{read}$. When we update some element `i` in block $b = i / B$, we'll also update $\text{blocks}_{read}[b]$. If later we want to read the entire block, we can read from here (and stuff written to the whole block in $\text{blocks}[b]$.)

When we write to a block, we'll write in $\text{blocks}[b]$. Later, when we want to read from an element `i` in block $b = i / B$, we'll read from $\text{heights}[i]$ and $\text{blocks}[b]$.

Our process for managing `query` and `update` will be similar.  While `left` isn't a multiple of `B`, we'll proceed with a brute-force-like approach, and similarly for `right`. In the end, `[left, right+1)` will represent a series of contiguous blocks: the interval will have a length that is a multiple of `B`, and `left` will also be a multiple of `B`.

```python
class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate compression
        #index = ...

        W = len(index)
        B = int(W**.5)
        heights = [0] * W
        blocks = [0] * (B+2)
        blocks_read = [0] * (B+2)

        def query(left, right):
            ans = 0
            while left % B and left <= right:
                ans = max(ans, heights[left], blocks[left / B])
                left += 1
            while right % B != B-1 and left <= right:
                ans = max(ans, heights[right], blocks[right / B])
                right -= 1
            while left <= right:
                ans = max(ans, blocks[left / B], blocks_read[left / B])
                left += B
            return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left / B] = max(blocks_read[left / B], h)
                left += 1
            while right % B != B-1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right / B] = max(blocks_read[right / B], h)
                right -= 1
            while left <= right:
                blocks[left / B] = max(blocks[left / B], h)
                left += B

        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N\sqrt{N})$, where $N$ is the length of `positions`. Each `query` and `update` has complexity $O(\sqrt{N})$.

* Space Complexity: $O(N)$, the space used by `heights`.
<br>
<br>

---
### Approach 4: Segment Tree with Lazy Propagation

**Intuition**

If we were familiar with the idea of a segment tree (which supports queries and updates on intervals), we could immediately crack the problem.

**Algorithm**

Segment trees work by breaking intervals into a disjoint sum of component intervals, whose number is at most `log(width)`. The motivation is that when we change an element, we only need to change `log(width)` of many intervals that aggregate on an interval containing that element.

When we want to update an interval all at once, we need to use *lazy propagation* to ensure good run-time complexity. This topic is covered in more depth [here](https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/).

With such an implementation in hand, the problem falls out immediately.

```python
class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x /= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in xrange(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L /= 2; R /= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L /= 2; R /= 2
        return ans

class Solution(object):
    def fallingSquares(self, positions):
        #Coordinate compression
        #index = ...

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \log N)$, where $N$ is the length of `positions`. This is the run-time complexity of using a segment tree.

* Space Complexity: $O(N)$, the space used by our tree.
<br>
<br>