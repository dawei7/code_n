# Number of Subarrays That Match a Pattern II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3036 |
| Difficulty | Hard |
| Topics | Array, Rolling Hash, String Matching, Hash Function |
| Official Link | [number-of-subarrays-that-match-a-pattern-ii](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and a pattern array `pattern` consisting of values -1, 0, and 1, determine how many contiguous subarrays of `nums` of length `len(pattern) + 1` follow the relative order defined by `pattern`. Specifically, for a subarray `nums[i...i+m]`, the pattern matches if for all `j` in `[0, m-1]`:
- `pattern[j] == 1` implies `nums[i+j+1] > nums[i+j]`
- `pattern[j] == 0` implies `nums[i+j+1] == nums[i+j]`
- `pattern[j] == -1` implies `nums[i+j+1] < nums[i+j]`

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `pattern`: A list of integers containing only -1, 0, or 1.

**Return value**

- An integer representing the total count of subarrays in `nums` that satisfy the pattern.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5, 6]`, `pattern = [1, 1]`
- Output: `4`

**Example 2**

- Input: `nums = [1, 4, 4, 1, 3, 5, 5, 3]`, `pattern = [1, 0, -1]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 3, 2, 1]`, `pattern = [1, 1, -1, -1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is equivalent to finding occurrences of a pattern string within a target string. Since the constraints are large, a naive $O(N \cdot M)$ approach is insufficient. We use the **Knuth-Morris-Pratt (KMP)** algorithm. We first transform `nums` into a sequence of relations (1, 0, -1) of length `len(nums) - 1`, then perform string matching to find the occurrences of the `pattern` array within this transformed sequence.

---

## Complexity Analysis
- **Time Complexity**: $O(N + M)$, where $N$ is the length of `nums` and $M$ is the length of `pattern`. The KMP preprocessing takes $O(M)$ and the search takes $O(N)$.
- **Space Complexity**: $O(N + M)$ to store the transformed relation array and the KMP failure function (pi table).
