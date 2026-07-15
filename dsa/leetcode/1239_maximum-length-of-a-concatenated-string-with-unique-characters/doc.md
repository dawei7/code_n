# Maximum Length of a Concatenated String with Unique Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1239 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) |

## Problem Description

### Goal

You are given an array `arr` of lowercase English strings. Select a subsequence of these strings and concatenate the selected strings without changing their original order. The resulting string is valid only when every character in the entire concatenation is unique.

Return the maximum possible length of a valid concatenation. You may delete any number of array elements, including all of them, so the empty concatenation of length zero is always available. A source string that already repeats one of its own characters cannot participate in any valid result.

### Function Contract

**Inputs**

- `arr`: A list of $n$ lowercase strings, where $1\le n\le16$ and each string has length from $1$ through $26$.

Define the total number of input characters as

$$
S = \sum_{w\in\texttt{arr}} \lvert w\rvert.
$$

**Return value**

- The maximum length of a concatenation formed from a subsequence of `arr` whose characters are all unique.

### Examples

**Example 1**

- Input: `arr = ["un","iq","ue"]`
- Output: `4`

Either `"uniq"` or `"ique"` has four distinct characters.

**Example 2**

- Input: `arr = ["cha","r","act","ers"]`
- Output: `6`

Valid longest choices include `"chaers"` and `"acters"`.

**Example 3**

- Input: `arr = ["abcdefghijklmnopqrstuvwxyz"]`
- Output: `26`

The only source string already contains every lowercase letter exactly once.

### Required Complexity

- **Time:** $O(S+2^n)$
- **Space:** $O(2^n)$

<details>
<summary>Approach</summary>

#### General

**Encode character sets as bitmasks.** Map each lowercase letter to one of 26 bits. While encoding a word, discard it if a bit appears twice, because that word can never belong to a unique-character concatenation. Otherwise, its mask records exactly the characters it contributes.

**Expand every reachable valid character set.** Begin with `masks = [0]`, representing the empty subsequence. For each usable word mask, iterate over a snapshot of the masks reachable before that word. If `existing & word_mask == 0`, their character sets are disjoint, so append `existing | word_mask` as a new reachable state. Taking a snapshot ensures the same array element is not selected more than once.

Every appended mask corresponds to a valid subsequence: it extends a previously valid choice with a later disjoint word. Conversely, any valid subsequence either omits the current word and remains in the old states, or includes it after a valid subsequence of earlier words and is created by this expansion. Induction over `arr` therefore covers all valid choices. The largest `bit_count()` among reachable masks is the requested maximum length.

#### Complexity detail

Encoding all words takes $O(S)$ time. At most $2^n$ distinct subsequence states are generated, with constant-time 26-bit compatibility and population-count operations, so total time is $O(S+2^n)$. The reachable-mask collection contains at most $2^n$ integers, giving $O(2^n)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate and concatenate every subsequence:** This is correct but repeatedly rebuilds strings and rechecks characters, adding an $O(S)$ factor to the exponential search.
- **Recursive backtracking with a bitmask:** It explores the same include-or-skip state space and can be equally efficient, but the iterative expansion avoids recursion bookkeeping.
- **Memoize by index and mask:** Memoization can merge repeated states, though the fixed 26-bit mask already makes iterative deduplication straightforward.
- **Internally repeated word:** Discard it before state expansion because no surrounding choice can remove its duplicate.
- **Duplicates across words:** Two individually valid words cannot be combined when their masks intersect.
- **All words unusable:** Only the empty mask remains and the answer is `0`.
- **Full alphabet:** No valid concatenation can exceed `26`, regardless of the number of input strings.

</details>
