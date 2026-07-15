# Check If All 1's Are at Least Length K Places Away

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1437 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/) |

## Problem Description

### Goal

Given a binary array `nums`, determine whether every two entries equal to `1` are separated by at least `k` array positions. For ones at indices $i<j$, this means that the number of intervening positions, $j-i-1$, must be at least $k$.

Return `true` when the condition holds for the entire array. Arrays with fewer than two ones satisfy it automatically, and when $k=0$, adjacent ones are permitted because zero intervening positions are required.

### Function Contract

**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 10^5$.
- `k`: the required minimum number of positions between ones, where $0 \le k \le n$.

**Return value**

- `true` if every pair of ones is at least $k$ places apart; otherwise `false`.

### Examples

**Example 1**

- Input: `nums = [1,0,0,0,1,0,0,1], k = 2`
- Output: `true`

**Example 2**

- Input: `nums = [1,0,0,1,0,1], k = 2`
- Output: `false`

**Example 3**

- Input: `nums = [0,1,0,0,1], k = 1`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Remember only the most recent one.** Scan `nums` from left to right and store the index `previous` of the last encountered `1`. Zero entries require no update.

**Translate the spacing rule into an index gap.** At a new one at index `i`, there are `i - previous - 1` positions between it and the preceding one. The requirement fails exactly when this count is smaller than `k`, equivalently when `i - previous <= k`. Return `false` immediately in that case; otherwise update `previous = i`.

**Why consecutive ones are sufficient.** Among all earlier ones, the most recent has the largest index and therefore the smallest distance to the current one. If the current one is far enough from that nearest predecessor, it is even farther from every earlier one. Checking each consecutive pair of ones consequently proves the condition for every pair. If no check fails, return `true`.

#### Complexity detail

The scan examines each of the $n$ entries once, giving $O(n)$ time. One previous index is retained, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Compare every pair of ones:** This directly checks the definition but can take $O(n^2)$ time when the array contains many ones.
- **Collect all one indices:** Comparing adjacent collected indices is linear but uses $O(n)$ extra space unnecessarily.
- **No ones or one one:** There is no pair that can violate the condition, so return `true`.
- **Zero required spacing:** Every binary array is valid because adjacent ones have zero positions between them.
- **Exact boundary:** An index gap of `k + 1` leaves exactly `k` positions and is valid.
- **Leading and trailing zeroes:** They do not affect distances between ones.

</details>
