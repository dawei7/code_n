# Most Frequent Number Following Key In an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2190 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums` and a value `key` that occurs in it,
consider every index $i$ from $0$ through
$\lvert\texttt{nums}\rvert-2$ where `nums[i] == key`. For each such
occurrence, the immediately following value `nums[i + 1]` is one observed
target.

Count these observations separately for every target value, then return the
target with the greatest count. An occurrence of `key` at the final index has
no follower and contributes nothing. The input guarantees that exactly one
target has the maximum count.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $2\le n\le1000$ and every
  value lies in `[1,1000]`.
- `key`: a value that occurs in `nums`.

**Return value**

Return the unique value that most frequently appears immediately after `key`.

### Examples

#### Example 1

- **Input:** `nums = [1,100,200,1,100]`, `key = 1`
- **Output:** `100`

#### Example 2

- **Input:** `nums = [2,2,2,2,3]`, `key = 2`
- **Output:** `2`

#### Example 3

- **Input:** `nums = [3,4,5,3]`, `key = 3`
- **Output:** `4`
