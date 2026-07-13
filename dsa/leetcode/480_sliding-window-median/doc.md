# Sliding Window Median

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 480 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/sliding-window-median/) |

## Problem Description
### Goal
Given an integer array and a valid window length `k`, examine each contiguous block of exactly `k` values as the window moves one position right from the start to the end. Duplicate values remain separate window occurrences.

Return one floating-point median per window in left-to-right order. For odd `k`, the median is the middle value after ordering the window; for even `k`, it is the arithmetic mean of the two middle values. Remove the departing occurrence and add the arriving occurrence for each shift. The result has `len(nums) - k + 1` entries and must be computed without sorting every window from scratch.

### Function Contract
**Inputs**

- `nums`: the input integers
- `k`: the window length

**Return value**

- One floating-point median for each of the `len(nums) - k + 1` windows

### Examples
**Example 1**

- Input: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
- Output: `[1, -1, -1, 3, 5, 6]`

**Example 2**

- Input: `nums = [1, 2, 3, 4], k = 2`
- Output: `[1.5, 2.5, 3.5]`

**Example 3**

- Input: `nums = [5], k = 1`
- Output: `[5]`

### Required Complexity

- **Time:** $O(n \log k)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Split the window around its median**

Maintain a max-heap `small` for the lower half and a min-heap `large` for the upper half. Keep either equal valid sizes or one extra valid value in `small`. The median is then the top of `small` for odd `k`, or the average of both tops for even `k`.

**Delete outgoing values lazily**

Binary heaps cannot remove an arbitrary value efficiently. Record each outgoing value in a delayed-deletion counter and decrement the logical size of the heap to which it belongs. Whenever a delayed value reaches a heap top, physically pop it and reduce its pending count. Buried stale entries remain harmless until exposed.

**Rebalance logical heap sizes**

After insertion or erasure, move one top value if `small` has more than one extra valid item or fewer valid items than `large`. Prune the source top after moving because it may expose delayed entries. These rules restore the median invariant before reading either top.

**Why duplicates remain correct**

Delayed deletion counts values rather than identities. Classifying an outgoing value relative to the current lower-half top removes one logical occurrence from the appropriate side; equal copies are interchangeable for the multiset median, and pruning consumes exactly the recorded multiplicity.

#### Complexity detail

Each value is inserted, moved, and physically popped only a constant number of times, with every heap operation costing $O(\log k)$. Across `n` positions the total is $O(n \log k)$ time. Two heaps and delayed counts store $O(k)$ active or pending values.

#### Alternatives and edge cases

- **Balanced ordered multiset:** supports insert, erase, and middle iterators in $O(\log k)$ where the language provides one.
- **Sorted list with binary insertion:** finds positions quickly but shifts $O(k)$ elements for each update.
- **Sort every window independently:** is simple but costs $O((n - k + 1) \cdot k \log k)$.
- **$k = 1$:** every value is its own median.
- **Even window:** average the two central values with floating-point division.
- **Duplicate outgoing value:** delayed multiplicity prevents removing too many equal entries.
- **Negative and large values:** heap ordering and averaging work without special cases.

</details>
