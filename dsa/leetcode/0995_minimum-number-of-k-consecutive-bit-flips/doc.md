# Minimum Number of K Consecutive Bit Flips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 995 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) |

## Problem Description

### Goal

You are given a binary array `nums` and an integer `k`. A k-bit flip selects a contiguous subarray of length `k` and changes all of its bits simultaneously: every `0` becomes `1`, and every `1` becomes `0`.

Return the minimum number of k-bit flips needed to leave no `0` anywhere in the array. A selected range must contain exactly `k` consecutive positions; if no sequence of such operations can turn the whole array into ones, return `-1`.

### Function Contract

**Inputs**

- `nums`: a binary list of length $N$, where $1\le N\le10^5$.
- `k`: the length of every flipped subarray, where $1\le\texttt{k}\le N$.

**Return value**

- The minimum number of k-bit flips that changes every bit to `1`, or `-1` when this is impossible.

### Examples

**Example 1**

- Input: `nums = [0, 1, 0], k = 1`
- Output: `2`
- Explanation: Flip the first and third individual bits.

**Example 2**

- Input: `nums = [1, 1, 0], k = 2`
- Output: `-1`
- Explanation: No sequence of length-two flips produces three ones.

**Example 3**

- Input: `nums = [0, 0, 0, 1, 0, 1, 1, 0], k = 3`
- Output: `3`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The leftmost effective zero forces a decision:** Scan from left to right. Once position `i` is reached, no future flip starting to its right can change it. If its effective bit is zero, an optimal solution is therefore forced to start a length-`k` flip at `i`; if fewer than `k` positions remain, the task is impossible.

**Track only the parity of active flips:** A bit is inverted when an odd number of previously started windows still covers it. Maintain this parity instead of physically changing all `k` bits. When a forced flip starts, toggle the parity and mark its start position with a sentinel value. At index `i`, a marked start at `i - k` has just expired, so toggle the parity again before inspecting the current bit.

For an original binary bit, `nums[i] == parity` means that applying the active inversions produces zero, so a new flip is required. Every chosen flip is forced by the earliest unresolved zero; induction over the scan positions therefore proves both feasibility and minimality.

#### Complexity detail

The scan performs constant work at each of the $N$ positions, giving $O(N)$ time. Reusing processed entries of `nums` as flip-start markers requires $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Physically toggle every chosen window:** The same greedy starts are correct, but changing all `k` entries per operation can take $O(Nk)$ time.
- **Difference or expiration array:** Recording where each flip ends also gives $O(N)$ time, but consumes $O(N)$ additional space.
- **Insufficient suffix:** If an effective zero occurs after the final legal start index, return `-1`.
- **Window length one:** Each zero must be flipped independently, so the answer is the number of zeros.
- **Already all ones:** No flip is needed regardless of `k`.

</details>
