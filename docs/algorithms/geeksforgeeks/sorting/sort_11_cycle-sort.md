# Cycle Sort

| | |
|---|---|
| **ID** | `sort_11` |
| **Category** | sorting |
| **Complexity (required)** | $O(N^2)$ Time, $O(1)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Missing Number](https://leetcode.com/problems/missing-number/) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order.
You must sort the array using the absolute theoretical mathematical minimum number of memory writes (swaps) possible.
(e.g., if an element is already in the correct position, it should NEVER be written to or swapped. If it is in the wrong position, it should be moved to its correct position in exactly one write).

**Input:** An unsorted array of integers `arr`.
**Output:** A sorted array.

## When to use it

- **EEPROM / Flash Memory:** When writing data physically damages or degrades the storage medium. Cycle Sort guarantees the absolute minimum number of writes to prolong the life of the hardware.
- **The 1 to N Array Pattern:** An unbelievably common interview pattern where the array values perfectly match the array indices (e.g. "Given an array of length N containing numbers 1 to N, find the duplicate/missing number"). Cycle sort solves this in $O(N)$ time!

## Approach

**1. The Mathematical Graph Cycle:**
Imagine every element in the array points an arrow to the index where it *should* theoretically be located.
Because every element has a single unique destination, and every index can only hold one element, the arrows perfectly form closed loops (Cycles) across the entire array!
If an element is already in the correct position, it points to itself (a Cycle of length 1).

**2. The Standard $O(N^2)$ Cycle Sort Algorithm:**
We start at index `0`. We pick up the element, leaving a "hole".
We scan the entire array to count exactly how many elements are smaller than it. If there are `K` smaller elements, its correct position is index `K`.
We go to index `K`, pull out the element that's currently there, and drop our element into the hole!
Now we have a new element in our hand. We repeat the process! We count how many elements are smaller than it, find its correct index, pull out the element there, and drop ours in.
We continue tracing this cycle of displacements until we pull out an element that belongs in index `0`! We drop it in index `0`, completing the cycle perfectly.
We move to index `1` and repeat.

**3. The 1 to N Magic Optimization ($O(N)$):**
If the problem guarantees that the array numbers are `[1, N]`, we DON'T HAVE TO SCAN to count smaller elements!
If we are holding the number `5`, it mathematically MUST belong at index `4`!
The $O(N)$ scan turns into an $O(1)$ direct array access!
We just pick up `nums[i]`. Is it at index `nums[i] - 1`? If no, swap it to index `nums[i] - 1`! Keep swapping whatever number lands in `nums[i]` until the correct number finally lands there. Then move to `i+1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_11: Cycle Sort.

In-place, write-optimal sort. For each position, count elements
smaller than it to find its final index, then place the value
there. The displaced value starts a new cycle. O(n^2) time,
O(1) extra space, and at most n-1 writes.
"""


def solve(data, n):
    for cycle_start in range(n - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if data[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        # Skip past duplicates of `item` already at `pos`.
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if data[i] < item:
                    pos += 1
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
    return data
```

</details>

## Walk-through (1-to-N Optimized)

`arr = [3, 4, -1, 1]`.

1. `i = 0`: `arr[0]` is `3`. It belongs at index `2`.
   - Swap `arr[0]` and `arr[2]`.
   - `arr` becomes `[-1, 4, 3, 1]`.
2. `i = 0` (Wait, we don't increment `i`! We must process the new element!):
   - `arr[0]` is `-1`. Out of bounds!
   - `i += 1`.
3. `i = 1`: `arr[1]` is `4`. It belongs at index `3`.
   - Swap `arr[1]` and `arr[3]`.
   - `arr` becomes `[-1, 1, 3, 4]`.
4. `i = 1` (Process new element):
   - `arr[1]` is `1`. It belongs at index `0`.
   - Swap `arr[1]` and `arr[0]`.
   - `arr` becomes `[1, -1, 3, 4]`.
5. `i = 1` (Process new element):
   - `arr[1]` is `-1`. Out of bounds!
   - `i += 1`.
6. `i = 2`: `arr[2]` is `3`. Correct position! `i += 1`.
7. `i = 3`: `arr[3]` is `4`. Correct position! `i += 1`.
Loop terminates. `arr = [1, -1, 3, 4]`. ✓
*(This is the exact logic used to find the First Missing Positive integer in $O(N)$ time! The missing integer is just the first index where `arr[i] != i + 1`. In this case, index 1 has `-1` instead of `2`. The missing positive is 2!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ or $O(N)$ | $O(1)$ |
| **Average** | $O(N^2)$ or $O(N)$ | $O(1)$ |
| **Worst** | $O(N^2)$ or $O(N)$ | $O(1)$ |

For standard Cycle Sort, finding the correct position for an element requires a linear scan of the rest of the array. Over N elements, this guarantees $O(N^2)$ time.
For 1-to-N Cycle Sort, the target index is calculated via $O(1)$ arithmetic. Because every single swap physically places exactly one element in its forever-correct home, there can be at most N swaps! Even though there is a `while` loop that doesn't increment `i`, the total number of operations across the entire execution is strictly bounded to $O(N)$.
Space complexity is $O(1)$.

## Variants & optimizations

- **Find the Duplicate Number:** If the array contains N+1 numbers in the range [1, N], one number must be a duplicate. If you run 1-to-N Cycle sort, the duplicate will be the element that gets trapped in the very last index!

## Real-world applications

- **NASA / Satellite Hardware:** Flash memory modules on deep space probes have highly limited write cycles. To sort local sensor data, Cycle Sort ensures absolutely minimal degradation of the storage sectors.

## Related algorithms in cOde(n)

- **[arrays_06 - Find Missing Positive](../arrays/arrays_06_first-missing-positive.md)** — The LeetCode Hard problem that is completely trivialized by using the 1-to-N Cycle Sort variant.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
