# Valid Palindrome III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1216 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-palindrome-iii/) |

## Problem Description

### Goal

A string is a **`k`-palindrome** when it can be transformed into a palindrome by removing at most `k` characters. The remaining characters keep their original relative order; removals may be made at any positions and do not need to be contiguous.

Given a string `s` and an integer `k`, return `true` if `s` is a `k`-palindrome. Otherwise, return `false`.

### Function Contract

**Inputs**

- `s`: A string of $n$ lowercase English letters, where $1\le n\le1000$.
- `k`: The maximum permitted number of removed characters, where $1\le k\le n$.

**Return value**

- `true` if removing at most `k` characters from `s` can leave a palindrome; otherwise `false`.

### Examples

**Example 1**

- Input: `s = "abcdeca"`, `k = 2`
- Output: `true`

Removing `b` and `e` leaves `acdca`, which is a palindrome.

**Example 2**

- Input: `s = "abbababa"`, `k = 1`
- Output: `true`

Removing the second character leaves `abababa`.

**Example 3**

- Input: `s = "abc"`, `k = 1`
- Output: `false`

At least two removals are needed to leave a palindrome.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Measure the minimum removals for every interval.** For an interval from `left` through `right`, matching endpoint characters can both remain, so its minimum equals the answer for the interior interval. When the endpoints differ, at least one must be removed; choose the cheaper of removing the left endpoint or the right endpoint, then add one.

**Compress the interval table into one row.** Process `left` from right to left and `right` from `left + 1` toward the end. Before an update, `dp[right]` represents the interval beginning at `left + 1`; after the update it represents the interval beginning at `left`. Meanwhile, `dp[right - 1]` already holds the current row's shorter interval. Keep the overwritten diagonal value in a scalar so matching endpoints can reuse the interior result.

**Why the final comparison is sufficient.** The recurrence considers both possible endpoint removals whenever a mismatch forces a choice, and it removes neither endpoint when they already match. By increasing interval length, every transition therefore uses exact results for smaller intervals and computes the minimum removals for its own interval. At completion, `dp[n - 1]` is the minimum for all of `s`; the string is a `k`-palindrome exactly when this value is at most `k`.

#### Complexity detail

There are $O(n^2)$ intervals and each update performs constant work, so the time is $O(n^2)$. The rolling array contains $n$ integers and the saved diagonal uses constant additional storage, giving $O(n)$ space.

#### Alternatives and edge cases

- **Longest palindromic subsequence:** The minimum removal count is $n-L$, where $L$ is the longest palindromic subsequence length. Computing $L$ with dynamic programming has the same asymptotic bounds when rows are compressed.
- **Longest common subsequence with the reverse:** Comparing `s` with `s[::-1]` also yields the longest palindromic subsequence length, but a full table uses $O(n^2)$ space and obscures the direct removal recurrence.
- **Unmemoized endpoint recursion:** Trying both removals at every mismatch is logically correct but repeats overlapping intervals and can take exponential time.
- **Already palindromic string:** Its minimum removal count is zero, so it qualifies for every allowed `k`.
- **Entire string may be removed:** Because `k` may equal $n$, even a string with no longer palindromic subsequence can qualify.
- **Noncontiguous removals:** The retained palindrome is a subsequence, not necessarily a substring.
- **Exact budget:** A minimum count equal to `k` must return `true` because the condition is at most `k`.

</details>
