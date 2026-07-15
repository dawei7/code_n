# Remove Palindromic Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1332 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-palindromic-subsequences/) |

## Problem Description
### Goal
Given a non-empty string `s` containing only the letters `a` and `b`, repeatedly remove a palindromic subsequence until the string is empty. A subsequence keeps the relative order of its chosen characters but does not have to occupy consecutive positions. A palindrome reads identically from left to right and from right to left.

Return the minimum number of removal steps. Each step may choose any non-empty palindromic subsequence of the current string.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1\le n\le1000$ and every character is either `a` or `b`.

**Return value**

The minimum number of palindromic subsequences that must be removed to empty `s`.

### Examples
**Example 1**

- Input: `s = "ababa"`
- Output: `1`
- Explanation: The complete string is a palindrome and can be removed at once.

**Example 2**

- Input: `s = "abb"`
- Output: `2`
- Explanation: Remove `"a"`, then remove `"bb"`.

**Example 3**

- Input: `s = "baabb"`
- Output: `2`
- Explanation: For example, remove `"baab"` and then the remaining `"b"`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the answer to a palindrome test**

If `s` is already a palindrome, removing the whole string is a legal single step. Because the input is non-empty, zero steps cannot suffice, so the optimum is exactly 1.

If `s` is not a palindrome, one step is impossible: the only way to empty the string in one removal is to choose every character, but that complete subsequence is not palindromic. Two steps always suffice because the alphabet contains only two letters. Select every `a` in their existing order; a sequence made from one repeated letter is a palindrome. Then do the same for every `b`. Empty selections may simply be omitted, and a non-palindrome over this alphabet necessarily contains both letters. Therefore every non-palindromic input has optimum 2.

Use two pointers from the ends to determine which of these cases applies. Return 2 at the first mismatch; if the pointers cross without one, return 1.

#### Complexity detail

At most $\lfloor n/2\rfloor$ mirrored pairs are compared, so the running time is $O(n)$. The two indices require $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Reverse-and-compare:** Comparing `s` with `s[::-1]` is equally direct and takes $O(n)$ time, but materializes a reversed string and therefore uses $O(n)$ auxiliary space in Python.
- **Longest palindromic subsequence dynamic programming:** Checking whether its length is $n$ also distinguishes the two answers, but spends $O(n^2)$ time and $O(n)$ or $O(n^2)$ space on information the binary-alphabet argument makes unnecessary.
- **Single character:** It is already a palindrome, so the answer is 1.
- **Only one letter:** Any number of identical characters forms a palindrome and can be removed together.
- **Subsequence versus substring:** The two-step upper bound depends on selecting all occurrences of one letter even when they are separated.

</details>
