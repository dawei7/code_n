# Finding MK Average

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/finding-mk-average/) |
| Frontend ID | 1825 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Design, Queue, Heap (Priority Queue), Data Stream, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Maintain a stream of positive integers for fixed parameters `m` and `k`. Once at least `m` values have arrived, the current window is the last `m` stream elements. Sort a copy of that window, discard its smallest `k` elements and largest `k` elements, then average the remaining `m - 2*k` values using floor division. Duplicate occurrences are separate elements and may occupy several trimmed positions.

Implement `MKAverage(m, k)`, `addElement(num)`, and `calculateMKAverage()`. Adding beyond `m` values evicts the oldest value from the active window. A calculation before the window is full returns `-1`; otherwise it returns the trimmed, rounded-down average without changing the stream.

### Function Contract

**Inputs**

- `MKAverage(m, k)` initializes an empty stream with $3 \le m \le 10^5$ and $1 < 2k < m$.
- `addElement(num)` appends one value with $1 \le \texttt{num} \le 10^5$.
- `calculateMKAverage()` takes no arguments.
- At most $10^5$ method calls follow construction. Let $q$ denote their count and $U=10^5$ the value-domain limit.

**Return value**

- Construction and `addElement` return no value.
- `calculateMKAverage` returns `-1` before `m` values exist; afterward it returns the floor of the sum of the middle `m - 2*k` sorted window elements divided by that count.

### Examples

**Example 1**

- Operations: `["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]`
- Arguments: `[[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]`
- Output: `[null,null,null,-1,null,3,null,null,null,5]`

The first calculation is too early. Window `[3,1,10]` retains only `3`; after three fives arrive, the active window is `[5,5,5]`.

### Required Complexity

- **Time:** $O(U + q\log U)$
- **Space:** $O(m+U)$

<details>
<summary>Approach</summary>

#### General

**Represent the moving window and its value distribution**

Use a deque to retain arrival order for eviction. Over values 1 through $U$, maintain one Fenwick tree of occurrence counts and another of occurrence sums. Insertion adds one count and the value to the corresponding trees. When the deque exceeds `m`, remove its front value with inverse updates.

**Obtain sums by sorted rank without materializing a sort**

To compute the sum of the smallest `t` elements, use binary lifting on the count tree to find the value containing rank `t`. The sum tree gives the complete contribution of smaller values, and any remaining occurrences at the boundary contribute `remaining * value`. Duplicate values are therefore split correctly when a trim boundary passes through them.

**Extract the middle and floor its average**

The sum of sorted ranks `k + 1` through `m - k` is `sumSmallest(m - k) - sumSmallest(k)`. Divide that exact middle sum by `m - 2*k`. Neither calculation mutates the deque or trees, so repeated queries return the same result until another addition.

#### Complexity detail

Initializing the two trees costs $O(U)$. Each insertion and possible eviction performs a constant number of Fenwick updates in $O(\log U)$ time. Each full-window calculation performs two order-statistic searches and prefix-sum queries, also $O(\log U)$; an early calculation is $O(1)$. Across $q$ calls, total time is $O(U+q\log U)$. The deque stores at most $m$ values and the two trees store $O(U)$ entries, giving $O(m+U)$ space.

#### Alternatives and edge cases

- **Sort the window for every query:** It is simple and correct but costs $O(m\log m)$ per full calculation.
- **Three balanced multisets:** Maintaining the lowest `k`, middle, and highest `k` groups with the middle sum also gives logarithmic updates, but requires careful duplicate-aware rebalancing.
- **Before warm-up:** Return `-1` until exactly `m` values have been added.
- **Duplicate trim boundaries:** Remove occurrences, not distinct values; Fenwick counts preserve multiplicity.
- **Eviction:** Only the oldest of the previous `m` values leaves when one new value arrives.
- **Flooring:** Use integer floor division after summing all retained values.
- **Repeated calculation:** Do not remove, reorder, or otherwise mutate window state.
- **Extreme values:** Values 1 and $10^5$ are ordinary Fenwick indices and may appear repeatedly.

</details>
