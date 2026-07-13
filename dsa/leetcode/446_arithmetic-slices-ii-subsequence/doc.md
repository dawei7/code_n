# Arithmetic Slices II - Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 446 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) |

## Problem Description
### Goal
Given an integer array, choose index subsequences of at least three elements while preserving original index order. A subsequence is arithmetic when every difference between consecutive selected values is identical; the common difference may be positive, negative, or zero.

Return the number of qualifying index subsequences. Selected positions need not be contiguous, and different index choices count separately even when duplicate values produce the same value sequence. Longer arithmetic subsequences count once as complete selections and also contain shorter selections that may count independently. Use sufficiently wide arithmetic for value differences and the total count.

### Function Contract
**Inputs**

- `nums`: an integer array from which subsequences retain original index order

**Return value**

- Return the number of arithmetic subsequences of length at least three; equal value sequences use common difference zero.

### Examples
**Example 1**

- Input: `nums = [2, 4, 6, 8, 10]`
- Output: `7`

**Example 2**

- Input: `nums = [7, 7, 7, 7, 7]`
- Output: `16`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `0`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Index dynamic-programming states by endpoint and difference**

Let `dp[i][difference]` count arithmetic subsequences of length at least two that end at index `i` with the given difference. Length-two pairs are retained as intermediate states even though they are not yet included in the answer.

**Extend every earlier endpoint into the current value**

For each pair `left < right`, compute `difference = nums[right] - nums[left]`. Every sequence counted by `dp[left][difference]` can append `nums[right]`, forming a valid sequence of length at least three. Add that count to the answer.

**Store both extensions and the new pair**

At `dp[right][difference]`, add the extended sequences plus one for the new two-element pair `(left, right)`. That pair may become a counted arithmetic subsequence when a later value with the same difference extends it.

**Why every arithmetic subsequence is counted once**

Any qualifying subsequence has a unique final two indices `left, right` and a unique common difference. Removing its final element leaves exactly one state counted at `dp[left][difference]`; processing that pair extends and counts it. Nonmatching differences never share a state, and length-two pairs enter the DP but not the answer.

#### Complexity detail

There are $n(n - 1) / 2$ ordered index pairs, each with average constant-time hash-map work, so time is $O(n^2)$. Across all endpoints, the difference maps can contain $O(n^2)$ states.

#### Alternatives and edge cases

- **Three-index predecessor scan:** store pair states but scan every still-earlier index to find matching differences; this is correct but takes $O(n^3)$ time.
- **Enumerate all subsequences:** tests the condition directly but takes exponential time.
- **Equal values:** difference zero is an ordinary map key and may create many valid subsequences.
- **Duplicate values at different indices:** form distinct subsequences and must retain multiplicity.
- **Fewer than three elements:** no qualifying subsequence exists.
- **Large differences:** use the language's full integer range rather than narrowing subtraction.

</details>
