# Binary Search

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 704 |
| Difficulty | Easy |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-search/) |

## Problem Description
### Goal
Given an integer array `nums` sorted in ascending order and an integer `target`, search for `target` in the array.

If the value exists, return its zero-based index; otherwise return `-1`. The required algorithm must run in $O(\log n)$ time, so it should use the sorted ordering to discard part of the remaining search interval after each comparison rather than scanning every element.

### Function Contract
**Inputs**

- `nums`: a nonempty strictly increasing integer array
- `target`: the value to locate

**Return value**

- The zero-based index of `target`, or `-1` when it is absent

### Examples
**Example 1**

- Input: `nums = [-1,0,3,5,9,12], target = 9`
- Output: `4`

**Example 2**

- Input: `nums = [-1,0,3,5,9,12], target = 2`
- Output: `-1`

**Example 3**

- Input: `nums = [5], target = 5`
- Output: `0`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Maintain the only possible interval**

Start with inclusive boundaries around the complete array. At every iteration, any possible target index lies between `left` and `right`.

**Use the middle value to discard half**

If the middle value equals `target`, return its index. If it is smaller, strict ordering proves the middle and every earlier value are too small, so move `left` past the middle. If it is larger, move `right` before the middle for the symmetric reason.

**Interpret an exhausted interval**

Each nonmatching step removes the checked middle and one impossible half while preserving every possible target position. When `left > right`, no candidate index remains, so returning `-1` is correct.

#### Complexity detail

Each comparison reduces the candidate interval to at most half its previous length, producing $O(\log n)$ iterations. The algorithm stores only two boundaries and a middle index, using $O(1)$ extra space.

#### Alternatives and edge cases

- **Half-open lower-bound search:** maintain `[left, right)` and locate the first value not smaller than `target`; verify equality before returning.
- **Linear scan:** stop at `target` or the first larger value; it is correct but takes $O(n)$ time in the worst case.
- The target may appear at either endpoint or in a one-element array.
- A target below the minimum or above the maximum returns `-1`.
- Strictly increasing input means a successful result is unique.
- Updating past the middle, rather than to the middle, is necessary to guarantee progress.

</details>
