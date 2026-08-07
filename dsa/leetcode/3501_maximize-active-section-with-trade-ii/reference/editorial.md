### Approach 1: Binary Search + Segment Tree

#### Intuition

Readers are advised to first solve the prerequisite problem [3499. Maximize Active Section with Trade I](https://leetcode.com/problems/maximize-active-section-with-trade-i/).

In [3499. Maximize Active Section with Trade I](https://leetcode.com/problems/maximize-active-section-with-trade-i/), we proved that after performing one operation, the maximum number of active sections in the string is

$\textit{cnt}_1+\textit{bestGain}$

where
* $\textit{cnt}_1$ is the number of characters $1$ in the string $s$.
* $\textit{bestGain}$ is the maximum sum of the lengths of two adjacent consecutive blocks of $0$s.

In this problem, however, we need to answer multiple queries.

For each query $[l,r]$, the operation is restricted to the substring $s[l..r]$. Note that the required answer is still the maximum number of active sections in the **entire string**, not just inside the substring. Therefore, for each query, we only need to compute the corresponding $\textit{bestGain}$ inside $s[l..r]$.

A brute-force solution would enumerate every consecutive block of $0$s inside the substring for every query, resulting in a time complexity of

$O(nq),$

which is too slow.

Therefore, we need a faster way to answer each query.

---

## Preprocessing Consecutive Blocks of $0$s

First, extract the lengths of all consecutive blocks of $0$s in the original string $s$.

Let
$\textit{zeroBlocks}=[z_0,z_1,\dots,z_{m-1}]$

where
* $m$ is the number of consecutive blocks of $0$s.
* $z_k$ is the length of the $k$-th consecutive block of $0$s.

For a query $[l,r]$, let
$\textit{subZeroBlocks}$

denote the array of consecutive $0$ block lengths inside the substring $s[l..r]$.

The following examples illustrate the possible forms of $\textit{subZeroBlocks}$.

![Slide 1](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_1_1_1.png)

![Slide 2](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_1_1_2.png)

![Slide 3](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_1_1_3.png)

![Slide 4](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_1_1_4.png)

![Slide 5](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_1_1_5.png)

![Slide 6](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_1_1_6.png)

Observe that, except for the first and last elements, $\textit{subZeroBlocks}$ is always a **contiguous subarray** of $\textit{zeroBlocks}$.

The reason is simple: a substring may cut through only the first and/or last block. Therefore, **only the lengths of the first and last blocks can change**.

Thus,

$\textit{subZeroBlocks}  =  [z_i',z_{i+1},\dots,z_{j-1},z_j'].$

Here,
* $z_i'$ is the actual length of the first consecutive block of $0$s inside $s[l..r]$, where $z_i' \le z_i$.
* $z_j'$ is the actual length of the last consecutive block of $0$s inside $s[l..r]$, where $z_j' \le z_j$.

Furthermore,
* $z_i'<z_i$ if and only if $s[l]='0'$ and $l$ is not the left endpoint of that block.
* $z_j'<z_j$ if and only if $s[r]='0'$ and $r$ is not the right endpoint of that block.

##### Computing $\textit{bestGain}$

From now on, for brevity, we refer to consecutive blocks of $0$s simply as **blocks**.

Since
$\textit{bestGain}  = \max(z_k+z_{k+1}),$

the answer for a query is simply the maximum of the following three cases.

#### Case 1

Use the first two blocks of $\textit{subZeroBlocks}$:
$val_1=z_i'+z_{i+1}.$

#### Case 2

Use the last two blocks:

$val_2=z_{j-1}+z_j'.$

#### Case 3

Use two adjacent blocks that lie completely inside the substring:
$val_3  = \max_{i+1\le k\le j-2} (z_k+z_{k+1}).$

Therefore,
$\textit{bestGain} = \max(val_1,val_2,val_3).$

##### Locating Blocks Efficiently

To compute these values efficiently, we need to quickly identify the corresponding blocks.

Preprocess two arrays:
* $\textit{blockLeft}[k]$: the left endpoint of the $k$-th block.
* $\textit{blockRight}[k]$: the right endpoint of the $k$-th block.

Since the blocks do not overlap, both arrays are strictly increasing, allowing us to locate the relevant blocks using binary search.

---

#### Processing a Query

For a query $[l,r]$:
First, binary search $\textit{blockRight}$ to find the first block satisfying
$\textit{blockRight}[i]\ge l.$

Suppose this block is
$[L_i,R_i].$

Then the actual length of the first block inside the substring is
$z_i' = R_i-\max(L_i,l)+1.$

Similarly, binary search $\textit{blockLeft}$ to find the last block satisfying
$\textit{blockLeft}[j]\le r.$

Suppose this block is
$[L_j,R_j].$

Then
$z_j' = \min(R_j,r)-L_j+1.$

To compute Case 3, define

$\textit{tmpSum}_k = z_k+z_{k+1}.$

Then
$$
val_3 = \max_{i+1\le k\le j-2}
\textit{tmpSum}_k.
$$

This becomes a standard range maximum query on the array $\textit{tmpSum}$, which can be answered using a segment tree.

---

#### Edge Cases

Several special cases should be handled.
* Binary search may fail, meaning $i>m-1$ or $j<0$. In this case, the substring contains no consecutive block of $0$s, so $\textit{bestGain}=0$.
* If $i\ge j$, the substring contains at most one consecutive block of $0$s, so there are no adjacent blocks and $\textit{bestGain}=0$.
* If the substring contains exactly two consecutive blocks of $0$s, then there are no complete interior blocks, making Case 3 irrelevant. In this case,

$\textit{bestGain}  = \textit{firstLen} + \textit{lastLen}.$

* If the original string contains fewer than two consecutive blocks of $0$s, no operation can increase the answer, so every query simply returns $\textit{cnt}_1$.

#### Implementation

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0] * (self.n << 2)

        if self.n:
            self.build(1, 0, self.n - 1)

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = self.arr[l]
            return

        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int) -> int:
        if L > R:
            return 0

        def _query(p: int, l: int, r: int) -> int:
            if L <= l and r <= R:
                return self.seg[p]

            mid = (l + r) >> 1
            res = 0

            if L <= mid:
                res = max(res, _query(p << 1, l, mid))

            if R > mid:
                res = max(res, _query(p << 1 | 1, mid + 1, r))

            return res

        return _query(1, 0, self.n - 1)

