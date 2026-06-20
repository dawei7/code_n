# Exponential Search (Galloping Search)

| | |
|---|---|
| **ID** | `search_07` |
| **Category** | searching |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Exponential search](https://en.wikipedia.org/wiki/Exponential_search) |

## Problem statement

Given a sorted array `arr` and a `target` value.
Find the index of the `target` in the array. If the `target` is not present, return `-1`.
Optimize the search for scenarios where the array is BOUNDLESS (infinite size) or when the target is expected to be very close to the beginning of the array.

**Input:** A sorted array `arr` and a `target` value.
**Output:** An integer representing the index.

## When to use it

- **Infinite Arrays:** When you literally do not know the size of the array (e.g., reading an active, endless data stream), you mathematically CANNOT use Binary Search because you don't know where to place the `right` pointer!
- **Front-Heavy Data:** When statistical analysis shows the target is usually located in the first 5% of a massive array, Binary Search wastes operations checking the middle/end.

## Approach

**1. The Galloping Phase:**
We start at index `1`. We check if the element there is \ge our target.
If it's smaller, we double our index! `1 -> 2 -> 4 -> 8 -> 16...`
We keep doubling our index exponentially until `arr[index] >= target` (or we go out of bounds).
Because the array is sorted, the exact moment we overshoot the target, we know the target MUST exist between our previous jump `index / 2` and our current `index`!

**2. The Binary Search Phase:**
Now that we have successfully identified a closed bound `[index / 2, min(index, N-1)]`, we simply pass those bounds into a standard Binary Search!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_07: Exponential Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    if n == 0 or data[0] > target:
        return -1
    bound = 1
    while bound < n and data[bound] <= target:
        bound *= 2
    # Binary search in [bound/2, min(bound, n-1)].
    low, high = bound // 2, min(bound, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

</details>

## Walk-through

`arr = [10, 20, 40, 50, 70, 90, 100, 120, 150]`, `target = 90`. Length 9.

1. `arr[0] = 10 == 90`? False.
2. **Gallop:**
   - `i = 1`: `arr[1] = 20 <= 90`. `i = 1 * 2 = 2`.
   - `i = 2`: `arr[2] = 40 <= 90`. `i = 2 * 2 = 4`.
   - `i = 4`: `arr[4] = 70 <= 90`. `i = 4 * 2 = 8`.
   - `i = 8`: `arr[8] = 150 <= 90` is FALSE! Gallop terminates.
3. **Binary Search Range:**
   - `left = 8 // 2 = 4`.
   - `right = min(8, 8) = 8`.
   - Call `binary_search(arr, left=4, right=8, target=90)`.
4. **Binary Search:**
   - `mid = (4 + 8) // 2 = 6`. `arr[6] = 100 > 90`. `right = 5`.
   - `mid = (4 + 5) // 2 = 4`. `arr[4] = 70 < 90`. `left = 5`.
   - `mid = (5 + 5) // 2 = 5`. `arr[5] = 90 == 90`! Match found!

Result: `5`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log I)$ | $O(1)$ |
| **Worst** | $O(\log I)$ | $O(1)$ |

Let I be the index where the target is actually located.
The galloping phase doubles i until it passes I. This takes $O(log I)$ steps.
The binary search phase then searches a range of size \frac{I}{2}. Binary searching that range takes $O(log(I/2)$) = $O(log I - 1)$ = $O(log I)$ steps.
Therefore, the total time complexity is strictly $O(log I)$.
If the target is at index 10, Exponential Search finds it in ~= log_2(10) = 3 operations, even if the array has 1 billion elements! Standard Binary search would take ~= log_2(10^9) = 30 operations.
Space complexity is $O(1)$.

## Variants & optimizations

- **Unbounded Binary Search:** When dealing with functions rather than arrays (e.g. "Find the first positive integer X where f(X) > 1000"), you mathematically cannot use standard Binary Search because there is no upper bound. You MUST use Exponential Search to find the upper bound first!

## Real-world applications

- **Python's Timsort:** The default sorting algorithm used in Python (`list.sort()`) and Java (`Arrays.sort()`). Timsort internally uses a highly optimized variation of Exponential Search (specifically called Galloping) to rapidly find insertion points when merging two arrays that are highly unbalanced in size!

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The secondary phase algorithm used after the bounding box is found.
- **[search_06 - Jump Search](search_06_jump-search.md)** — Uses a similar logic of jumping over elements, but uses fixed-size arithmetic jumps (\sqrt{N}) instead of exponential geometric jumps (x 2).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
