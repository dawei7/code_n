# Palindrome Removal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1246 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-removal/) |

## Problem Description

### Goal

You are given an integer array `arr`. In one move, choose any nonempty contiguous subarray that is a palindrome and remove all of its elements. After removal, the elements on its left and right concatenate and become adjacent.

Repeat until the array is empty, and return the minimum possible number of moves. A single element is always a palindrome, but removing some middle elements first may bring equal values together and allow a larger palindrome to be removed in fewer later moves.

### Function Contract

**Inputs**

- `arr`: A list of $n$ integers, where $1\le n\le100$ and $1\le\texttt{arr[i]}\le20$.

**Return value**

- The minimum number of palindromic-subarray removals needed to delete the entire array.

### Examples

**Example 1**

- Input: `arr = [1,2]`
- Output: `2`

The two unequal values must be removed separately.

**Example 2**

- Input: `arr = [1,3,4,1,5]`
- Output: `3`

Remove `[4]`, then `[1,3,1]`, then `[5]`.

**Example 3**

- Input: `arr = [1,2,1]`
- Output: `1`

The full array is already a palindrome.

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Define an interval state.** Let `dp[left][right]` be the fewest moves needed to remove the original interval from `left` through `right`. A one-element interval costs one move, and an empty interval contributes zero.

**Allow the left value to leave alone.** Removing `arr[left]` as a singleton and then optimally clearing the suffix gives `1 + dp[left + 1][right]`. This is always valid and supplies an initial upper bound.

**Merge the left value with a matching value.** If `arr[left] == arr[left + 1]`, those two can disappear together in one move, followed by the rest. More generally, for a matching position `middle >= left + 2`, first remove everything strictly between the equal values. They then become adjacent and can be absorbed into the same removal plan as the right copy, so the cost is `dp[left + 1][middle - 1] + dp[middle + 1][right]`. Try every matching position and retain the minimum.

Fill intervals from shorter to longer so every referenced interior or suffix state is already known. Any optimal plan either removes the left value without a later matching partner, or eventually removes it together with some equal value after the intervening interval disappears; the recurrence covers both exhaustive cases.

#### Complexity detail

There are $O(n^2)$ intervals. For each interval, the recurrence may scan $O(n)$ matching positions, yielding $O(n^3)$ time. The two-dimensional dynamic-programming table uses $O(n^2)$ space.

#### Alternatives and edge cases

- **Unmemoized recursion:** It follows the same exact recurrence but recomputes intervals exponentially many times.
- **Remove the longest current palindrome greedily:** A locally largest removal can destroy a better sequence of future merges and is not generally optimal.
- **Enumerate every palindromic subarray per state:** This explores many equivalent removal orders and grows far faster than interval DP.
- **Single element:** One move is necessary and sufficient.
- **Whole-array palindrome:** The answer is `1` because the full interval may be removed immediately.
- **All values distinct:** No multi-element palindrome can form, so every value requires its own move.
- **Equal adjacent pair:** Handle it as one move even when additional elements remain to the right.

</details>
