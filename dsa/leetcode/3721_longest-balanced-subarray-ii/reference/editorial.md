### Approach: Prefix Sum + Segment Tree

#### Intuition

The key idea is to convert the notion of "distinct types of odd elements" and "distinct types of even elements" from the problem statement into a numerical form that can be efficiently processed by a data structure. Specifically, for each distinct value, we assign a contribution of `-1` (if odd) or `+1` (if even) at its **first occurrence** only. Subsequent occurrences of the same value do not add to the prefix sum, since they do not introduce a new distinct element. Under this transformation, a subarray is **balanced** if and only if the prefix sum difference across it is `0`, meaning the number of distinct even values equals the number of distinct odd values within that range.

After this transformation, the array becomes a difference array consisting only of `-1` and `+1`. By computing the prefix sum array, we observe that whenever a prefix sum equals `0`, the corresponding prefix subarray is balanced. More generally, for a fixed left boundary, the right boundary of the longest balanced subarray corresponds to the **rightmost position where the prefix sum is equal to the prefix sum at the left boundary**.

Since the prefix sum changes by at most `1` at each step, it satisfies a discrete version of the intermediate value theorem. This property allows us to use a segment tree to efficiently locate the **rightmost occurrence of `0`** in a given range. The search works as follows:

1. Maintain both the minimum and maximum prefix sum values for each segment.
2. Check whether `0` lies within the range `[min, max]` of the right child. If it does, recurse into the right child.
3. Otherwise, recurse into the left child.

Because of the discrete intermediate value property, checking the minimum and maximum values is sufficient to determine whether `0` exists in a segment, allowing each query to be completed in $O(\log n)$ time.

Next, we iterate over all possible left boundaries. Let the current left boundary be index $i$, and let the current maximum length of a balanced subarray be $l$. As an optimization, we start searching for the right boundary from index $i + l$, since any shorter subarray cannot improve the current answer.

The remaining challenge is handling the removal of the contribution of the element at the previous left boundary as we move the left pointer forward.

Recall that in a difference array, a nonzero value at position $i$ contributes to all prefix sums from position $i$ onward. For example, if the contribution at position $1$ is `-1`, it decreases the values of $S_1, S_2, \dots, S_n$ by `1`. More generally, if an element appears at positions $p_1$ and $p_2$, its contribution at $p_1$ affects the interval $[p_1, p_2 - 1]$, while the contribution at $p_2$ affects the interval $[p_2, \dots]$.

$$[ \dots, 0, \underbrace{1, 1, \dots, 1}*{\text{contributed by the first } x},
\underbrace{1, 1, \dots, 1}*{\text{contributed by the second } x}, \dots ]$$

Therefore, we record all positions where each element appears using a queue. When the left boundary moves forward, we determine the interval over which the removed element contributes and subtract its effect from that interval. Since this is a range update, it can be efficiently handled using the segment tree with lazy propagation.

Putting everything together, we first compute the prefix sums and record the occurrence positions of each element. Then, we iterate over all possible left boundaries, dynamically update the prefix sums using the segment tree, query the rightmost position where the prefix sum is `0`, and update the global maximum length accordingly.

#### Implementation

```python
class LazyTag:
    def __init__(self):
        self.to_add = 0

    def add(self, other):
        self.to_add += other.to_add
        return self

    def has_tag(self):
        return self.to_add != 0

    def clear(self):
        self.to_add = 0

class SegmentTreeNode:
    def __init__(self):
        self.min_value = 0
        self.max_value = 0
        self.lazy_tag = LazyTag()

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
        self._build(data, 1, self.n, 1)

    def add(self, l, r, val):
        tag = LazyTag()
        tag.to_add = val
        self._update(l, r, tag, 1, self.n, 1)

    def find_last(self, start, val):
        if start > self.n:
            return -1
        return self._find(start, self.n, val, 1, self.n, 1)

    def _apply_tag(self, i, tag):
        self.tree[i].min_value += tag.to_add
        self.tree[i].max_value += tag.to_add
        self.tree[i].lazy_tag.add(tag)

    def _pushdown(self, i):
        if self.tree[i].lazy_tag.has_tag():
            tag = LazyTag()
            tag.to_add = self.tree[i].lazy_tag.to_add
            self._apply_tag(i << 1, tag)
            self._apply_tag((i << 1) | 1, tag)
            self.tree[i].lazy_tag.clear()

    def _pushup(self, i):
        self.tree[i].min_value = min(
            self.tree[i << 1].min_value, self.tree[(i << 1) | 1].min_value
        )
        self.tree[i].max_value = max(
            self.tree[i << 1].max_value, self.tree[(i << 1) | 1].max_value
        )

    def _build(self, data, l, r, i):
        if l == r:
            self.tree[i].min_value = data[l - 1]
            self.tree[i].max_value = data[l - 1]
            return

        mid = l + ((r - l) >> 1)
        self._build(data, l, mid, i << 1)
        self._build(data, mid + 1, r, (i << 1) | 1)
        self._pushup(i)

    def _update(self, target_l, target_r, tag, l, r, i):
        if target_l <= l and r <= target_r:
            self._apply_tag(i, tag)
            return

        self._pushdown(i)
        mid = l + ((r - l) >> 1)
        if target_l <= mid:
            self._update(target_l, target_r, tag, l, mid, i << 1)
        if target_r > mid:
            self._update(target_l, target_r, tag, mid + 1, r, (i << 1) | 1)
        self._pushup(i)

    def _find(self, target_l, target_r, val, l, r, i):
        if self.tree[i].min_value > val or self.tree[i].max_value < val:
            return -1

        if l == r:
            return l

        self._pushdown(i)
        mid = l + ((r - l) >> 1)

        if target_r >= mid + 1:
            res = self._find(target_l, target_r, val, mid + 1, r, (i << 1) | 1)
            if res != -1:
                return res

        if l <= target_r and mid >= target_l:
            return self._find(target_l, target_r, val, l, mid, i << 1)

        return -1

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        occurrences = defaultdict(deque)

        def sgn(x):
            return 1 if x % 2 == 0 else -1

        length = 0
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = sgn(nums[0])
        occurrences[nums[0]].append(1)

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1]
            occ = occurrences[nums[i]]
            if not occ:
                prefix_sum[i] += sgn(nums[i])
            occ.append(i + 1)

        seg = SegmentTree(prefix_sum)
        for i in range(len(nums)):
            length = max(length, seg.find_last(i + length, 0) - i)
            next_pos = len(nums) + 1
            occurrences[nums[i]].popleft()
            if occurrences[nums[i]]:
                next_pos = occurrences[nums[i]][0]

            seg.add(i + 1, next_pos - 1, -sgn(nums[i]))

        return length
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n \log n)$.

  Computing prefix sums and maintaining element positions require $O(n \log n)$. Building the segment tree takes $O(n \log n)$. Each iteration performs a constant number of segment tree operations and map accesses, each taking $O(\log n)$. Therefore, the total time complexity is $O(n \log n)$.

- Time complexity: $O(n)$.

  The segment tree, prefix sum array, and auxiliary data structures together require $O(n)$ space.

---