class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        blockLeft = []
        blockRight = []

        i = 0
        while i < n:
            st = i

            while i < n and s[i] == s[st]:
                i += 1

            if s[st] == "0":
                zeroBlocks.append(i - st)
                blockLeft.append(st)
                blockRight.append(i - 1)

        m = len(zeroBlocks)
        if (
            m < 2
        ):  # continuous 0 blocks less than 2 segments, return the answer directly
            return [cnt1] * len(queries)

        tmpSum = [zeroBlocks[i] + zeroBlocks[i + 1] for i in range(m - 1)]
        seg = SegmentTree(tmpSum)
        ans = []

        for l, r in queries:
            i = bisect_left(blockRight, l)
            j = bisect_right(blockLeft, r) - 1

            # at most 1 continuous block of 0s within the substring
            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue

            firstLen = (
                blockRight[i] - max(blockLeft[i], l) + 1
            )  # actual length of the first consecutive block of 0s in the substring

            lastLen = (
                min(blockRight[j], r) - blockLeft[j] + 1
            )  # actual length of the last consecutive block of 0s in the substring

            # exactly 2 consecutive 0 blocks within the substring
            if i + 1 == j:
                bestGain = firstLen + lastLen
                ans.append(cnt1 + bestGain)
                continue

            val1 = firstLen + zeroBlocks[i + 1]

            val2 = zeroBlocks[j - 1] + lastLen

            val3 = seg.query(i + 1, j - 2)

            bestGain = max(val1, val2, val3)

            ans.append(cnt1 + bestGain)

        return ans
