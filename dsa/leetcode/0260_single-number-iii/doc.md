# Single Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 260 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/single-number-iii/) |

## Problem Description
### Goal
Given an integer array, exactly two distinct values occur once and every other distinct value occurs exactly twice. Paired occurrences may appear anywhere and need not be adjacent, while the two singleton values may be negative, positive, or zero.

Return the two singleton values in any order, with each appearing once in the result. The task asks for values rather than their indices. Meet the required linear running time and constant extra space instead of sorting the array or storing frequencies for all distinct values, and do not cancel the two different singleton values against each other.

### Function Contract
**Inputs**

- `nums`: an integer array containing exactly two singleton values

**Return value**

The two singleton values in either order.

### Examples
**Example 1**

- Input: `nums = [1,2,1,3,2,5]`
- Output: `[3,5]`

**Example 2**

- Input: `nums = [-1,0]`
- Output: `[-1,0]`

**Example 3**

- Input: `nums = [0,1]`
- Output: `[0,1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Pair cancellation reveals how the singletons differ**

XOR every value. Paired values cancel, leaving `first ^ second`. Its lowest set bit identifies a position on which the two singleton values differ.

**One set bit separates the two unknown values**

XOR values into two groups according to the distinguishing bit. Equal pairs enter the same group and cancel; the two singletons enter different groups.

**Each partition cancels independently**

After any prefix, each group accumulator equals the XOR of values assigned to that group. At completion all pairs contribute zero, leaving exactly one singleton in each accumulator. The selected bit guarantees they cannot land together.

#### Complexity detail

Two linear passes take $O(n)$ time. The total XOR, mask, and two accumulators use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Frequency map:** takes linear time but $O(n)$ extra space.
- **Count every candidate:** can take $O(n^2)$.
- XOR and the lowest-set-bit operation work for zero and negative Python integers as well.

</details>
