# Range Update, Point Query (BIT)

| | |
|---|---|
| **ID** | `fenwick_04` |
| **Category** | fenwick |
| **Complexity (required)** | $O(\log N)$ Query/Update |
| **Difficulty** | 6/10 |
| **Interview relevance** | 4/10 |
| **LeetCode Equivalent** | (Classic BIT Variant) |

## Problem statement

Given an array of size N initialized to 0, implement a Fenwick Tree that supports an inverted paradigm:
1. `range_update(left, right, delta)`: Add `delta` to **every single element** in the inclusive range `[left, right]`.
2. `point_query(index)`: Return the current value of the element at `index`.

Both operations must execute in strictly $O(\log N)$ time.

**Input:** A sequence of `range_update` and `point_query` operations.
**Output:** The results of the point queries.

## When to use it

- When you have a massive array where you frequently apply sweeping changes (e.g. "give +500 HP to all units in range 10-50"), but only need to know the status of individual units, not area sums.
- This perfectly inverts the standard Fenwick Tree (`fenwick_02`), which handles Point Updates and Range Queries!

## Approach

If we used a standard BIT, a `range_update` would require looping from `left` to `right` and calling `point_update` on each element. That takes $O(K log N)$ where K is the range length. If K is large, this degenerates to $O(N \log N)$.

**The Difference Array Approach:**
We change what the BIT physically stores. Instead of storing the array values, the BIT will store the **Difference Array**.
In a difference array, `diff[i] = arr[i] - arr[i-1]`.
This means the actual value of `arr[index]` is exactly equal to the prefix sum of the difference array from 0 to `index`!

With the BIT storing differences:
1. **Range Update `[L, R]` with `delta`:**
   - We only need to touch the difference array at two places!
   - `BIT.add(L, delta)`: This effectively adds `delta` to element L and *every element after it forever*.
   - `BIT.add(R + 1, -delta)`: This cancels out the `delta` for all elements strictly after R.
   - This takes exactly two $O(\log N)$ operations!
2. **Point Query at `index`:**
   - The value is simply the prefix sum of the difference array up to `index`.
   - `BIT.query_prefix(index)`.
   - This takes exactly one $O(\log N)$ operation!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_04: Range Update + Point Query (BIT).

Maintain an array of n integers under repeated
"""


def solve(arr, n, range_updates, point_queries, q):
    """Range add + point query via single BIT.

    Seed the BIT with the initial arr values (so the point
    query at idx returns arr[idx] + accumulated deltas).
    """
    bit = [0] * (n + 2)

    def update(i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Initialize the BIT with the DIFF array, not the values.
    # For the "range update, point query" technique, the BIT
    # stores a difference array so that point query at idx
    # gives the current value at idx.
    if n > 0:
        update(0, arr[0])
        for i in range(1, n):
            update(i, arr[i] - arr[i - 1])
    # Apply range updates: diff array approach.
    for l, r, val in range_updates:
        update(l, val)
        if r + 1 < n:
            update(r + 1, -val)
    # Point queries: read prefix sum at each index.
    out = []
    for (idx,) in point_queries:
        out.append(prefix(idx))
    return out
```

</details>

## Walk-through

Array of size 5 (Indices 0 to 4). Initially all 0.
BIT stores differences.

**1. Range Update [1, 3] with +10:**
- `_add(2, 10)`: Elements 1, 2, 3, 4 now logically have +10.
- `_add(5, -10)`: Element 4 has the +10 cancelled out.
- Logical Array State: `[0, 10, 10, 10, 0]`.

**2. Range Update [2, 4] with +5:**
- `_add(3, 5)`: Elements 2, 3, 4 get +5.
- `_add(6, -5)`: Out of bounds, ignored.
- Logical Array State: `[0, 10, 15, 15, 5]`.

**3. Point Query(index 2):**
- Prefix sum up to index 2 (1-based index 3).
- Sum = `_add(2)` + `_add(3)` effects.
- Result evaluates to exactly `15`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(N)$ |
| **Average** | $O(\log N)$ | $O(N)$ |
| **Worst** | $O(\log N)$ | $O(N)$ |

Both operations resolve to executing the standard BIT `_add` or `_query_prefix` functions a constant number of times (1 or 2). Therefore, all operations are strictly $O(\log N)$.
Space complexity is $O(N)$ for the array allocation.

## Variants & optimizations

- **Segment Tree with Lazy Propagation:** A Segment Tree can also do Range Updates in $O(\log N)$ time, but requires "Lazy Propagation" (storing pending updates in nodes and pushing them down to children during queries). The Fenwick Difference approach is roughly 5x shorter to code and strictly faster in constants!

## Real-world applications

- **Gaming:** Applying massive Area of Effect (AoE) status buffs/debuffs to units lined up in tower defense grids, then instantly querying individual unit stats during damage calculations.

## Related algorithms in cOde(n)

- **[fenwick_02 - Range Sum Query](fenwick_02_range-sum-query-bit.md)** — The exact inverse of this structure.
- **[fenwick_05 - Range Update Range Query](fenwick_05_range-update-range-query-bit.md)** — The ultimate fusion, combining this difference array logic with a second BIT to support BOTH range operations!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
