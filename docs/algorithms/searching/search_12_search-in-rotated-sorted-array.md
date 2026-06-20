# Search in Rotated Sorted Array

| | |
|---|---|
| **ID** | `search_12` |
| **Category** | searching |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 10/10 |
| **LeetCode Equivalent** | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |

## Problem statement

There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly **rotated** at an unknown pivot index `k`.
For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.
Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
You must write an algorithm with $O(\log N)$ runtime complexity.

**Input:** A rotated sorted array `nums` and a `target` value.
**Output:** An integer representing the index.

## When to use it

- One of the most infamous and common Binary Search variations in FAANG interviews.
- Tests your ability to establish logical invariants (guarantees) on half of a dataset when the whole dataset is slightly corrupted.

## Approach

**1. The Rotated Array Guarantee:**
In a standard Binary Search, we pick a `mid` point. Because the array is perfectly sorted, we automatically know which half the target must be in.
In a *Rotated* array, if we pick `mid`, the array is NO LONGER perfectly sorted!
BUT, there is a massive mathematical guarantee: **If you split a rotated sorted array in half, exactly ONE of the two halves will ALWAYS be perfectly sorted!**

Look at `[4, 5, 6, 7, 0, 1, 2]`. Mid is `7`.
- Left half `[4, 5, 6, 7]` is perfectly sorted!
- Right half `[7, 0, 1, 2]` is corrupted.

Look at `[6, 7, 0, 1, 2, 4, 5]`. Mid is `1`.
- Left half `[6, 7, 0, 1]` is corrupted.
- Right half `[1, 2, 4, 5]` is perfectly sorted!

**2. The Invariant Elimination Logic:**
We must figure out *which* half is the sorted one.
We just compare the start of the array to the middle! If `nums[left] <= nums[mid]`, the left half is the perfectly sorted one. Otherwise, the right half is the sorted one!

Once we find the perfectly sorted half, we have a pristine environment! We check if the `target` falls mathematically within the bounds of that sorted half.
- If it does, we discard the corrupted half entirely and standard Binary Search the sorted half!
- If it DOES NOT, the target MUST be hiding somewhere inside the corrupted half! We discard the sorted half and repeat the process on the corrupted half!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_12: Search in Rotated Sorted Array.

A sorted array that has been rotated at some unknown pivot.
Find the index of ``target`` (or -1) in O(log n) time.
Find the pivot (smallest element) first, then binary-search
the half that could contain the target.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    low, high = 0, n - 1
    # Find the rotation pivot: the smallest element.
    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        else:
            high = mid
    pivot = low
    # Decide which half to search.
    if pivot == 0:
        low, high = 0, n - 1
    elif data[0] <= target <= data[pivot - 1]:
        # Target is in the upper half (data[0..pivot-1]).
        low, high = 0, pivot - 1
    else:
        # Target is in the lower half (data[pivot..n-1]).
        low, high = pivot, n - 1
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

`nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`. Length 7.

1. `L=0, R=6, M=3`. `nums[3] = 7`.
   - `7 == 0`? False.
   - Is Left sorted? `nums[L] (4) <= nums[M] (7)` -> TRUE! Left is sorted `[4, 5, 6, 7]`.
   - Is target inside left? `4 <= 0 < 7` -> FALSE! Target is not in the sorted half.
   - Discard left half. `L = M+1 = 4`.
2. `L=4, R=6, M=5`. `nums[5] = 1`.
   - `1 == 0`? False.
   - Is Left sorted? `nums[L] (0) <= nums[M] (1)` -> TRUE! Left is sorted `[0, 1]`.
   - Is target inside left? `0 <= 0 < 1` -> TRUE!
   - Target is in the sorted half! Discard right half. `R = M-1 = 4`.
3. `L=4, R=4, M=4`. `nums[4] = 0`.
   - `0 == 0`! Match found!
   - Return `mid = 4`.

Result: `4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(\log N)$ | $O(1)$ |

Even though the array is rotated and partially corrupted, our algorithm guarantees that we successfully discard exactly 50% of the remaining search space on every single iteration!
Therefore, the time complexity remains identical to pristine Binary Search: $O(\log N)$.
Space complexity is $O(1)$ because we only use three integer pointer variables.

## Variants & optimizations

- **Search in Rotated Array II (With Duplicates):** If the array can contain duplicates (e.g. `[1, 0, 1, 1, 1]`), our check `nums[left] <= nums[mid]` BREAKS! (1 is \le 1, so it thinks the left half `[1, 0, 1]` is sorted, which is false!). To fix this, you must add a check: if `nums[left] == nums[mid]`, you can't be sure which half is sorted, so you just do `left += 1` to manually step past the duplicate. This degrades the worst-case time complexity to $O(N)$.
- **Find Minimum in Rotated Sorted Array:** A related problem where the goal is specifically to find the pivot point (the smallest element) rather than an arbitrary target.

## Real-world applications

- **Circular Buffers / Ring Buffers:** Data streams (like audio/video rendering streams) are often stored in fixed-size arrays where the "head" loops back to index 0 when it hits the end, effectively creating a perpetually Rotated Sorted Array of timestamps.

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The foundational algorithm that this heavily modifies.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
