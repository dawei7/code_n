# Counting Sort

| | |
|---|---|
| **ID** | `sort_07` |
| **Category** | sorting |
| **Complexity (required)** | $O(n + k)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Counting sort](https://en.wikipedia.org/wiki/Counting_sort) |

## Problem statement

Given an array of integers `arr`, where all elements are non-negative and are known to be bounded by a relatively small maximum value `k`, sort the array in ascending order using the Counting Sort algorithm.

**Input:** An unsorted array of non-negative integers `arr`, and the maximum value `k` in the array.
**Output:** The array sorted in strictly ascending order.

**Example:**
| Input `arr` | `k` | Output |
|---|---|---|
| `[4, 2, 2, 8, 3, 3, 1]` | 8 | `[1, 2, 2, 3, 3, 4, 8]` |

## When to use it

- When the input data are integers spanning a **small, known range** (e.g., sorting ages of people, which are strictly bounded between 0 and 150).
- When you need a **linear time $O(n)$** sort. Because Counting Sort doesn't compare elements to each other, it shatters the `O(n log n)` lower-bound mathematically proven for comparison-based sorts!
- As a stable subroutine for **Radix Sort**.

## Approach

Counting Sort completely abandons the idea of comparing `a` vs `b`.
Instead, it counts the absolute frequency of every integer in the array.

1. **Count Frequencies:** Create a `count` array of size `k + 1` (initialized to 0). Iterate through the input `arr`. If you see the number `4`, increment `count[4]`.
2. **Compute Prefix Sums:** Modify the `count` array so that each index now stores the sum of all preceding counts. `count[i] += count[i-1]`. This brilliant step transforms the array from "frequencies" to "actual starting positions" in the final sorted array.
3. **Build Output:** Iterate through the original `arr` *backwards* (to maintain stability). Find the element's position in the `count` array, place it in an `output` array at that exact index `- 1`, and decrement the count.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for sort_07: Counting Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val + 1
    counts = [0] * span
    for value in data:
        counts[value - min_val] += 1
    # Rewrite data in place by walking the count array.
    index = 0
    for offset, count in enumerate(counts):
        for _ in range(count):
            data[index] = offset + min_val
            index += 1
    return data
```

</details>

## Walk-through

Let `arr = [2, 1, 1, 0, 2]`. `k = 2`.

**1. Frequencies:**
`count = [0, 0, 0]`
- Read 2 -> `count = [0, 0, 1]`
- Read 1 -> `count = [0, 1, 1]`
- Read 1 -> `count = [0, 2, 1]`
- Read 0 -> `count = [1, 2, 1]`
- Read 2 -> `count = [1, 2, 2]`

**2. Prefix Sums:**
`count[0]` stays `1`.
`count[1] = count[1] + count[0]` = `2 + 1 = 3`.
`count[2] = count[2] + count[1]` = `2 + 3 = 5`.
`count` array is now `[1, 3, 5]`. This means the last `0` goes at index 0, the last `1` goes at index 2, the last `2` goes at index 4.

**3. Build Output (Backwards):**
- Read `2`. `count[2]` is 5. Place at index 4. `count[2]` becomes 4. `output = [_, _, _, _, 2]`
- Read `0`. `count[0]` is 1. Place at index 0. `count[0]` becomes 0. `output = [0, _, _, _, 2]`
- Read `1`. `count[1]` is 3. Place at index 2. `count[1]` becomes 2. `output = [0, _, 1, _, 2]`
- Read `1`. `count[1]` is 2. Place at index 1. `count[1]` becomes 1. `output = [0, 1, 1, _, 2]`
- Read `2`. `count[2]` is 4. Place at index 3. `count[2]` becomes 3. `output = [0, 1, 1, 2, 2]`

Sorted! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n + k)$ | $O(n + k)$ |
| **Average** | $O(n + k)$ | $O(n + k)$ |
| **Worst** | $O(n + k)$ | $O(n + k)$ |

The algorithm iterates through the input array twice (size `n`), and the count array twice (size `k`). Therefore, the time complexity is strictly `O(n + k)`. If `k` is small (e.g., `k <= n`), this is a true linear `O(n)` sort!
However, space complexity is also `O(n + k)`. If you try to sort an array `[1, 1000000000]`, the algorithm will blindly allocate a 1-Billion-element array just to sort 2 numbers, resulting in a catastrophic Out Of Memory crash.

## Variants & optimizations

- **Negative Numbers:** Counting Sort inherently assumes indices start at 0. If the array contains negative numbers, find the absolute minimum value and shift the entire array uniformly by adding `abs(min)`. After sorting, subtract it back.

## Real-world applications

- **Radix Sort Foundation:** Used as the stable integer sorting mechanism behind Radix Sort, allowing Radix Sort to sort numbers digit-by-digit sequentially.
- **Suffix Arrays:** Advanced string processing algorithms use Counting Sort to heavily optimize the prefix sorting phases, accelerating substring searches.

## Related algorithms in cOde(n)

- **[sort_08 - Radix Sort](sort_08_radix-sort.md)** — Solves Counting Sort's massive memory problem by sorting extremely large numbers digit-by-digit rather than all at once.
- **[sort_09 - Bucket Sort](sort_09_bucket-sort.md)** — A closely related non-comparison sort that handles floating-point numbers instead of integers.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
