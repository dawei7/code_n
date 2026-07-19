# Maximum Binary String After Change

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1702 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-binary-string-after-change/) |

## Problem Description
### Goal

You are given a binary string `binary`. Any occurrence of `00` may be replaced by `10`, and any occurrence of `10` may be replaced by `01`. Either operation may be applied any number of times and at any positions made available by earlier changes.

Return the greatest binary string reachable under these rules. All reachable strings retain the original length. One binary string is greater than another when its value as a base-two integer is greater, so the earliest differing position determines which equal-length result is better.

### Function Contract
**Inputs**

- `binary`: a string of length $n$ containing only `0` and `1`, where $1 \le n \le 10^5$

**Return value**

The lexicographically and numerically maximum length-$n$ binary string obtainable through the allowed `00` to `10` and `10` to `01` replacements.

### Examples
**Example 1**

- Input: `binary = "000110"`
- Output: `"111011"`

Repeated moves eliminate all but one zero and place that zero at index `3`.

**Example 2**

- Input: `binary = "01"`
- Output: `"01"`

Neither allowed two-character pattern occurs, so the input is already maximal.

**Example 3**

- Input: `binary = "11000"`
- Output: `"11110"`

The two leading ones remain fixed, while the three-zero suffix is transformed to contain one zero at its final position.
