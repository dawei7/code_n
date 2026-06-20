# K-th Smallest / Order Statistic (Binary Lifting)

| | |
|---|---|
| **ID** | `fenwick_07` |
| **Category** | fenwick |
| **Complexity (required)** | $O(log M)$ Query |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **LeetCode Equivalent** | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) (Advanced Variant) |

## Problem statement

Given a dynamic collection of numbers where you can continuously insert or delete elements, support a query to find the **K-th smallest element** in the collection (the k-th order statistic).
While a balanced Binary Search Tree (like an AVL or Red-Black Tree augmented with subtree sizes) solves this naturally, implementing one from scratch in an interview is virtually impossible.
You must solve this elegantly by leveraging a **Fenwick Tree** combined with a technique called **Binary Lifting** to answer the query in strictly $O(log M)$ time.

**Input:** A sequence of insertions and queries for the K-th smallest element.
**Output:** The values answering the queries.

## When to use it

- To find rolling medians or specific percentiles in a highly dynamic stream of data.
- Binary Lifting on a Fenwick Tree is a profound "secret weapon" in competitive programming to avoid writing hundreds of lines of AVL tree code.

## Approach

As in `fenwick_06`, we use the Fenwick Tree as a **Frequency Array**. `BIT[val]` stores how many times `val` exists in our collection.
The Prefix Sum up to `val` tells us exactly how many elements in the collection are \le val.
To find the K-th smallest element, we want to find the **smallest index `val` such that `PrefixSum(val) >= K`**.

A naive approach would be to binary search the index 1 \dots M. For each guess `mid`, we query the BIT for the prefix sum. This takes $O(log M)$ for the binary search, and $O(log M)$ for the prefix query, resulting in $O(log^2 M)$.

**Binary Lifting ($O(log M)$):**
We can merge the binary search *directly into the BIT traversal structure*!
1. We start at `index = 0` and `current_sum = 0`.
2. We look at the largest power of 2 that fits in our maximum limit (e.g., 2^{19}). Let's call this `step`.
3. We check the BIT at `index + step`. Because of how Fenwick Trees are constructed, `BIT[index + step]` conveniently stores the exact frequency sum of the block from `index` to `index + step`!
4. If `current_sum + BIT[index + step] < K`:
   - It means the K-th element is strictly *larger* than `index + step`.
   - We confidently jump forward! `index += step`.
   - We accumulate the sum: `current_sum += BIT[index]`.
5. If the sum is \ge K, we do NOT jump.
6. Halve the `step` (e.g., to 2^{18}) and repeat until `step` becomes 0.
7. The target index is `index + 1`!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_07: K-th Smallest (Order-Statistic BIT).

Given a frequency array freq[1..n] (how many times
"""


def solve(freq, n, k):
    """K-th smallest via order-statistic BIT (binary lifting)."""
    total = sum(freq)
    if k < 1 or k > total:
        return -1
    if n == 0:
        return -1
    # Build BIT.
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = freq[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    # Binary lifting: find largest idx with BIT.prefix(idx) < k.
    # The k-th smallest value is then idx + 1 (since the BIT
    # is 1-indexed and BIT[i] represents the count of value i).
    # The descent uses STRICT less-than: we take a step only
    # if bit[pos + bitmask] < (k - bit.prefix(pos)), so that
    # bit.prefix(pos) stays strictly less than k. The k-th
    # value is the smallest idx with prefix >= k, which is
    # (largest pos with prefix < k) + 1.
    idx = 0
    bitmask = 1
    while bitmask << 1 <= n:
        bitmask <<= 1
    remaining = k
    while bitmask > 0:
        nxt = idx + bitmask
        if nxt <= n and bit[nxt] < remaining:
            remaining -= bit[nxt]
            idx = nxt
        bitmask >>= 1
    return idx + 1
```

</details>

## Walk-through

*(Conceptual)*
`max_val = 15`. `max_power = 8`.
Insert values: `[2, 2, 5, 8]`.
We want the `K = 3` rd smallest element (which should be 5).
BIT array is populated with these frequencies.

1. `step = 8`. Check `BIT[8]` (which holds the sum of frequencies 1 through 8). Let's say `BIT[8] = 4` (since all four elements are \le 8).
   - `0 + 4 < 3` is FALSE. Do not jump. `index = 0`.
2. `step = 4`. Check `BIT[4]` (holds sum 1 through 4). Value is 2 (the two `2`s).
   - `0 + 2 < 3` is TRUE!
   - Jump! `index = 4`. `current_sum = 2`.
3. `step = 2`. Check `BIT[4 + 2 = 6]`. (Holds sum of 5 through 6). Value is 1 (the `5`).
   - `current_sum (2) + BIT[6] (1) < 3` is FALSE (3 < 3 is false).
   - Do not jump. `index = 4`.
4. `step = 1`. Check `BIT[4 + 1 = 5]`. (Holds sum of 5). Value is 1.
   - `current_sum (2) + BIT[5] (1) < 3` is FALSE.
   - Do not jump. `index = 4`.

Loop ends. Return `index + 1` = `5`. ✓
The 3rd smallest element is exactly 5!

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(log M)$ | $O(M)$ |
| **Average** | $O(log M)$ | $O(M)$ |
| **Worst** | $O(log M)$ | $O(M)$ |

*Where M is the maximum value in the collection.*
The binary lifting loop executes exactly log_2 M times. In each iteration, it performs $O(1)$ operations because it reads the sum directly from the specific BIT index without traversing upward! Time complexity is strictly $O(log M)$.
Space complexity is $O(M)$ to store the BIT array (which necessitates coordinate compression if M is astronomical).

## Variants & optimizations

- **Segment Tree Walking:** You can achieve the exact same $O(log M)$ order statistic query by walking down a Segment Tree, steering left or right based on whether the left child's sum is \ge K. However, the Fenwick tree version is significantly faster due to memory locality and lack of pointers.

## Real-world applications

- **Database Percentiles:** Calculating the exact 99th percentile response time from a high-frequency stream of server telemetry logs.

## Related algorithms in cOde(n)

- **[fenwick_06 - Count Inversions](fenwick_06_count-inversions-bit.md)** — The basic application of Fenwick as a Frequency map.
- **[heap_04 - Median in a Stream](../heap/heap_04_median-in-a-stream.md)** — A different approach using two Priority Queues. Two heaps are better if you *only* need the exact 50th percentile (median), but the Fenwick approach is required if you want arbitrary K-th percentiles dynamically.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
