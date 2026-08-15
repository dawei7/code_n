# Make String Anti-palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3088 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Greedy, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [make-string-anti-palindrome](https://leetcode.com/problems/make-string-anti-palindrome/) |

## Problem Description

### Goal

An even-length string `s` of length $n$ is an anti-palindrome when every character differs from the character at its mirrored position: for every $0 \le i<n$,

$$
s_i \ne s_{n-i-1}.
$$

You may repeatedly choose any two positions and swap their characters, including making no swaps. Thus the result may be any rearrangement of the original multiset of lowercase English letters.

Return the lexicographically smallest rearrangement that is an anti-palindrome. If no rearrangement can satisfy every mirrored pair, return `"-1"`.

### Function Contract

**Inputs**

- `s`: An even-length string of lowercase English letters, where $2 \le \lvert s\rvert \le 10^5$.

**Return value**

- The lexicographically smallest anti-palindromic rearrangement of `s`, or `"-1"` when none exists.

### Examples

#### Example 1

- **Input:** `s = "abca"`
- **Output:** `"aabc"`
- **Explanation:** The mirrored pairs are `a` with `c` and `a` with `b`, and no valid rearrangement is lexicographically smaller.

#### Example 2

- **Input:** `s = "abba"`
- **Output:** `"aabb"`
- **Explanation:** Both `a` characters occupy the first half and both `b` characters the second, so each mirror pair differs.

#### Example 3

- **Input:** `s = "cccd"`
- **Output:** `"-1"`
- **Explanation:** Three copies of `c` cannot be distributed among two mirrored pairs without placing `c` at both ends of at least one pair.
