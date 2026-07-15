# Maximum Subarray Sum with One Deletion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) |

## Problem Description

### Goal

Given an integer array `arr`, choose a non-empty subarray—that is, a contiguous range of its elements. From the chosen subarray, you may optionally delete at most one element, and you want the sum of the elements that remain to be as large as possible.

Return that maximum sum. Deletion is optional, so an unchanged subarray is allowed. If an element is deleted, at least one element must still remain; deleting the only element of a length-one subarray to obtain an empty result is forbidden.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $1\le n\le10^5$ and $-10^4\le\texttt{arr[i]}\le10^4$.

**Return value**

- The maximum sum obtainable from a non-empty subarray after deleting zero or one of its elements.

### Examples

**Example 1**

- Input: `arr = [1,-2,0,3]`
- Output: `4`

Choose the entire subarray and delete `-2`; the remaining elements sum to `1 + 0 + 3 = 4`.

**Example 2**

- Input: `arr = [1,-2,-2,3]`
- Output: `3`

Choosing the one-element subarray `[3]` is better than connecting the separated positive values.

**Example 3**

- Input: `arr = [-1,-1,-1,-1]`
- Output: `-1`

The result cannot be empty, so deleting the only value from a one-element choice cannot produce zero.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track whether deletion has been used.** After processing an index, `kept` is the maximum sum of a non-empty subarray ending at that index with no deletion. `deleted` is the corresponding maximum when exactly one element in the chosen range has been removed and the remaining sequence is still non-empty.

**Update the no-deletion state.** For current value `value`, either start a new subarray at this element or extend the previous one, giving `kept = max(value, previous_kept + value)`. This is Kadane's recurrence.

**Update the deletion state without losing the old values.** There are two ways to end at the current position after one deletion. Delete the current value, leaving `previous_kept` as the non-empty remaining sum, or retain it after an earlier deletion, giving `previous_deleted + value`. Therefore assign `deleted = max(previous_kept, previous_deleted + value)` before overwriting the prior state. The maximum observed value across both states includes every valid subarray with zero or one deletion. Initializing from `arr[0]` and treating the deletion state as impossible prevents an empty result from winning when all values are negative.

#### Complexity detail

Each of the $n$ values performs a constant number of additions and comparisons, so the time is $O(n)$. Only the two rolling dynamic-programming states and the best answer are retained, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix and suffix Kadane arrays:** Compute the best sum ending and starting at every index, then join the two sides around each deletion. This is also $O(n)$ time but uses $O(n)$ space.
- **Try every deleted index:** Running Kadane's algorithm once for each possible deletion is correct but costs $O(n^2)$ time.
- **All-negative array:** The best answer is the largest single element; deletion cannot create an empty subarray with sum zero.
- **Single element:** No deletion is usable because one element must remain, so return that element.
- **No beneficial deletion:** The `kept` state preserves the ordinary maximum subarray.
- **Deletion at a boundary:** Deleting the first or last element of a longer chosen range is equivalent to choosing the shorter remaining subarray, already covered by starting or ending the range there.
- **Zero values:** A zero may remain, be deleted, or form the answer by itself when every other option is negative.

</details>
