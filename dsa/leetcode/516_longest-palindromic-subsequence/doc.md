# Longest Palindromic Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 516 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/) |

## Problem Description
### Goal
Given a nonempty lowercase string `s`, form a subsequence by deleting zero or more characters without changing the relative order of the characters retained. A palindromic subsequence reads identically from left to right and from right to left.

Return the maximum possible length of such a subsequence. Selected characters do not need to be contiguous, repeated occurrences at different positions remain separate choices, and the function returns only the optimal length rather than the subsequence itself. A one-character selection is always palindromic, while matching outer characters can surround a smaller palindromic subsequence.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase English string

**Return value**

- The length of the longest palindromic subsequence of `s`

### Examples
**Example 1**

- Input: `s = "bbbab"`
- Output: `4`

**Example 2**

- Input: `s = "cbbd"`
- Output: `2`

**Example 3**

- Input: `s = "a"`
- Output: `1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Define an interval optimum**

For indices `left <= right`, let the interval value be the longest palindromic subsequence inside `s[left:right + 1]`. A one-character interval has value one. If its endpoints match, they can surround an optimal subsequence from the interior, giving `2 + value(left + 1, right - 1)`. If they differ, at least one endpoint is excluded, so take the maximum of the intervals that drop the left or right endpoint.

**Compress interval rows into one array**

Process `left` from right to left. Before updating, `dp[right]` stores the value for `(left + 1, right)`. During the left-to-right inner scan, `dp[right - 1]` has already become the value for `(left, right - 1)`, while a variable named `diagonal` retains the old value for `(left + 1, right - 1)`.

**Preserve the overwritten diagonal**

Save the old `dp[right]` before writing the current interval, then assign it to `diagonal` for the next column. This makes all three recurrence dependencies available with one array. Once `left` reaches zero, `dp[n - 1]` represents the complete string.

**Why matching endpoints may both be chosen**

When endpoints match, any palindromic subsequence of the interior remains palindromic after placing that character at both ends. Conversely, an optimal solution using both endpoints leaves a palindromic interior; a solution using at most one endpoint is no longer than an optimum from one of the endpoint-dropped intervals, which is already bounded by the matched-end recurrence. Thus the transition covers an optimum in both cases.

#### Complexity detail

There are $n(n + 1) / 2$ intervals and each transition is constant time, giving $O(n^2)$ time. The compressed DP array contains `n` integers, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Two-dimensional interval table:** mirrors the recurrence directly in $O(n^2)$ time and space.
- **Longest common subsequence with the reversed string:** produces the same length in $O(n^2)$ time and can also be space-compressed.
- **Memoized recursion:** evaluates only interval states that are reached but may use $O(n^2)$ cache and call-stack space.
- **Unmemoized recursion:** repeats overlapping intervals and takes exponential time.
- **One character:** has answer one.
- **All distinct characters:** any single character is an optimal palindrome.
- **All equal characters:** the entire string is palindromic.
- **Subsequence versus substring:** skipped characters are allowed; contiguity is not required.

</details>
