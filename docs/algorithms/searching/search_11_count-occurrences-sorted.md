# Count Occurrences in Sorted Array

| | |
|---|---|
| **ID** | `search_11` |
| **Category** | searching |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problem statement

Given a sorted array `arr` and a `target` value. The array may contain duplicate elements.
Find the total number of times the `target` appears in the array.
You must solve this in $O(\log N)$ time complexity.

**Input:** A sorted integer array `arr`, and an integer `target`.
**Output:** An integer representing the total count of the target.

## When to use it

- To precisely map the Left Bound and Right Bound of a sequence of duplicates.
- Whenever standard Binary Search fails because you need the *very first* occurrence of an element rather than a random middle one.

## Approach

**1. The Flaw of Standard Binary Search:**
If `arr = [2, 2, 2, 2, 2]` and `target = 2`. Standard binary search finds the `2` at index 2, and immediately returns.
If we want to count the occurrences, we could write a `while` loop to linearly scan left and right from index 2 to find all the other `2`s.
BUT, what if the array is ONE MILLION `2`s? The linear scan will take 1,000,000 operations! This turns our $O(\log N)$ algorithm into $O(N)$, completely violating the time requirement!

**2. Finding the First Occurrence (Lower Bound):**
To stay strictly in $O(\log N)$ time, we must use Binary Search to find the EXACT starting index of the target.
We modify standard Binary Search: When we find `arr[mid] == target`, **WE DO NOT RETURN!**
Instead, we think: "I found a 2. But there might be more 2s to my left!"
So, we record this index as a potential answer, and then we deliberately throw away the right half of the array! `right = mid - 1`.
We keep doing this. The last index we recorded before the loop terminates is guaranteed to be the FIRST occurrence!

**3. Finding the Last Occurrence (Upper Bound):**
We write a second, almost identical Binary Search.
When we find `arr[mid] == target`, we think: "I found a 2. But there might be more 2s to my right!"
We record the index, and throw away the left half! `left = mid + 1`.
The last index recorded is guaranteed to be the LAST occurrence!

**4. The Final Count:**
Once we have the `first_index` and `last_index`, the total count is simply `last_index - first_index + 1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_11: Count Occurrences (Sorted).

Sorted array; count how many times ``target`` appears. Two
binary searches: one for the first occurrence (lower_bound),
one for the last (upper_bound). Difference = count.
O(log n) time.
"""


def solve(data, target, n):
    if n == 0:
        return 0

    def lower_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] <= t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(0, n, target)
    if first == n or data[first] != target:
        return 0
    last = upper_bound(first, n, target)
    return last - first
```

</details>

## Walk-through

`arr = [1, 2, 2, 2, 2, 3, 4]`, `target = 2`. Length 7.

**Finding First Occurrence:**
1. `L=0, R=6, M=3`. `arr[3] = 2 == target`.
   - `first_idx = 3`. `R = M-1 = 2`.
2. `L=0, R=2, M=1`. `arr[1] = 2 == target`.
   - `first_idx = 1`. `R = M-1 = 0`.
3. `L=0, R=0, M=0`. `arr[0] = 1 < target`.
   - `L = M+1 = 1`.
4. `L=1, R=0`. `L <= R` is False. Loop ends. `first_idx = 1`.

**Finding Last Occurrence:**
1. `L=0, R=6, M=3`. `arr[3] = 2 == target`.
   - `last_idx = 3`. `L = M+1 = 4`.
2. `L=4, R=6, M=5`. `arr[5] = 3 > target`.
   - `R = M-1 = 4`.
3. `L=4, R=4, M=4`. `arr[4] = 2 == target`.
   - `last_idx = 4`. `L = M+1 = 5`.
4. `L=5, R=4`. `L <= R` is False. Loop ends. `last_idx = 4`.

Count = `4 - 1 + 1 = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(\log N)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(\log N)$ | $O(1)$ |

We run exactly two separate Binary Searches, sequentially.
Each Binary Search takes $O(\log N)$ time.
Total time is $O(log N + log N)$ = $O(2 log N)$, which strictly bounds to $O(\log N)$.
Space complexity is $O(1)$ because we only use integer pointer variables.

## Variants & optimizations

- **C++ `std::lower_bound`:** In modern C++, this exact algorithm is natively built into the standard library! `std::lower_bound(arr, target)` returns a pointer to the *first* occurrence. `std::upper_bound(arr, target)` returns a pointer to exactly one element *past* the last occurrence. Finding the count is as simple as `upper_bound - lower_bound`.
- **Python `bisect`:** Python's standard library equivalent. `bisect.bisect_left()` finds the first occurrence index, and `bisect.bisect_right()` finds the element after the last occurrence.

## Real-world applications

- **Log File Analysis:** If millions of server log entries are sorted by timestamp (e.g. `12:00:01`, `12:00:01`, `12:00:01`, `12:00:05`), this algorithm rapidly counts exactly how many requests occurred at a specific second without scanning the whole file.

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The foundational algorithm that this builds upon.
- **[arrays_03 - Majority Element](../arrays/arrays_03_majority-element.md)** — If the array is sorted, this algorithm can be used to instantly check if the count of an element is > N/2, proving it is a Majority Element in $O(\log N)$ time instead of $O(N)$ Boyer-Moore time!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
