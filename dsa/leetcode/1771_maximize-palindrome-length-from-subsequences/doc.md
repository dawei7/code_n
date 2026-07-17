# Maximize Palindrome Length From Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1771 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) |

## Problem Description

### Goal

You are given strings `word1` and `word2`. Choose a nonempty subsequence from each word, then concatenate the subsequence from `word1` before the subsequence from `word2`.

The concatenated string must be a palindrome. Return the maximum possible length, or `0` when no such palindrome can use characters from both words.

A subsequence may delete any characters while preserving the relative order of those retained. A palindrome reads identically from left to right and right to left.

### Function Contract

**Inputs**

- `word1`: a lowercase English string with $1 \le A \le 1000$, where $A=\lvert\texttt{word1}\rvert$.
- `word2`: a lowercase English string with $1 \le B \le 1000$, where $B=\lvert\texttt{word2}\rvert$.

Let $L=A+B$.

**Return value**

- Return the greatest length of a palindrome expressible as a nonempty subsequence of `word1` followed by a nonempty subsequence of `word2`.
- Return `0` if no qualifying palindrome exists.

### Examples

**Example 1**

- Input: `word1 = "cacb", word2 = "cbba"`
- Output: `5`
- Explanation: Choose `"ab"` from `word1` and `"cba"` from `word2` to form `"abcba"`.

**Example 2**

- Input: `word1 = "ab", word2 = "ab"`
- Output: `3`
- Explanation: The subsequences `"ab"` and `"a"` concatenate to `"aba"`.

**Example 3**

- Input: `word1 = "aa", word2 = "bb"`
- Output: `0`
- Explanation: No character from one word can pair across the palindrome with a character from the other.

### Required Complexity

- **Time:** $O(L^2)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Preserve concatenation order in one string**

Form `combined = word1 + word2`. Any subsequence of `combined` consists of some characters from `word1` followed by some characters from `word2`, exactly matching the required concatenation order. The remaining challenge is ensuring that an accepted palindrome uses at least one character from each side of the boundary.

**Build longest palindromic subsequences by interval**

For an interval with endpoints `left` and `right`, matching endpoint characters can surround the best palindromic subsequence strictly inside them, adding two characters. When they differ, the best result omits one endpoint and takes the better adjacent interval. Single-character intervals have length one.

**Require a matched pair across the boundary**

Whenever equal endpoints satisfy `left < A <= right`, the constructed palindrome necessarily uses the left endpoint from `word1` and the right endpoint from `word2`. Its interior may use either word, but the two required nonempty subsequences are already guaranteed. Record the largest such interval value rather than returning the unrestricted LPS of the complete concatenation.

Every valid palindrome using both words has an outermost character chosen from `word1` and an outermost matching character chosen from `word2`: all `word1` characters precede all `word2` characters in the concatenation. Therefore considering every equal cross-boundary endpoint pair cannot miss an optimum. Conversely, every recorded candidate is palindromic by the interval recurrence and contains both endpoints, so it satisfies the contract.

**Compress interval rows into one array**

Process `left` from right to left and `right` from left to right. Before updating a cell, `lengths[right]` stores the interval below it, `lengths[right - 1]` stores the current row's interval to its left, and a saved `diagonal` value stores the previous row's inner interval. These are exactly the three dependencies of the recurrence, allowing $O(L)$ storage.

#### Complexity detail

The algorithm evaluates one state for every pair with `left <= right`, totaling $L(L+1)/2$ states and $O(L^2)$ time. The rolling array has $L$ entries and all other state is constant-sized, giving $O(L)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate both subsequences:** Trying all nonempty subsequence pairs takes exponential time in $A+B$.
- **Full interval table:** A conventional LPS table is correct and easier to visualize, but requires $O(L^2)$ space.
- **Unrestricted LPS:** Returning the longest palindrome in `word1 + word2` can incorrectly choose characters from only one word.
- **No shared character:** Without an equal cross-boundary pair, no valid palindrome exists and the result is `0`.
- **Single matching characters:** One character from each word forms a length-two palindrome.
- **Odd-length palindrome:** The center may come from either word; only the outer cross-boundary pair is required.
- **Repeated letters:** All endpoint positions are considered, so the best inner ordering is preserved.
- **Palindrome wholly inside one word:** It is ignored unless a matching pair from opposite words can surround an appropriate interior subsequence.

</details>
