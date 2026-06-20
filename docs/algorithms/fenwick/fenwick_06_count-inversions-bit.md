# Count Inversions (using BIT)

| | |
|---|---|
| **ID** | `fenwick_06` |
| **Category** | fenwick |
| **Complexity (required)** | $O(N \log N)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/) |

## Problem statement

Given an array of integers `arr`, find the total number of **inversions**.
An inversion is defined as a pair of indices `(i, j)` such that `i < j` but `arr[i] > arr[j]`.
While this is classically solved using a modified Merge Sort, you must solve it elegantly using a **Fenwick Tree (BIT)**.

**Input:** An array of integers `arr`.
**Output:** An integer representing the total count of inversions.

## When to use it

- Whenever you need to measure how "unsorted" an array is.
- The BIT approach is often easier to write from scratch in an interview than modifying a complex recursive Merge Sort, provided you understand the coordinate compression.

## Approach

Imagine we iterate through the array from right to left.
For the current element `arr[i]`, an inversion occurs for every element we have *already seen* (which means they are to the right of `i`) that is strictly *smaller* than `arr[i]`.
If we could somehow maintain a dynamic "frequency map" of elements we've seen, we just need to ask: **"How many elements in the map are less than `arr[i]`?"**

This is a **Prefix Sum Query**!
1. We can use a Fenwick Tree as a frequency array. `BIT[val]` stores the number of times we have seen `val`.
2. When we see `arr[i]`, we query the BIT for the sum of all frequencies from `1` to `arr[i] - 1`. This immediately tells us how many elements to the right are smaller!
3. We add that count to our global inversions total.
4. Then, we `update` the BIT by adding +1 to the frequency of `arr[i]`.

**Coordinate Compression:**
What if the numbers in the array are negative, or massive (e.g., 10^9)? A BIT array of size 10^9 would crash memory!
Since we only care about *relative* ordering (`<` or `>`), we can map the values to dense ranks from 1 to N.
`[100, -5, 4000, 100]` becomes `[2, 1, 3, 2]`.
Now the maximum value is N, and our BIT array fits perfectly in memory!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_06: Count Inversions (BIT).

Count the number of inversions in an array: pairs
"""


def solve(arr, n):
    """Inversion count via BIT, with value compression."""
    if n <= 1:
        return 0
    # Compress arr to 1..n by rank order.
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    compressed = [rank[v] for v in arr]
    # BIT of size n (max compressed value is n).
    bit = [0] * (n + 2)
    inv = 0
    for i in range(n - 1, -1, -1):
        v = compressed[i]
        # prefix sum of bit up to v-1.
        j = v - 1
        s = 0
        while j > 0:
            s += bit[j]
            j -= j & -j
        inv += s
        # Add 1 at index v.
        j = v
        while j <= n:
            bit[j] += 1
            j += j & -j
    return inv
```

</details>

## Walk-through

`arr = [8, 4, 2, 1]`

1. **Coordinate Compression:**
   - Sorted unique: `[1, 2, 4, 8]`.
   - Ranks: `{1:1, 2:2, 4:3, 8:4}`.
   - Array becomes: `[4, 3, 2, 1]`.
2. **BIT initialized to size 5:** `[0, 0, 0, 0, 0]`.
3. **Iterate Right to Left:**
   - **i = 3 (`val=1, rank=1`):**
     - Query `Prefix(1 - 1) = Prefix(0) = 0`. `inversions = 0`.
     - Add +1 to rank 1. `BIT` has `1` at rank 1.
   - **i = 2 (`val=2, rank=2`):**
     - Query `Prefix(2 - 1) = Prefix(1) = 1`. `inversions = 0 + 1 = 1`.
     - Add +1 to rank 2. `BIT` has `1` at rank 2.
   - **i = 1 (`val=4, rank=3`):**
     - Query `Prefix(3 - 1) = Prefix(2) = 2`. `inversions = 1 + 2 = 3`.
     - Add +1 to rank 3.
   - **i = 0 (`val=8, rank=4`):**
     - Query `Prefix(4 - 1) = Prefix(3) = 3`. `inversions = 3 + 3 = 6`.
     - Add +1 to rank 4.

Total inversions = 6. ✓ (The array is perfectly reversed, so (N x (N-1))/2 = 6).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Coordinate compression requires sorting the unique elements, taking $O(N \log N)$ time.
The backward iteration loops N times. Inside the loop, it performs a BIT query and a BIT update, taking $O(\log N)$ time each. Total time is $O(N \log N)$.
Space complexity is $O(N)$ for the coordinate compression dictionary and the BIT array.

## Variants & optimizations

- **Merge Sort Inversions:** The classical approach. During the merge step of Merge Sort, if an element from the right array is pulled before an element in the left array, it means the right element is smaller than *all remaining elements* in the left array! You simply add `len(left) - left_ptr` to the inversion count. This also takes $O(N \log N)$ and avoids coordinate compression entirely.

## Real-world applications

- **Collaborative Filtering:** Measuring the "Kendall tau distance" (which is mathematically derived from inversion count) between two users' ranked preference lists to recommend movies/products.

## Related algorithms in cOde(n)

- **[sort_03 - Merge Sort](../sorting/sort_03_merge-sort.md)** — The foundation for the alternative, non-BIT method of counting inversions.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