```

#### Complexity Analysis

Let $n$ be the length of the string $s$.

- Time Complexity: $O(n+q\log n)$, including the preprocessing part such as building the segment tree, with a time complexity of $O(n)$. For each query:

- The time complexity of two binary searches is $O(\log n)$;

- The time complexity of one segment tree range maximum query is $O(\log n)$.

Therefore, the total time complexity is:

$O(n+q\log n)$

- Space Complexity: $O(n)$.
---

### Approach 2: Binary Search + Sparse Table

#### Intuition

In Approach 1, we use a segment tree to answer range maximum queries on the array `tmpSum`.

Note that in this problem, the array $\textit{tmpSum}$ does not change after preprocessing, so we can also use a Sparse Table to solve the static RMQ (Range Maximum Query) problem.

#### Implementation

```python
class SparseTable:
    def __init__(self, data: list):
        self.st = [list(data)]
        i, N = 1, len(self.st[0])
        while 2 * i <= N + 1:
            pre = self.st[-1]
            self.st.append(
                [max(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)]
            )
            i <<= 1

    def query(self, begin: int, end: int):
        if begin > end:
            return 0
        lg = (end - begin + 1).bit_length() - 1
        return max(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        blockLeft = []
        blockRight = []

        i = 0
        while i < n:
            st = i

            while i < n and s[i] == s[st]:
                i += 1

            if s[st] == "0":
                zeroBlocks.append(i - st)
                blockLeft.append(st)
                blockRight.append(i - 1)

        m = len(zeroBlocks)
        if (
            m < 2
        ):  # continuous 0 blocks less than 2 segments, return the answer directly
            return [cnt1] * len(queries)

        tmpSum = [zeroBlocks[i] + zeroBlocks[i + 1] for i in range(m - 1)]
        st = SparseTable(tmpSum)
        ans = []

        for l, r in queries:
            i = bisect_left(blockRight, l)
            j = bisect_right(blockLeft, r) - 1

            # at most 1 continuous block of 0s within the substring
            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue

            firstLen = (
                blockRight[i] - max(blockLeft[i], l) + 1
            )  # actual length of the first consecutive block of 0s in the substring

            lastLen = (
                min(blockRight[j], r) - blockLeft[j] + 1
            )  # actual length of the last consecutive block of 0s in the substring

            # exactly 2 consecutive 0 blocks within the substring
            if i + 1 == j:
                bestGain = firstLen + lastLen
                ans.append(cnt1 + bestGain)
                continue

            val1 = firstLen + zeroBlocks[i + 1]

            val2 = zeroBlocks[j - 1] + lastLen

            val3 = st.query(i + 1, j - 2)

            bestGain = max(val1, val2, val3)

            ans.append(cnt1 + bestGain)

        return ans
```

#### Complexity Analysis

- Time complexity: $O((n+q)\log n)$, where $n$ is the length of the string $s$. The preprocessing time complexity of the Sparse Table is $O(n\log n)$. For each query:

  - The time complexity of two binary searches is $O(\log n)$;

  - The time complexity of a single Sparse Table query is $O(1)$.

- Space complexity: $O(n\log n)$. The Sparse Table requires $O(n\log n)$ additional space.

### Approach 3: Mo's Algorithm (Not the expected complexity for this problem, optional reading)

#### Intuition

Mo's algorithm is a classic offline algorithm for answering multiple static range queries using a sliding window. By carefully ordering the queries, it reduces the total cost of moving the sliding window, achieving a time complexity on the order of the square root of the input size.

Since this problem involves multiple interval queries without any updates, it provides a good introduction to Mo's algorithm. However, note that this solution does **not** achieve the expected time complexity for this problem and is therefore **not guaranteed to pass all test cases**. It is included for readers who are interested in learning this technique.

The core idea behind Mo's algorithm is **square root decomposition**. We partition the string $s$ into blocks. For simplicity, let the block length be

$B=\sqrt{n}.$

A brute-force solution processes a query in $O(n)$ time, where $n$ is the length of the substring. Therefore, for queries whose interval length is at most $B$, we simply compute the answer by brute force, resulting in a total complexity of

$O(q\sqrt{n}).$

We only need to apply Mo's algorithm to queries whose interval length exceeds $B$. Since such queries are longer than one block, their left and right endpoints cannot lie in the same block.

We group these queries according to the block containing their **left endpoint**. Within each group, the queries are sorted in ascending order of their **right endpoint**.

> Since queries within the same group may be processed in any order, we can simply sort all remaining queries using the block ID of the left endpoint as the primary key and the right endpoint as the secondary key. As a result, queries belonging to the same group become consecutive, and their right endpoints are automatically sorted in ascending order.

Next, we process the groups one by one. For now, assume that every sliding window update and every query can be answered in $O(1)$ time.

Before processing each group, we initialize the sliding window and the auxiliary data structures required to answer the queries. Throughout the discussion below, we represent the sliding window using **open intervals**.

Suppose we are processing the queries whose left endpoints belong to the $k$-th block (where $k$ is zero-indexed). We initialize the sliding window as

$(L,R)=(kB-1,(k+1)B).$

That is, $L$ is initialized to the right endpoint of the $k$-th block, while $R$ is initialized to the left endpoint of the next block.

Since the interval is open, neither endpoint belongs to the window. Therefore, after initialization, the sliding window is empty.

At the same time, we initialize an array $\textit{subZeroBlocks}$ to record the lengths of consecutive blocks of $0$s inside the current window.

We now process the queries in each group from left to right.

---

#### Step 1: Expand the Right Endpoint

For a query $[l,r]$, we first expand the right endpoint until $R>r$.

During this process, new characters continuously enter the window from the right.

* If $s[R]='1'$, then $\textit{subZeroBlocks}$ remains unchanged.
* Otherwise, we update $\textit{subZeroBlocks}$.
* If $R$ is the first position of a consecutive block of $0$s in the original string, append a new element of value $1$ to the end of $\textit{subZeroBlocks}$, indicating that a new block of length $1$ has entered the window.
* Otherwise, increase the last element of $\textit{subZeroBlocks}$ by $1$, since the rightmost block has been extended.

---

#### Step 2: Expand the Left Endpoint

Next, expand the left endpoint until $L<l$.

During this process, new characters continuously enter the window from the left.
* If $s[L]='1'$, then $\textit{subZeroBlocks}$ remains unchanged.
* Otherwise, update $\textit{subZeroBlocks}$.
* If $L$ is the first position of a consecutive block of $0$s in the original string, prepend a new element of value $1$ to the front of $\textit{subZeroBlocks}$, indicating that a new block has entered the window.
* Otherwise, increase the first element of $\textit{subZeroBlocks}$ by $1$, since the leftmost block has been extended.

Using these rules, we can maintain $\textit{subZeroBlocks}$ dynamically as the sliding window expands.

Once both endpoints have been adjusted, the current window exactly corresponds to the query interval $[l,r]$. We can therefore compute $\textit{bestGain}$ from the current $\textit{subZeroBlocks}$ and answer the query.

---

#### Step 3: Roll Back the Left Endpoint

After answering the current query, we restore the left endpoint to its initial position so that the next query in the same group can be processed.

As the window shrinks from the left, characters continuously leave the window. We update $\textit{subZeroBlocks}$ using the reverse of the operations described in Step 2.

After restoring the left endpoint to the right boundary of the current block, we return to Step 1 to process the next query.

The overall workflow of Mo's algorithm is illustrated below.

![Slide 1](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_1.png)

![Slide 2](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_2.png)

![Slide 3](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_3.png)

![Slide 4](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_4.png)

![Slide 5](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_5.png)

![Slide 6](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_6.png)

![Slide 7](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_7.png)

![Slide 8](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_8.png)

![Slide 9](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_9.png)

![Slide 10](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_10.png)

![Slide 11](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_11.png)

![Slide 12](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_12.png)

![Slide 13](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_13.png)

![Slide 14](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_14.png)

![Slide 15](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_15.png)

![Slide 16](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_16.png)

![Slide 17](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_17.png)

![Slide 18](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_18.png)

![Slide 19](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_19.png)

![Slide 20](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_20.png)

![Slide 21](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_21.png)

![Slide 22](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_22.png)

![Slide 23](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_23.png)

![Slide 24](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_24.png)

![Slide 25](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_25.png)

![Slide 26](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_26.png)

![Slide 27](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_27.png)

![Slide 28](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_28.png)

![Slide 29](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_29.png)

![Slide 30](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_30.png)

![Slide 31](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_31.png)

![Slide 32](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_32.png)

![Slide 33](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_33.png)

![Slide 34](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_34.png)

![Slide 35](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_35.png)

![Slide 36](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_36.png)

![Slide 37](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_37.png)

![Slide 38](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_38.png)

![Slide 39](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_39.png)

![Slide 40](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_40.png)

![Slide 41](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_41.png)

![Slide 42](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_42.png)

![Slide 43](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_43.png)

![Slide 44](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_44.png)

![Slide 45](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_45.png)

![Slide 46](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_46.png)

![Slide 47](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_47.png)

![Slide 48](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_48.png)

![Slide 49](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_49.png)

![Slide 50](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_50.png)

![Slide 51](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_51.png)

![Slide 52](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_52.png)

![Slide 53](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_53.png)

![Slide 54](images/slideshow_3501_Maximize_Active_Section_with_Trade_II_2_3_54.png)

#### Implementation

```python
class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n, m = len(s), len(queries)
        cnt1 = s.count("1")

        left = [
-1
        ] * n  # left[i]: represents the length of the continuous block ending at position i, which is the same as s[i]
        right = [
-1
        ] * n  # right[i]: represents the length of the continuous block starting at position i with the same value as s[i]
        for i in range(n):
            left[i] = left[i - 1] + 1 if i > 0 and s[i - 1] == s[i] else 1
        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] + 1 if i < n - 1 and s[i + 1] == s[i] else 1

        ans = [-1] * m
        block_size = isqrt(n)

        longQueries = []  # query with length greater than block length

        def brute_force(l, r) -> int:
            i = l
            best = 0
            prev = -inf

            while i <= r:
                start = i

                while i <= r and s[i] == s[start]:
                    i += 1

                if s[start] == "0":
                    cur = i - start
                    best = prev + cur if prev + cur > best else best
                    prev = cur
            return best

        for i, (l, r) in enumerate(queries):
            if r - l + 1 > block_size:
                longQueries.append((l // block_size, l, r, i))
            else:
                ans[i] = cnt1 + brute_force(
                    l, r
                )  # queries shorter than block length, brute-force calculation

        # sort by the ID of the block where the left endpoint is located as the first keyword, and by the right endpoint as the second keyword
        longQueries.sort(key=lambda q: (q[0], q[2]))
        subZeroBlocks = deque()

        for i, (bid, l, r, qid) in enumerate(longQueries):
            if (
                i == 0 or bid > longQueries[i - 1][0]
            ):  # traverse to a new block, perform initialization operations
                L = (
                    bid + 1
                ) * block_size - 1  # L is initialized as the right endpoint of the block
                R = (
                    bid + 1
                ) * block_size  # R is initialized as the left endpoint of the next block
                subZeroBlocks.clear()
                bestGain = 0

            while R <= r:
                sz = min(r - R + 1, right[R])
                if s[R] == "0":
                    if subZeroBlocks and s[R - 1] == "0":
                        subZeroBlocks[-1] += sz
                    else:
                        subZeroBlocks.append(sz)
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(
                            subZeroBlocks[-1] + subZeroBlocks[-2], bestGain
                        )
                R += sz

            tmp_bestGain = bestGain  # before moving the left endpoint L, backup the value of bestGain
            tmp_firstValue = (
                subZeroBlocks[0] if subZeroBlocks else None
            )  # value of the first element of subZeroBlocks before moving the left endpoint
            cnt = 0  # the number of digits added from the left during the process of recording the movement of the left endpoint L

            while L >= l:
                sz = min(L - l + 1, left[L])
                if s[L] == "0":
                    if subZeroBlocks and s[L + 1] == "0":
                        subZeroBlocks[0] += sz
                    else:
                        subZeroBlocks.appendleft(sz)
                        cnt += 1
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(
                            subZeroBlocks[0] + subZeroBlocks[1], bestGain
                        )
                L -= sz

            ans[qid] = bestGain + cnt1  # answering inquiries

            # restore left endpoint L
            L = (bid + 1) * block_size - 1

            # restore bestGain
            bestGain = tmp_bestGain

            # restore subZeroBlocks
            for _ in range(cnt):
                subZeroBlocks.popleft()
            if tmp_firstValue:
                subZeroBlocks[0] = tmp_firstValue
        return ans
```

#### Complexity Analysis

- Time complexity: $O(q \log q + n \sqrt{n}+q \sqrt{n})$, which simplifies to $O(n \sqrt{n})$ when $q$ and $n$ are of the same order.

- Space complexity: $O(n)$.

Below, assume that both sliding window updates and query answering can be performed in $O(1)$ time. We first analyze the complexity of the algorithm under this assumption.

Since the queries within each group are sorted by non-decreasing right endpoint, the right endpoint $R$ only moves monotonically to the right.

We partition the string into blocks of length

$B=\sqrt{n},$

so the total number of blocks is approximately

$\textit{blockCount}=\frac{n}{B}=\sqrt{n}.$

Within each group, the right endpoint moves from its initial position to the end of the string at most once. Therefore, over all groups, the total number of movements of the right endpoint is

$O(n\cdot\textit{blockCount}) =$\mathcal{O}(n\sqrt{n})$.$

Now consider the left endpoint.

For every query, the left endpoint first expands until it reaches the query boundary and is then restored to its initial position. Since both the query's left endpoint and the initial position belong to the same block, the total movement of the left endpoint for a single query is at most twice the block length.

Therefore, the total complexity contributed by the left endpoint is

$O(2qB) =$\mathcal{O}(q\sqrt{n})$.$

As mentioned earlier, queries whose interval length does not exceed $B$ are handled using brute force, contributing another

$O(q\sqrt{n})$

time.

Finally, sorting all queries requires

$O(q\log q).$

Combining all components, the overall time complexity is

$O(q\log q+n\sqrt{n}+q\sqrt{n}).$

When $q$ and $n$ are of the same order, this simplifies to

$O(n\sqrt{n}).$

This is the central idea behind Mo's algorithm: by carefully reordering the queries, the total movement of the sliding window is minimized, making it possible to answer a large number of static interval queries efficiently.

---

In the previous discussion, we assumed that both sliding window updates and query answering can be performed in $O(1)$ time. We now explain how to achieve this.

Since elements need to be inserted and removed at both ends of $\textit{subZeroBlocks}$, a deque is a natural choice for maintaining it, allowing each update to be completed in $O(1)$ time.

However, maintaining only $\textit{subZeroBlocks}$ is not sufficient. To answer a query, we would still need to scan the entire deque to compute $\textit{bestGain}$, which is no longer an $O(1)$ operation.

Therefore, we need to maintain additional information that allows the answer to be updated incrementally.

#### Maintaining $\textit{bestGain}$

Recall that $\textit{bestGain}$ is defined as the maximum sum of two adjacent elements in $\textit{subZeroBlocks}$. Instead of recomputing it from scratch for every query, we maintain its value dynamically.

Before processing each group of queries, in addition to initializing an empty deque $\textit{subZeroBlocks}$, we also initialize

$\textit{bestGain}=0.$

Updating $\textit{bestGain}$ during window expansion is straightforward. Whenever one end of $\textit{subZeroBlocks}$ changes, only the newly formed adjacent pair near that end can affect the answer.

Suppose the current deque is

$\textit{subZeroBlocks} = [z_0,z_1,\dots,z_{m-1}].$

When appending or modifying an element on the right, we simply update

$\textit{bestGain}  = \max(\textit{bestGain},z_{m-2}+z_{m-1}).$

Similarly, when inserting or modifying an element on the left, we update

$\textit{bestGain} = \max(\textit{bestGain},z_0+z_1).$

As a result, every query can be answered in $O(1)$ time using the maintained value of $\textit{bestGain}$.

---

#### The Rollback Problem

The difficulty arises when restoring the left endpoint after answering a query.

During rollback, one of the following may happen:
* The leftmost element $z_0$ is removed from $\textit{subZeroBlocks}$.
* The value of $z_0$ decreases.

Suppose the current maximum is

$\textit{bestGain}  = z_0+z_1.$

After modifying or removing $z_0$, what should the new value of $\textit{bestGain}$ be?

Unfortunately, this cannot be determined in $O(1)$ time. We only know the current maximum, but we do not know the **second-largest** adjacent sum. Once the pair contributing the maximum disappears, we have no way to immediately determine the new maximum.

One possible solution is to maintain all adjacent sums in an ordered set or a lazy-deletion heap. Then, whenever an adjacent pair becomes invalid, the next largest value can be obtained efficiently.

However, every update would then require an additional

$O(\log n)$

time, increasing the complexity of every sliding window update. Can we avoid this?

---

#### Rollback Optimization

Notice how the algorithm is organized.

For every query, we first expand the left endpoint until it reaches the query boundary, answer the query, and then restore the left endpoint to its original position before processing the next query.

The key observation is that **no query is answered during the rollback process**.

Therefore, after rollback, we only need the maintained information to be exactly the same as it was before expanding the left endpoint.

In particular, the value of $\textit{bestGain}$ after rollback must be identical to its value before expansion, because the sliding window itself has been restored to the same state.

Thus, before expanding the left endpoint, we simply save the current value of

$\textit{bestGain}.$

After rollback, we restore it directly.

This completely avoids the need to maintain the "second-largest" adjacent sum, eliminating any additional data structures and keeping both sliding window updates and query answering at $O(1)$ time.

This idea is commonly known as **Rollback Mo's Algorithm**. Interested readers may continue exploring this technique by solving [3636. Threshold Majority Queries](https://leetcode.com/problems/threshold-majority-queries/description/i/).

---

#### Skipping Entire Blocks

We can further optimize the sliding window movement through preprocessing.

Specifically, preprocess two arrays:
* $\textit{left}[i]$: the length of the consecutive block ending at position $i$ that has the same character as $s[i]$.
* $\textit{right}[i]$: the length of the consecutive block starting at position $i$ that has the same character as $s[i]$.

For example,

$s=0011100$

gives

$\textit{left} = [1,2,1,2,3,1,2]$

and

$\textit{right} = [2,1,3,2,1,2,1].$

Both arrays can be computed in linear time.

With these arrays, we no longer need to move the sliding window one character at a time. Instead, we can jump directly over entire blocks of identical characters.

For example, suppose the current right endpoint is $R$.
* If $s[R]='1'$, then the entire consecutive block of $1$s contributes nothing to the answer and can be skipped.
* Otherwise, the length of the current consecutive block of $0$s is

$\textit{sz} = \min(\textit{right}[R],r-R+1),$

where the minimum is taken because the block may extend beyond the query boundary.

We can then move the right endpoint directly by

$R  \leftarrow R + \textit{sz},$

instead of advancing one position at a time.

The same optimization applies to the left endpoint. If the current left endpoint is $L$, then the length of the current consecutive block is

$\textit{sz} = \min(\textit{left}[L],L-l+1),$

and we update

$L  \leftarrow L - \textit{sz}.$

In this way, the sliding window skips entire blocks instead of individual characters.

This optimization makes the algorithm significantly faster in practice, especially on random data or strings containing long consecutive blocks.

---

#### Simplifying Rollback

The rollback process can be simplified even further.

Observe that expanding the left endpoint affects $\textit{subZeroBlocks}$ in only two ways:

* If the left endpoint falls inside an existing consecutive block of $0$s, only the first element of $\textit{subZeroBlocks}$ changes.
* Otherwise, one or more new blocks are inserted at the front.

Therefore, instead of undoing every operation one by one during rollback, we only need to record two pieces of information before expanding the left endpoint:

* the original value of the first element of $\textit{subZeroBlocks}$;
* the number of new elements inserted at the front.

During rollback, we simply:
* remove the recorded number of newly inserted elements from the front;
* restore the original value of the first element.

This restores $\textit{subZeroBlocks}$ to exactly the same state it had before the expansion, while keeping the rollback operation simple and efficient.

---