# Pancake Sort

| | |
|---|---|
| **ID** | `sort_12` |
| **Category** | sorting |
| **Complexity (required)** | $O(N^2)$ Time, $O(1)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 2/10 |
| **LeetCode Equivalent** | [Pancake Sorting](https://leetcode.com/problems/pancake-sorting/) |

## Problem statement

Given an array of integers `arr`, sort the array in ascending order.
You are ONLY allowed to modify the array using a single specific operation: `flip(k)`.
A `flip(k)` operation reverses the sub-array `arr[0...k]`.
Return the sequence of `k` values that sort the array.

**Input:** An unsorted array of integers `arr`.
**Output:** An array of integers representing the flip sizes.

## When to use it

- Essentially a brain-teaser puzzle rather than a practical algorithm.
- Historically famous because Bill Gates' ONLY published academic paper (written during his time at Harvard) was an optimization on the mathematical bounds of Pancake Sorting!

## Approach

**1. The Spatula Analogy:**
Imagine a messy stack of pancakes of all different sizes. You want the largest pancake at the bottom, and the smallest at the top.
You only have one tool: a spatula. You can slide the spatula under the k-th pancake from the top, and flip the entire stack resting on the spatula completely upside down!

**2. The "Move to End" Strategy:**
How do we get the absolute largest pancake to the very bottom of the stack?
1. First, we find the largest pancake. Suppose it is at index `i`.
2. We slide the spatula under it and flip the stack: `flip(i)`.
3. Now, the largest pancake is at index `0` (the very top of the stack)!
4. We slide the spatula under the ENTIRE stack: `flip(N-1)`.
5. The entire stack is reversed, placing the largest pancake perfectly at the very bottom (index `N-1`)!

**3. Shrinking the Stack:**
Now that the largest pancake is perfectly in place at the bottom, we pretend the stack is now 1 pancake shorter!
We find the *second* largest pancake in the remaining stack (indices `0` to `N-2`).
We `flip` it to the top (`0`), and then `flip` it to the bottom of the active stack (`N-2`).
We repeat this process until the active stack size shrinks to 1.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_12: Pancake Sort.

The only allowed operation is ``reverse prefix [0..k]`` for
some k. For each pass, find the maximum in the current
unsorted prefix, flip it to the front, then flip the prefix
to drop the max to the end. O(n^2) flips.
"""


def solve(data, n):
    def flip(end):
        start = 0
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    size = n
    while size > 1:
        # Find index of the maximum element in data[0..size-1].
        max_idx = 0
        for i in range(1, size):
            if data[i] > data[max_idx]:
                max_idx = i
        if max_idx != size - 1:
            if max_idx != 0:
                flip(max_idx)
            flip(size - 1)
        size -= 1
    return data
```

</details>

## Walk-through

`arr = [3, 2, 4, 1]`. `N = 4`. `result = []`.

**Iteration 1 (`curr_size = 4`):**
1. Max element in `[3, 2, 4, 1]` is `4` at `max_idx = 2`.
2. `max_idx != 0`. `flip(2)`!
   - Reverse `arr[0...2]`: `[4, 2, 3, 1]`.
   - `result.append(3)`.
3. `flip(3)` (the entire active stack)!
   - Reverse `arr[0...3]`: `[1, 3, 2, 4]`.
   - `result.append(4)`.
Largest element `4` is now perfectly in place at the end!

**Iteration 2 (`curr_size = 3`):**
1. Max element in `[1, 3, 2]` is `3` at `max_idx = 1`.
2. `max_idx != 0`. `flip(1)`!
   - Reverse `arr[0...1]`: `[3, 1, 2, 4]`.
   - `result.append(2)`.
3. `flip(2)` (the active stack)!
   - Reverse `arr[0...2]`: `[2, 1, 3, 4]`.
   - `result.append(3)`.
`3` is now perfectly in place!

**Iteration 3 (`curr_size = 2`):**
1. Max element in `[2, 1]` is `2` at `max_idx = 0`.
2. `max_idx == 0`! No need to flip it to the top!
3. `flip(1)` (the active stack)!
   - Reverse `arr[0...1]`: `[1, 2, 3, 4]`.
   - `result.append(2)`.
`2` is now perfectly in place!

Array is completely sorted `[1, 2, 3, 4]`. ✓
Sequence of `k` flips: `[3, 4, 2, 3, 2]`.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N^2)$ | $O(1)$ |
| **Worst** | $O(N^2)$ | $O(1)$ |

Finding the maximum element takes an $O(N)$ linear scan.
Flipping the array takes $O(N)$ operations.
Because we must repeat this process N times (once for every pancake size), the total operations are bounded by $O(N x (N + N)$) = $O(N^2)$.
The maximum number of `flip` operations required to sort ANY stack of size N is mathematically proven to be \le \frac{18}{11}N.
Space complexity is $O(1)$ to sort the array, though the LeetCode variation requires an $O(N)$ array to store the string of answers.

## Variants & optimizations

- **Burnt Pancake Sort:** A notoriously difficult math variation where every pancake is burnt on one side. You must sort the stack by size AND ensure that every pancake has the burnt side facing completely downwards!

## Real-world applications

- **Genetics:** The mathematical operations of Pancake Sorting perfectly model the biological phenomenon of "Chromosome Inversions", where segments of DNA physically detach, reverse themselves, and reinsert into the genome!

## Related algorithms in cOde(n)

- **[sort_02 - Selection Sort](sort_02_selection-sort.md)** — The closest standard sorting algorithm, which similarly scans for the maximum element and moves it directly to the end of the array, shrinking the active boundary.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
