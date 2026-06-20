# Build Fenwick Tree (Binary Indexed Tree)

| | |
|---|---|
| **ID** | `fenwick_01` |
| **Category** | fenwick |
| **Complexity (required)** | $O(N)$ or $O(N \log N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree) |

## Problem statement

Given an array `arr` of N integers, construct a **Fenwick Tree** (also known as a Binary Indexed Tree or BIT). 
A Fenwick Tree is a 1-indexed array `BIT` where each element stores the sum of a specific range of elements from the original array. This structure allows both updating elements and calculating prefix sums in $O(\log N)$ time.
You must construct this `BIT` array from the given `arr`.

**Input:** An array of integers `arr` of size N.
**Output:** An array `BIT` of size N + 1 representing the constructed Fenwick Tree.

## When to use it

- When you have an array that undergoes frequent element updates (e.g., `arr[i] += 5`) and you need to frequently query the sum of elements from index 0 to index `i`. 
- Fenwick Trees are vastly easier to code and use less memory than Segment Trees, but are slightly less flexible (they easily handle cumulative sums, but struggle with range maximums).

## Approach

A Fenwick Tree relies entirely on binary bit manipulation. 
The core idea: Every integer can be represented as a sum of powers of 2 (its binary representation). Similarly, a cumulative frequency can be represented as a sum of sub-frequencies.
In a BIT, the index `i` is responsible for a range of elements ending at `i`. The *length* of this range is exactly equal to the **value of the lowest set bit (LSB)** in the binary representation of `i`.
- Index `12` in binary is `1100`. The lowest set bit is `0100` (which is 4 in decimal). Therefore, `BIT[12]` stores the sum of the last 4 elements ending at index 12 (i.e., elements 9, 10, 11, 12).

**Building the Tree:**
The naive way to build it is to start with a `BIT` array of 0s, and for every element `arr[i]`, call the `update` function. This takes $O(N \log N)$ time.

**The $O(N)$ Optimization:**
We can build the tree in strictly $O(N)$ time!
1. Initialize a 1-indexed array `BIT` of size N+1.
2. Copy all elements of `arr` (which is 0-indexed) directly into `BIT` (which is 1-indexed).
3. Loop `i` from 1 to N.
4. At index `i`, the `BIT[i]` currently contains the correct sum for its range. We need to propagate this sum to the *next* node that is responsible for `i`.
5. The immediate parent of `i` in the BIT is mathematically `parent = i + (i & -i)`.
6. If `parent <= N`, simply add `BIT[i]` to `BIT[parent]`!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_01: Build Fenwick Tree.

bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the
number of trailing zeros in i.
"""


def solve(arr, n):
    if n == 0:
        return []
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    return bit
```

</details>

## Walk-through

`arr = [3, 2, -1, 6, 5, 4]`, N = 6.
Initialize `BIT`: `[0, 3, 2, -1, 6, 5, 4]`.

**i = 1:** `BIT[1]` is 3. Parent = `1 + (1 & -1)` = `1 + 1` = `2`.
`BIT[2] += BIT[1]` -> 2 + 3 = 5.
`BIT = [0, 3, 5, -1, 6, 5, 4]`.

**i = 2:** `BIT[2]` is 5. Parent = `2 + (2 & -2)` = `2 + 2` = `4`.
`BIT[4] += BIT[2]` -> 6 + 5 = 11.
`BIT = [0, 3, 5, -1, 11, 5, 4]`.

**i = 3:** `BIT[3]` is -1. Parent = `3 + (3 & -3)` = `3 + 1` = `4`.
`BIT[4] += BIT[3]` -> 11 + (-1) = 10.
`BIT = [0, 3, 5, -1, 10, 5, 4]`.

**i = 4:** `BIT[4]` is 10. Parent = `4 + (4 & -4)` = `4 + 4` = `8`.
`8 > N(6)`. Do nothing.

**i = 5:** `BIT[5]` is 5. Parent = `5 + (5 & -5)` = `5 + 1` = `6`.
`BIT[6] += BIT[5]` -> 4 + 5 = 9.
`BIT = [0, 3, 5, -1, 10, 5, 9]`.

**i = 6:** `BIT[6]` is 9. Parent = `6 + (6 & -6)` = `6 + 2` = `8`.
`8 > N`. Do nothing.

Final `BIT` = `[0, 3, 5, -1, 10, 5, 9]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The optimized construction visits each index exactly once and does an $O(1)$ bitwise calculation and addition. Total time is strictly $O(N)$.
Space complexity is $O(N)$ to store the BIT array of size N+1.

## Variants & optimizations

- **Segment Tree Construction:** If you actually need range minimums/maximums instead of just sums, you must build a Segment Tree. Segment Trees also build in $O(N)$ time but require $O(4N)$ memory overhead compared to the Fenwick Tree's $O(N)$.

## Real-world applications

- **Database Analytics:** Powering "rolling sum" columns in OLAP databases where rows are frequently updated.
- **Data Compression:** Maintaining dynamic frequency tables for Adaptive Arithmetic Coding.

## Related algorithms in cOde(n)

- **[fenwick_02 - Range Sum Query](fenwick_02_range-sum-query-bit.md)** — How to actually use the array we just built to answer prefix sum queries.
- **[segment_tree_01 - Segment Tree Build](../segment_tree/segtree_01_point-update-range-query.md)** — The heavier, more versatile alternative to Fenwick Trees.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
