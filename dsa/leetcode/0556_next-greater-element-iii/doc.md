# Next Greater Element III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 556 |
| Difficulty | Medium |
| Topics | Math, Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-element-iii/) |

## Problem Description
### Goal
Given a positive integer `n` that fits in signed 32-bit range, rearrange exactly its existing decimal digit occurrences without adding or deleting any digit. Among the rearrangements strictly greater than `n`, find the smallest numerical value.

Return that next greater value when it exists and still fits in a signed 32-bit integer; otherwise return `-1`. Repeated digits remain separate occurrences, leading zeroes cannot create a valid shorter representation, and a merely larger permutation is insufficient when another valid permutation lies numerically closer to the original.

### Function Contract
**Inputs**

- `n`: a positive signed 32-bit integer

**Return value**

- The next greater integer using exactly the same digits, or `-1`

### Examples
**Example 1**

- Input: `n = 12`
- Output: `21`

**Example 2**

- Input: `n = 21`
- Output: `-1`

**Example 3**

- Input: `n = 230241`
- Output: `230412`

### Required Complexity

- **Time:** $O(d)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Find the longest non-increasing suffix**

Scan digits from right to left while each digit is at least the one after it. That suffix is already the largest arrangement of its digits, so no change confined entirely inside it can produce a greater number. The digit immediately before it is the rightmost pivot that can be increased.

**Swap in the smallest possible larger digit**

Because the suffix is non-increasing, scan from its right end to find the first digit greater than the pivot. This is the smallest available digit that can increase the prefix. Swapping it with the pivot makes the number greater while changing the most significant possible position as little as possible.

**Minimize everything after the pivot**

The suffix remains in non-increasing order after the swap. Reverse it to obtain non-decreasing order, which is the smallest arrangement of the remaining digits and therefore the closest number above the input.

**Reject impossible and overflowing results**

If no pivot exists, the digits are globally non-increasing and already form their largest permutation. Otherwise convert the new digit sequence and return it only when it does not exceed $2^{31} - 1$.

**Why this is the immediate next value**

Every greater permutation must first differ from the input at some position it increases. Choosing the rightmost possible pivot preserves the longest prefix. At that pivot, choosing the smallest larger suffix digit gives the least possible increase, and sorting the remaining suffix ascending gives its least completion. No other greater arrangement can lie between the constructed value and the input.

#### Complexity detail

For `d` digits, the pivot scan, successor scan, and suffix reversal each take $O(d)$ time. The mutable digit list uses $O(d)$ space.

#### Alternatives and edge cases

- **Enumerate digit permutations:** can find the answer by comparison but takes factorial time.
- **Sort every candidate suffix:** works after choosing a pivot but costs $O(d \log d)$; reversal is sufficient because the suffix is already monotone.
- **Descending digits:** have no greater permutation and return `-1`.
- **Repeated digits:** the successor must be strictly greater than the pivot, not merely different.
- **Single digit:** has no alternative arrangement.
- **Zero inside the number:** remains an ordinary digit; the pivot construction never creates a leading zero for a greater positive result.
- **32-bit overflow:** a valid greater permutation still returns `-1` when it exceeds $2^{31} - 1$.

</details>
