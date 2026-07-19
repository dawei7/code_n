# How Many Numbers Are Smaller Than the Current Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1365 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) |

## Problem Description

### Goal

Given an integer array `nums`, produce one answer for every index. For the value at index $i$, count the indices $j$ such that $j\ne i$ and `nums[j]` is strictly smaller than `nums[i]`.

Preserve the original input order in the returned array. Equal values do not count as smaller, so every occurrence of the same value receives the same result even when that value appears several times.

### Function Contract

**Inputs**

- `nums`: an array of $n$ integers, each in the inclusive range from $0$ through $100$.
- Let $U=101$ be the number of possible input values.

**Return value**

- A length-$n$ array whose entry at index $i$ is the number of input elements strictly smaller than `nums[i]`.

### Examples

**Example 1**

- Input: `nums = [8,1,2,2,3]`
- Output: `[4,0,1,1,3]`

**Example 2**

- Input: `nums = [6,5,4,8]`
- Output: `[2,1,0,3]`

**Example 3**

- Input: `nums = [7,7,7,7]`
- Output: `[0,0,0,0]`
