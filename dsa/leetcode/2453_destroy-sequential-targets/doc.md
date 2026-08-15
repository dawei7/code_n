# Destroy Sequential Targets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2453 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Destroy Sequential Targets](https://leetcode.com/problems/destroy-sequential-targets/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of positive integers representing targets on a number line, together with a positive integer `space`. If the machine is seeded with a chosen value `nums[i]`, it destroys every target whose value can be written as `nums[i] + c * space` for some non-negative integer `c`.

Choose a seed from `nums` that destroys the greatest possible number of array entries. Duplicate values represent separate targets and are counted separately. If several seed values attain the maximum, return the smallest such value.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive target values, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `space`: The positive gap between reachable values, where $1 \le \texttt{space} \le 10^9$.

**Return value**

- The smallest seed value from `nums` that destroys the maximum number of targets.

### Examples

#### Example 1

- **Input:** `nums = [3, 7, 8, 1, 1, 5], space = 2`
- **Output:** `1`
- **Explanation:** Seeding with 1 destroys both targets valued 1 and the targets 3, 5, and 7, for five targets total.

#### Example 2

- **Input:** `nums = [1, 3, 5, 2, 4, 6], space = 2`
- **Output:** `1`
- **Explanation:** Seeds 1 and 2 each destroy three targets, so the smaller seed is returned.

#### Example 3

- **Input:** `nums = [6, 2, 5], space = 100`
- **Output:** `2`
- **Explanation:** No seed reaches another target, so every seed destroys one target and the smallest wins.
