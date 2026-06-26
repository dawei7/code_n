# Frequency of Elements in Sorted Array

| | |
|---|---|
| **ID** | `dc_18` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problem statement

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If `target` is not found in the array, return `[-1, -1]`.
You must write an algorithm with $O(\log N)$ runtime complexity.
*(Alternatively framed as: count the frequency of `target` in the sorted array by returning `end_index - start_index + 1`).*

**Input:** A sorted integer array `nums` and a `target` integer.
**Output:** An array `[start_index, end_index]`.

## When to use it

- Whenever you need to search an array where duplicate elements are allowed, and you need to pinpoint the boundaries of a specific element cluster.
- The fundamental extension to standard Binary Search.

## Approach

**1. The Flaw of Standard Binary Search:**
If the array is `[5, 7, 7, 8, 8, 8, 8, 8, 10]` and target is `8`.
Standard Binary Search might randomly land on index `5`. It returns `5` and terminates. But you don't know where the `8`s start or end!
You *could* linearly scan left and right from index 5 until the 8s stop, but if the entire array of 1 million elements is all `8`s, your linear scan degrades to $O(N)$ time limit exceeded!

**2. Divide and Conquer (Binary Search Modifiers):**
We can run Binary Search TWICE.
- Once to find the absolute Leftmost occurrence of `target`.
- Once to find the absolute Rightmost occurrence of `target`.

**3. Finding the Left Boundary:**
When we are searching for the target, and `nums[mid] == target`, what should we do?
Normally, we stop. But because we want the LEFTMOST occurrence, we pretend `mid` might not be the absolute furthest left one!
We store `ans = mid`, and aggressively chop off the right half of the array! We set `high = mid - 1` and keep searching to the left!

**4. Finding the Right Boundary:**
Identical logic. When `nums[mid] == target`, we store `ans = mid`, but we aggressively chop off the left half! We set `low = mid + 1` and keep searching to the right to see if there are any MORE occurrences of `target` further down!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_18: Frequency in Limited Range (sorted array).

Given a sorted array of positive integers and a
"""


def solve(arr, n, target):
    """Frequency of `target` in a sorted array via two binary
    searches (first and last occurrence)."""
    # First occurrence.
    lo, hi, first = 0, n - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            first = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if first == -1:
        return 0
    # Last occurrence.
    lo, hi, last = first, n - 1, first
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            last = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return last - first + 1
```

</details>

## Walk-through

`nums = [5, 7, 7, 8, 8, 10]`, `target = 8`.

**Run 1: Left Boundary (`is_finding_left = True`)**
1. `low=0`, `high=5`. `mid=2` (val `7`). `7 < 8`. `low = 3`.
2. `low=3`, `high=5`. `mid=4` (val `8`). MATCH!
   - `ans = 4`.
   - `high = mid - 1 = 3`. (Force search left!).
3. `low=3`, `high=3`. `mid=3` (val `8`). MATCH!
   - `ans = 3`. (Overwrites 4, we found an earlier one!).
   - `high = mid - 1 = 2`.
4. `low (3) <= high (2)` is FALSE. Loop ends. `left_bound = 3`.

**Run 2: Right Boundary (`is_finding_left = False`)**
1. `low=0`, `high=5`. `mid=2` (val `7`). `7 < 8`. `low = 3`.
2. `low=3`, `high=5`. `mid=4` (val `8`). MATCH!
   - `ans = 4`.
   - `low = mid + 1 = 5`. (Force search right!).
3. `low=5`, `high=5`. `mid=5` (val `10`). `10 > 8`.
   - `high = mid - 1 = 4`.
4. `low (5) <= high (4)` is FALSE. Loop ends. `right_bound = 4`.

Result `[3, 4]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(\log N)$ | $O(1)$ |

We simply run two completely independent $O(\log N)$ Binary Searches sequentially. Thus, $O(\log N)$ + $O(\log N)$ = $O(\log N)$ time complexity.
Space complexity is $O(1)$.

## Variants & optimizations

- **`bisect` module in Python:** Instead of writing this by hand, Python's built-in binary search module has `bisect_left` (returns the index of the first occurrence) and `bisect_right` (returns the index immediately *after* the last occurrence).
- **Count the frequency:** Just return `right_bound - left_bound + 1`.

## Real-world applications

- **Database Range Scans (B-Trees):** When executing a SQL query like `SELECT * FROM table WHERE age = 25`, the database uses a B-Tree index (a multi-way binary search tree) to find the leftmost node containing 25, and then sequentially reads disk pages until the key changes to 26. This algorithm models the exact mechanism of finding that leftmost starting block.

## Related algorithms in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The foundation.
- **[searching_03 - Search Insert Position](../searching/search_03_search-insert-position.md)** — A closely related variation where `bisect_left` is used to find where an element *should* be inserted.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
