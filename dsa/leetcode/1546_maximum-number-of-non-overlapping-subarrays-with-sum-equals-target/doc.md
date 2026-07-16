# Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1546 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, select as many contiguous subarrays as possible such that every selected subarray has sum exactly equal to `target`. Selected subarrays must be pairwise non-overlapping: no array position may belong to more than one of them.

Return the maximum possible number of selected subarrays. Values may be positive, negative, or zero, so a sliding window based on monotonic growth is not generally valid, and locally overlapping target-sum candidates may require choosing the one that leaves the most room for later selections.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.
- `target`: the required sum of every selected subarray, where $-10^6 \le \texttt{target} \le 10^6$.

**Return value**

The largest number of pairwise non-overlapping contiguous subarrays whose sums equal `target`.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 2`
- Output: `2`
- Explanation: Two disjoint length-two subarrays can be selected; one element remains unused.

**Example 2**

- Input: `nums = [-1, 3, 5, 1, 4, 2, -9], target = 6`
- Output: `2`
- Explanation: Negative values allow several candidate boundaries, but at most two target-sum intervals can be disjoint.

**Example 3**

- Input: `nums = [3, 4, 7, 2, -3, 1, 4, 2], target = 7`
- Output: `3`
- Explanation: The subarrays `[3, 4]`, `[7]`, and `[1, 4, 2]` are pairwise non-overlapping and each sums to seven.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recognize a target-sum interval with prefix sums**

Within the portion of the array that remains available, maintain the running prefix sum and a set of prefix sums seen since the last selected interval ended. A subarray ending at the current position sums to `target` exactly when an earlier prefix equals `prefix - target`. Initializing the set with zero also recognizes an interval that starts at the beginning of the currently available portion.

**Greedily take the earliest finishing interval**

As soon as any target-sum subarray ends, select one and increment the answer. This is the standard earliest-finish rule for maximizing the number of non-overlapping intervals: if an optimal selection uses a first interval ending later, replacing it with the currently found interval cannot invalidate any subsequent interval and leaves at least as much suffix available. Repeating the exchange argument after each selection proves that the greedy count is optimal.

The exact starting boundary of the chosen interval does not need to be recovered, because all earlier positions become unavailable regardless. Only its earliest possible ending matters to the remaining capacity.

**Reset state at the chosen boundary**

After accepting an interval, clear all prior prefix sums and restart with prefix zero immediately after its end. This prevents every later recognized interval from reaching back into already consumed positions. If no interval ends at the current element, add the current prefix to the set and continue.

This scan recognizes the earliest possible finishing interval in each remaining suffix, selects it, and then applies the same argument independently to what remains. Therefore every counted interval is valid and disjoint, and no alternative selection can contain more intervals.

#### Complexity detail

The algorithm visits each of the $n$ values once. Prefix addition, set membership, insertion, and reset take expected constant time, giving $O(n)$ expected time. At most $n+1$ distinct prefix sums can be stored before a selection, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Dynamic programming over all intervals:** test every start and end while tracking the best count before each start; this is correct but takes $O(n^2)$ time.
- **Enumerate then schedule intervals:** collecting every target-sum interval can itself require $O(n^2)$ output space before interval scheduling begins.
- **Sliding window:** shrinking based on whether the sum is too large fails when negative values destroy monotonicity.
- A selected subarray may contain one element.
- The answer can be zero when no contiguous sum equals `target`.
- When `target = 0`, individual zeroes and longer cancelling ranges must both be handled.
- Resetting the prefix set after a selection is essential; retaining old prefixes can count overlapping intervals.
- Repeated prefix sums are valid and naturally handled by a set because only existence, not multiplicity, is needed.
- Negative targets and negative array values require no special branch.

</details>
