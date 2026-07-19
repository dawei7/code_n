# Happy Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 202 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/happy-number/) |

## Problem Description
### Goal
Starting with a positive integer `n`, repeatedly replace the current value by the sum of the squares of its decimal digits. For example, each occurrence of a digit contributes independently, and the process continues using the digits of the newly produced value.

Return `True` if this sequence eventually reaches `1`, after which it remains there. Return `False` if the process instead repeats a previous non-one value and enters a cycle that can never reach `1`. The task asks only for this classification, not for the sequence itself or the number of transformations performed.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

`True` when the sequence reaches one; otherwise `False` when it enters a non-one cycle.

### Examples
**Example 1**

- Input: `19`
- Output: `True`

**Example 2**

- Input: `2`
- Output: `False`

**Example 3**

- Input: `1`
- Output: `True`
