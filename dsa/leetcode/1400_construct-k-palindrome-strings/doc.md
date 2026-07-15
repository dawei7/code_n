# Construct K Palindrome Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1400 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/construct-k-palindrome-strings/) |

## Problem Description

### Goal

Given a lowercase English string `s` and an integer `k`, use every character of `s` exactly once to construct exactly `k` nonempty strings. Characters may be rearranged freely among and within the constructed strings.

Determine whether all `k` strings can be palindromes. A palindrome reads identically from left to right and right to left. The task asks only whether such a construction exists; the actual palindromes do not need to be returned.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `k`: the required number of nonempty palindrome strings, where $1 \le k \le 10^5$.

**Return value**

- `true` if all characters can be partitioned into exactly $k$ palindromes; otherwise `false`.

### Examples

**Example 1**

- Input: `s = "annabelle", k = 2`
- Output: `true`

**Example 2**

- Input: `s = "leetcode", k = 3`
- Output: `false`

**Example 3**

- Input: `s = "true", k = 4`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Count the frequency of each of the 26 letters and count how many frequencies are odd.

Every palindrome can contain at most one odd-frequency letter, placed at its center. Therefore each odd count requires a different palindrome, making `odd_count <= k` necessary. Exactly `k` nonempty strings also require `k <= n` because every palindrome needs at least one character.

These conditions are sufficient as well. Give each odd letter to the center of its own palindrome. If more centers are needed, take characters from even pairs to start additional palindromes; pairs can be split into two single-character palindromes when necessary. Distribute all remaining pairs symmetrically around any centers. Thus a construction exists exactly when `odd_count <= k <= n`.

#### Complexity detail

Counting the $n$ characters takes $O(n)$ time. The frequency table has exactly 26 slots, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Attempt explicit construction:** Building and balancing the palindrome strings is unnecessary for a boolean answer and introduces avoidable allocation and bookkeeping.
- **Repeated full-string counts:** Recomputing a character's frequency at every string position remains correct but performs $O(n^2)$ work.
- **Too many palindromes:** If $k > n$, nonempty construction is impossible even when all counts are even.
- **Many odd counts:** Each odd frequency needs its own center, so more than $k$ odd letters makes construction impossible.
- **Exactly `n` palindromes:** Always possible by using every character as a one-letter palindrome.
- **One palindrome:** Possible exactly when at most one frequency is odd.

</details>
