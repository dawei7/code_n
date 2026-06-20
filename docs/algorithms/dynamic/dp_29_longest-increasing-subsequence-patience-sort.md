# Longest Increasing Subsequence ($O(n log n)$ Patience Sort)

| | |
|---|---|
| **ID** | `dp_29` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(n log n)$ |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Longest Increasing Subsequence (Optimal)](https://leetcode.com/problems/longest-increasing-subsequence/) |

## Problem statement

*(This is an advanced binary-search optimization of `dp_07_longest-increasing-subsequence`).*

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

The standard DP algorithm (`dp_07`) solves this in $O(n^2)$ time by comparing every pair of elements. Can we optimize this to $O(n log n)$?

## When to use it

- To solve LIS when the array size N is up to 10^5, where an $O(n^2)$ algorithm would result in a Time Limit Exceeded (TLE) error.

## Approach

We can construct an active "tails" array.
`tails[i]` stores the **smallest** tail element of all increasing subsequences of length `i+1`.

Why keep the *smallest* tail? 
Because if we want to extend a subsequence later, having a smaller tail gives us the best possible chance of finding a number larger than it!

As we iterate through the given `nums` array, we look at each `num`:
1. If `num` is larger than every element currently in `tails`, it naturally extends our longest increasing subsequence by 1. We append it to the end of `tails`.
2. If `num` is *not* the largest, it cannot extend the longest sequence. However, it can *replace* an existing tail to create a more favorable (smaller) tail for a sequence of that specific length! We find the first element in `tails` that is \ge `num`, and overwrite it with `num`.

**The Magic:**
Because `tails` stores increasing subsequences of strictly increasing lengths, the `tails` array is mathematically guaranteed to be **strictly sorted in ascending order** at all times!
Because it is sorted, we can find the element to overwrite using **Binary Search** in $O(log n)$ time!

*(Note: The `tails` array itself is NOT the actual LIS sequence! It just stores the optimal tails. However, the `length(tails)` perfectly equals the length of the LIS).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_29: LIS (Patience Sort).

Maintain a sorted tails array; binary-search to place each
value. O(n log n).
"""


def solve(arr, n):
    if n == 0:
        return 0
    import bisect
    tails = []
    for v in arr:
        idx = bisect.bisect_left(tails, v)
        if idx == len(tails):
            tails.append(v)
        else:
            tails[idx] = v
    return len(tails)
```

</details>

## Walk-through

`nums = [4, 5, 6, 3]`. `tails = []`.

**num = 4:**
- Binary search in `[]` yields `left = 0`.
- Append `4`. `tails = [4]`.

**num = 5:**
- BS in `[4]` yields `left = 1` (since 5 > 4).
- Append `5`. `tails = [4, 5]`.

**num = 6:**
- BS in `[4, 5]` yields `left = 2` (since 6 > 5).
- Append `6`. `tails = [4, 5, 6]`.

**num = 3:**
- BS in `[4, 5, 6]`. `3` is smaller than `4`. `left = 0`.
- Overwrite index 0. `tails = [3, 5, 6]`.
*(Notice that `[3, 5, 6]` is not a valid subsequence in the original array! But it doesn't matter. The length is still 3. And if we later encountered `[4, 5]`, having `3` at index 0 makes it easier to build new sequences).*

Output: `length(tails) = 3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(n log n)$ | $O(n)$ |
| **Average** | $O(n log n)$ | $O(n)$ |
| **Worst** | $O(n log n)$ | $O(n)$ |

We iterate through n elements. For each element, we perform a binary search on the `tails` array, which takes $O(log n)$ time. Total time complexity is strictly $O(n log n)$.
Space complexity is $O(n)$ for the `tails` array.

## Variants & optimizations

- **Patience Sorting:** This algorithm is mathematically equivalent to the card game Patience. You place cards into piles where a card can only be placed on a pile if its value is smaller. The number of piles formed is exactly the length of the LIS!

## Real-world applications

- **Version Control Systems (Git):** Used in the `diff` algorithm to find the Longest Common Subsequence of lines between two files by transforming the LCS problem into an LIS problem!

## Related algorithms in cOde(n)

- **[dp_07 - Longest Increasing Subsequence](dp_07_longest-increasing-subsequence.md)** — The classic $O(n^2)$ DP approach.
- **[search_03 - Binary Search](../searching/search_03_binary-search.md)** — The $O(log n)$ engine used here.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
