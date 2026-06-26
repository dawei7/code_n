# Range Update, Range Query (Dual BIT)

| | |
|---|---|
| **ID** | `fenwick_05` |
| **Category** | fenwick |
| **Complexity (required)** | $O(\log N)$ Query/Update |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **LeetCode Equivalent** | (Advanced Competitive Programming) |

## Problem statement

Given an array of size N initialized to 0, implement a data structure that supports BOTH:
1. `range_update(left, right, delta)`: Add `delta` to every element in the inclusive range `[left, right]`.
2. `range_query(left, right)`: Return the sum of all elements in the inclusive range `[left, right]`.

Both operations must execute in strictly $O(\log N)$ time. While a Segment Tree with Lazy Propagation can do this naturally, you must achieve it using **Fenwick Trees (BITs)** to minimize memory overhead and maximize constant-factor speed.

**Input:** A sequence of `range_update` and `range_query` operations.
**Output:** The results of the range queries.

## When to use it

- In highly constrained competitive programming environments where a Segment Tree uses too much memory or is slightly too slow to pass strict time limits.
- A brilliant demonstration of advanced algebraic manipulation of data structures.

## Approach

Let's look at the math of a Difference Array (from `fenwick_04`).
If we add `D` to the range `[L, R]`, our difference array updates are `Diff[L] += D` and `Diff[R+1] -= D`.
What happens when we ask for the Prefix Sum up to index `X`?
The true value of element `i` is \sum_{j=1}^{i} Diff[j].
Therefore, the Prefix Sum up to `X` is:
PrefixSum(X) = \sum_{i=1}^{X} \text{value}[i] = \sum_{i=1}^{X} \sum_{j=1}^{i} Diff[j]

Notice that Diff[1] is added X times. Diff[2] is added X-1 times. Diff[i] is added (X - i + 1) times!
We can algebraically rewrite this summation:
PrefixSum(X) = \sum_{i=1}^{X} Diff[i] x (X - i + 1)
PrefixSum(X) = \sum_{i=1}^{X} (Diff[i] x X + Diff[i]) - \sum_{i=1}^{X} (Diff[i] x i)
PrefixSum(X) = (X + 1) \sum_{i=1}^{X} Diff[i] - \sum_{i=1}^{X} (Diff[i] x i)

**The Dual BIT Insight:**
This equation has two distinct summations!
1. \sum Diff[i] — This is just a standard BIT maintaining the Difference Array (`BIT1`)!
2. \sum (Diff[i] x i) — This requires a **second BIT** (`BIT2`) that maintains the exact same Difference Array, but multiplied by the index i!

To query the Prefix Sum up to `X`, we just ask both BITs for their prefix sums and plug them into the equation:
`PrefixSum(X) = (X + 1) * BIT1.query(X) - BIT2.query(X)`

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_05: Range Update + Range Query (BIT).

Maintain an array of n integers under repeated
"""


def solve(arr, n, range_updates, range_queries, q):
    """Range add + range sum via two BITs.

    Seed both BITs with the initial arr values so the
    range sum reflects the actual current array.
    """
    INF = n + 5
    bit1 = [0] * (n + 2)
    bit2 = [0] * (n + 2)

    def update(bit, i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(bit, i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def range_update(l, r, val):
        update(bit1, l, val)
        if r + 1 < n:
            update(bit1, r + 1, -val)
        update(bit2, l, val * (l - 1))
        if r + 1 < n:
            update(bit2, r + 1, -val * r)

    def prefix_sum(x):
        # sum of [0, x]
        if x < 0:
            return 0
        return prefix(bit1, x) * x - prefix(bit2, x)

    # Initialize: each initial value is a point update (a
    # range update of length 1). This seeds both BITs so the
    # formula (bit1.prefix(x) * x - bit2.prefix(x)) yields
    # sum of arr[0..x] including the initial values.
    for i in range(n):
        range_update(i, i, arr[i])
    for l, r, val in range_updates:
        range_update(l, r, val)
    out = []
    for l, r in range_queries:
        out.append(prefix_sum(r) - prefix_sum(l - 1))
    return out
```

</details>

## Walk-through

*(Conceptual)*
Array size 5. Initially all 0.
1. **Range Update [1, 3] with +10:**
   - `L=2, R=4`. `delta=10`.
   - `BIT1`: Add `10` at index 2. Add `-10` at index 5.
   - `BIT2`: Add `10 * 2 = 20` at index 2. Add `-10 * 5 = -50` at index 5.

2. **Range Query [2, 4]:** (Indices 3 to 5)
   - `_get_prefix_sum(5)`:
     - `BIT1` prefix(5) = `10 - 10 = 0`.
     - `BIT2` prefix(5) = `20 - 50 = -30`.
     - `Sum(5) = (5 + 1) * 0 - (-30) = 30`. (Elements 1,2,3 got +10. Total sum is 30). ✓
   - `_get_prefix_sum(2)`:
     - `BIT1` prefix(2) = `10`.
     - `BIT2` prefix(2) = `20`.
     - `Sum(2) = (2 + 1) * 10 - 20 = 10`. (Only element 1 got +10 up to index 2). ✓
   - **Range Result:** `Sum(5) - Sum(2) = 30 - 10 = 20`.
   - Elements at array indices 2, 3, 4 are `10, 10, 0`. Sum is 20! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(N)$ |
| **Average** | $O(\log N)$ | $O(N)$ |
| **Worst** | $O(\log N)$ | $O(N)$ |

Every update touches two BITs, taking 2 x $O(\log N)$. Every query touches two BITs, taking 2 x $O(\log N)$. Thus, all operations are strictly bounded by $O(\log N)$.
Space complexity is $O(N)$ for the two arrays, which is significantly smaller than the memory required for a Lazy Segment Tree.

## Variants & optimizations

- **Segment Tree with Lazy Propagation:** As mentioned, the alternative structure. Lazy Segment Trees are easier to conceptualize and extend to max/min queries, whereas this Dual BIT trick ONLY works for summations.

## Real-world applications

- **High-Frequency Trading:** Maintaining aggregate limits on tiered pricing structures where continuous blocks of prices are updated simultaneously, and risk systems demand nanosecond query latency.

## Related algorithms in cOde(n)

- **[fenwick_04 - Range Update Point Query](fenwick_04_range-update-point-query-bit.md)** — The foundation of the Difference Array math used here.
- **[segtree_04 - Lazy Propagation](../segment_tree/segtree_04_lazy-propagation.md)** — The Segment Tree approach to solving this exact same problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
