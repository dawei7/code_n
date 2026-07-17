# Check If Two String Arrays are Equivalent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1662 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) |

## Problem Description
### Goal
Each input is an array of nonempty lowercase string fragments. An array represents the single string formed by concatenating all of its elements in their given order from left to right; fragment boundaries do not become part of that represented string.

Determine whether `word1` and `word2` represent exactly the same character sequence, even when the two arrays divide that sequence at different positions.

### Function Contract
**Inputs**

- `word1`: between 1 and $10^3$ nonempty lowercase fragments.
- `word2`: between 1 and $10^3$ nonempty lowercase fragments.

Each represented string contains at most $10^3$ characters. Let $N$ be the total number of characters across both arrays.

**Return value**

Return `true` when the ordered concatenations are identical; otherwise return `false`.

### Examples
**Example 1**

- Input: `word1 = ["ab", "c"], word2 = ["a", "bc"]`
- Output: `true`

Both arrays represent `"abc"`.

**Example 2**

- Input: `word1 = ["a", "cb"], word2 = ["ab", "c"]`
- Output: `false`

**Example 3**

- Input: `word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]`
- Output: `true`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Ignore fragment boundaries.** Treat each array as a lazy stream that yields the characters of its first fragment, then its second, and so on. Comparing streams directly captures the represented strings without allocating either concatenation.

**Compare aligned characters and exhaustion.** Advance both streams together. Every paired character must match, and both streams must end at the same moment. A mismatch proves inequality immediately; if one stream has an extra character after the other ends, the represented lengths differ and the result is also false.

**Why streaming is sufficient.** Concatenation preserves exactly the order in which the nested iteration yields characters. Fragment boundaries contribute no data, so equal-length streams with equal characters at every position are identical strings, while any unequal position or unequal exhaustion distinguishes them.

#### Complexity detail

At most all $N$ input characters are examined once, for $O(N)$ time. Iterators and current positions use $O(1)$ auxiliary space; the output strings are never materialized.

#### Alternatives and edge cases

- **Join and compare:** `"".join(word1) == "".join(word2)` is concise and $O(N)$ time, but allocates $O(N)$ additional string storage.
- **Manual fragment pointers:** Four indices tracking each array and offset provide the same $O(N)$ time and $O(1)$ space without iterator utilities.
- **Repeated concatenation:** Rebuilding a growing string after each fragment can copy prefixes repeatedly and cost $O(N^2)$.
- Equal fragment counts are neither necessary nor sufficient.
- A mismatch may occur exactly across different fragment boundaries.
- Identical prefixes with different total lengths are not equivalent.
- Single-fragment arrays reduce to ordinary string equality.
- Every fragment is nonempty, so no special empty-fragment skipping is required by the contract.

</details>
