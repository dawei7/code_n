# Apply Operations to Make Sum of Array Greater Than or Equal to k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3091 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/) |

## Problem Description

### Goal

Start with the one-element array `nums = [1]`. A positive integer `k` is given, and either of two operations may be performed any number of times, including zero times.

One operation may select an existing element and increase its value by `1`. Alternatively, one operation may duplicate any existing element and append that copy to the array. Determine the minimum total number of operations needed for the sum of the final array to be greater than or equal to `k`.

### Function Contract

**Inputs**

- `k`: the required lower bound for the final array sum, where $1 \leq k \leq 10^5$.

**Return value**

Return the minimum number of increment and duplication operations whose resulting array has sum at least `k`.

### Examples

**Example 1**

- Input: `k = 11`
- Output: `5`
- Explanation: Increase the initial value three times to obtain `[4]`, then duplicate that value twice to obtain `[4, 4, 4]`. The sum is `12`, and the construction uses five operations.

**Example 2**

- Input: `k = 1`
- Output: `0`
- Explanation: The initial array already has sum `1`, so no operation is necessary.

**Example 3**

- Input: `k = 9`
- Output: `4`
- Explanation: Two increments followed by two duplications produce `[3, 3, 3]`, whose sum is `9`.
