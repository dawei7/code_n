# Find Kth Largest XOR Coordinate Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1738 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Bit Manipulation, Sorting, Heap (Priority Queue), Matrix, Prefix Sum, Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/) |

## Problem Description

### Goal

The nonnegative integer `matrix` has $m$ rows and $n$ columns. The value of coordinate `(a,b)` is the bitwise XOR of every `matrix[i][j]` in the inclusive rectangle from `(0,0)` to `(a,b)`.

Compute all $mn$ coordinate values conceptually and return their $k$th largest value, where ranks are one-based and repeated values occupy separate ranks. The dimensions are each between $1$ and $1000$, matrix entries are at most $10^6$, and $1 \le k \le mn$.

### Function Contract

**Inputs**

- `matrix`: a nonempty rectangular matrix of nonnegative integers.
- `k`: the one-based descending rank to retrieve.

Let $C=mn$ be the number of matrix cells.

**Return value**

- Return the $k$th largest prefix-rectangle XOR value, counting duplicates separately.

### Examples

**Example 1**

- Input: `matrix = [[5,2],[1,6]], k = 1`
- Output: `7`
- Explanation: The four coordinate values are `5,7,4,0`; the largest is $7$.

**Example 2**

- Input: `matrix = [[5,2],[1,6]], k = 2`
- Output: `5`
- Explanation: Sorting the coordinate values in descending order gives `7,5,4,0`.

**Example 3**

- Input: `matrix = [[5,2],[1,6]], k = 3`
- Output: `4`
- Explanation: The prefix rectangle ending at `(1,0)` has XOR `5 ^ 1 = 4`.

### Required Complexity

- **Time:** $O(C\log k)$
- **Space:** $O(n+k)$

<details>
<summary>Approach</summary>

#### General

**Extend the prefix recurrence with XOR**

Let `current[j]` represent the coordinate value for the current row and column $j-1$, while `previous[j]` stores the row above. The inclusive prefix value at a cell is the matrix entry XOR the prefix above, the prefix to the left, and the upper-left prefix. The upper-left term must be included because it appears in both other rectangles and XORing it a third time leaves it counted once.

**Keep only one prefix row**

Compute a fresh prefix row from left to right, then replace the previous row. This preserves every dependency needed by the next cell while avoiding an $m \times n$ prefix matrix.

**Select with a bounded min-heap**

Maintain the largest $k$ coordinate values seen so far in a min-heap. Push until it contains $k$ values; afterward, replace its root only when a larger coordinate value arrives. At the end, every discarded value is no larger than the heap's minimum, so the root is exactly the $k$th largest value. Equal values remain separate heap entries and therefore retain their separate ranks.

#### Complexity detail

Every one of the $C=mn$ cells performs constant prefix-XOR work and at most one $O(\log k)$ heap update, giving $O(C\log k)$ time. Two prefix rows use $O(n)$ space and the selection heap uses $O(k)$, for $O(n+k)$ auxiliary space.

#### Alternatives and edge cases

- **Sort all coordinate values:** This is straightforward but takes $O(C\log C)$ time and $O(C)$ storage.
- **Quickselect:** Collecting all values and selecting in expected $O(C)$ time is valid, but still stores all $C$ values and requires careful pivot handling.
- **Full 2D prefix matrix:** It simplifies indexing but consumes $O(C)$ space when two rows suffice.
- **Single cell:** Its matrix value is the only coordinate value and must be returned.
- **Duplicate coordinate values:** They are counted at distinct ranks rather than deduplicated.
- **Rank one:** The heap contains only the maximum seen so far.
- **Rank $C$:** The result is the minimum coordinate value, and the heap may contain all values.

</details>
