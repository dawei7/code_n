# Range Sum Query (Point Update)

| | |
|---|---|
| **ID** | `fenwick_02` |
| **Category** | fenwick |
| **Complexity (required)** | $O(\log N)$ Query, $O(\log N)$ Update |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem statement

Given an array `arr` and its pre-constructed Fenwick Tree (BIT), implement two operations:
1. `update(index, value)`: Update the original array such that `arr[index] = value`.
2. `query(left, right)`: Return the sum of elements in `arr` from index `left` to `right` (inclusive).

You must perform both operations in strictly $O(\log N)$ time.

**Input:** A pre-built `BIT` array, and a sequence of `update` and `query` operations.
**Output:** The result of the `query` operations.

## When to use it

- When array elements are constantly changing (mutating) and you need to query the sum of a sub-array continuously.
- A standard prefix sum array (`sum[i] = sum[i-1] + arr[i]`) answers queries in $O(1)$, but updating a single element takes $O(N)$ because you have to rewrite the entire prefix array! Fenwick balances this perfectly.

## Approach

**Point Update:**
If the original array `arr` at index `i` changes its value, we don't set the BIT directly. We calculate the *delta* (difference) between the new value and the old value.
We must add this `delta` to `BIT[i]`, and to every parent node in the BIT that is responsible for `i`!
To traverse up the tree to all responsible parents, we use the rule: `index = index + (index & -index)`.
We loop until the index exceeds the size of the BIT.

**Prefix Sum Query:**
To find the sum from 0 to i, we start at `BIT[i]` (which holds the sum of a specific chunk of the array ending at i).
To get the remaining chunks, we strip off the lowest set bit to find the previous chunk: `index = index - (index & -index)`.
We accumulate these values and loop until the index reaches 0.

**Range Query [left, right]:**
Just like standard prefix sum arrays, the sum of `[left, right]` is simply:
`PrefixSum(right) - PrefixSum(left - 1)`.

*(Remember: The BIT is 1-indexed, while the original array is usually 0-indexed. Always add 1 to the array index before passing it to the BIT operations!)*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_02: Range Sum Query (BIT).

Build a BIT, apply updates, then answer each range-sum query.
"""


def solve(arr, n, updates, queries, q):
    if n == 0:
        return [0] * q
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]

    def update(i, delta):
        i += 1
        while i <= n:
            bit[i] += delta
            i += i & -i

    work = list(arr)
    for idx, val in updates:
        delta = val - work[idx]
        work[idx] = val
        update(idx, delta)

    out = []
    for l, r in queries:
        def prefix(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        out.append(prefix(r) - (prefix(l - 1) if l > 0 else 0))
    return out
```

</details>

## Walk-through

`arr = [3, 2, -1, 6]`. BIT is `[0, 3, 5, -1, 10]`.

**1. Query Range [0, 2]:**
- We need `_query_prefix(2 + 1)` - `_query_prefix(0)`.
- `_query_prefix(3)`:
  - `total += BIT[3]` (-1). `total = -1`.
  - `i = 3 - (3 & -3) = 3 - 1 = 2`.
  - `total += BIT[2]` (5). `total = 4`.
  - `i = 2 - (2 & -2) = 2 - 2 = 0`. Loop ends. Return 4.
- Sum is 4 - 0 = 4. ✓ (3 + 2 - 1 = 4).

**2. Update(index 1, value 5):**
- Old `arr[1]` is 2. New is 5. `delta = 3`.
- `_add(1 + 1, 3)` -> `_add(2, 3)`.
  - `BIT[2] += 3` -> 5 + 3 = 8.
  - `i = 2 + (2 & -2) = 4`.
  - `BIT[4] += 3` -> 10 + 3 = 13.
  - `i = 4 + 4 = 8`. 8 > 4. Loop ends.
- BIT is now `[0, 3, 8, -1, 13]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(N)$ |
| **Average** | $O(\log N)$ | $O(N)$ |
| **Worst** | $O(\log N)$ | $O(N)$ |

The number of set bits in an index i determines the number of iterations in the `while` loops. The maximum index is N. An integer N has at most ~= log_2(N) bits. Thus, traversing up or down the tree requires strictly bounded $O(\log N)$ steps.
Space complexity is $O(N)$ for the tree storage.

## Variants & optimizations

- **Segment Tree:** A Segment tree takes identical $O(\log N)$ time, but allows you to query ranges for Maximum, Minimum, GCD, and arbitrary custom associative functions. The Fenwick Tree ONLY works perfectly for operations that have an inverse (like addition has subtraction, XOR has XOR), because `Range(L,R)` relies on subtracting `Prefix(L-1)`!

## Real-world applications

- **Financial Ledgers:** Quickly pulling the net sum of transactions within any date range while allowing historical transaction corrections to update the ledger in real-time.

## Related algorithms in cOde(n)

- **[fenwick_01 - Build Tree](fenwick_01_build-fenwick-tree.md)** — The prerequisite construction step.
- **[segtree_01 - Segment Tree Query](../segment_tree/segtree_01_point-update-range-query.md)** — The exact same problem solved with a slightly heavier data structure.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
