# Jump Search (Block Search)

| | |
|---|---|
| **ID** | `search_06` |
| **Category** | searching |
| **Complexity (required)** | $O(\sqrt{N})$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Jump search](https://en.wikipedia.org/wiki/Jump_search) |

## Problem statement

Given a sorted array `arr` and a `target` value.
Find the index of the `target` in the array. If the `target` is not present, return `-1`.
You must solve this by jumping forward in fixed steps to find the correct block, and then performing a linear search within that block.

**Input:** A sorted array `arr` and a `target` value.
**Output:** An integer representing the index.

## When to use it

- When you have a sorted array but Binary Search is computationally inefficient because "Jumping Backwards" is significantly more expensive than jumping forwards. (e.g. searching data on a physical magnetic tape drive, or iterating through a Singly Linked List with "Skip" pointers).

## Approach

**1. The Block Skipping Strategy:**
Instead of checking every single element (Linear Search $O(N)$), we can skip chunks of data!
If we jump in steps of `m`:
Index 0, Index m, Index 2m, Index 3m...
At each jump, we check if `arr[km] >= target`.
Because the array is sorted, the exact moment `arr[km]` becomes larger than our target, we know we overshot it!
The target MUST be mathematically trapped in the previous block between index (k-1)m and index km.

**2. The Localized Linear Search:**
Once we have identified the correct block of size `m`, we simply jump backwards one single time to the start of the block, and perform a standard $O(m)$ Linear Search until we hit the target.

**3. Choosing the Optimal Block Size:**
What is the mathematically perfect jump size `m`?
In the worst-case scenario, we have to jump \frac{N}{m} times to reach the final block.
Then, we have to linear search through m-1 elements in that block.
Total operations = \frac{N}{m} + m - 1.
Using Calculus, we take the derivative with respect to m and set it to 0 to find the minimum:
-\frac{N}{m^2} + 1 = 0 -> m^2 = N -> m = \sqrt{N}.
Therefore, the optimal jump size is exactly the square root of the array length!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_06: Jump Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    import math
    step = max(1, int(math.sqrt(n)))
    prev = 0
    # Find the block where the target could be.
    while prev < n and data[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # Linear scan inside the block.
    for index in range(prev, min(step, n)):
        if data[index] == target:
            return index
    return -1
```

</details>

## Walk-through

`arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`, `target = 55`.
`N = 11`. `step = sqrt(11) = 3`. `prev = 0`.

1. **Jump 1:** Check index `3-1 = 2`. `arr[2] = 1`.
   - `1 < 55`. Jump! `prev = 3`, `step = 6`.
2. **Jump 2:** Check index `6-1 = 5`. `arr[5] = 5`.
   - `5 < 55`. Jump! `prev = 6`, `step = 9`.
3. **Jump 3:** Check index `9-1 = 8`. `arr[8] = 21`.
   - `21 < 55`. Jump! `prev = 9`, `step = 12`.
4. **Jump 4:** `min(step, n) - 1 = min(12, 11) - 1 = 10`. `arr[10] = 55`.
   - `55 < 55` is FALSE! Loop terminates.

Block identified! `prev = 9`, end bound = `min(12, 11) = 11`.
1. **Linear Search:** `i = 9`. `arr[9] = 34 == 55`? False.
2. `i = 10`. `arr[10] = 55 == 55`? TRUE!
Return `10`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\sqrt{N})$ | $O(1)$ |
| **Worst** | $O(\sqrt{N})$ | $O(1)$ |

The number of jumps is bounded by \frac{N}{\sqrt{N}} = \sqrt{N}. The number of linear search steps is bounded by the block size \sqrt{N}.
Therefore, the total time complexity is $O(\sqrt{N} + \sqrt{N})$ = $O(\sqrt{N})$.
This is vastly superior to Linear Search $O(N)$, but vastly inferior to Binary Search $O(\log N)$.
Space complexity is $O(1)$.

## Variants & optimizations

- **Multi-Level Jump Search:** Why just do a linear search in the final block? If the block size \sqrt{N} is still very large, you can do a Jump Search INSIDE the block! (Using a new block size of N^{1/4}). Repeating this recursively creates a system that approaches $O(\log N)$ time, conceptually identical to a B-Tree structure or a Skip List!

## Real-world applications

- **Skip Lists:** The fundamental logic of creating "Express Lanes" over a Linked List to achieve $O(\log N)$ search times without relying on contiguous memory arrays.
- **Magnetic Tape Drives / Sequential Storage:** Seeking backwards on physical cassette tapes takes significantly longer than fast-forwarding. Binary Search jumps backwards 50% of the time! Jump Search only jumps backward EXACTLY once (when the block is found), making it vastly superior for physical sequential media.

## Related algorithms in cOde(n)

- **[search_01 - Linear Search](search_01_linear-search.md)** — The core $O(N)$ algorithm used inside the final block.
- **[search_02 - Binary Search](search_02_binary-search.md)** — The mathematically optimal search algorithm for memory-backed arrays.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
