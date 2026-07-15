# The k-th Lexicographical String of All Happy Strings of Length n

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1415 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) |

## Problem Description

### Goal

A happy string contains only the characters `a`, `b`, and `c`, and no two adjacent characters are equal. Consider every happy string whose length is exactly `n`, sorted in lexicographical order.

Return the `k`-th string in that one-indexed ordering. If fewer than `k` happy strings of length `n` exist, return the empty string. The result must be selected from the ordering itself rather than from strings of shorter lengths.

### Function Contract

**Inputs**

- `n`: the required string length, where $1 \le n \le 10$.
- `k`: the one-indexed requested rank, where $1 \le k \le 100$.

**Return value**

- The `k`-th lexicographically smallest happy string of length `n`, or `""` when that rank does not exist.

### Examples

**Example 1**

- Input: `n = 1, k = 3`
- Output: `"c"`

**Example 2**

- Input: `n = 1, k = 4`
- Output: `""`

**Example 3**

- Input: `n = 3, k = 9`
- Output: `"cab"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count the strings under a prefix.** There are three choices for the first character and two choices at every later position, so the total number is $3 \cdot 2^{n-1}$. If `k` exceeds this value, the requested string does not exist.

After a prefix has chosen its last character, each allowable next character begins a lexicographically contiguous block. If $r$ positions remain after that choice, every block contains exactly $2^r$ completions, because each later position has two choices different from its predecessor.

**Unrank one block at a time.** At each position, list the allowable characters in `a`, `b`, `c` order. The zero-based block containing rank `k` is `(k - 1) // block_size`. Append that block's character, subtract the number of strings in all earlier blocks from `k`, and continue.

Every valid completion belongs to exactly one next-character block, and the blocks occur in the same order as their first differing character. Selecting the block containing the current rank therefore preserves the requested global ordering. Once all positions are fixed, the sole remaining completion is exactly the original `k`-th string.

#### Complexity detail

The algorithm makes at most three constant-time character checks at each of the $n$ positions, for $O(n)$ time. The constructed answer and its short choice lists use $O(n)$ space in total.

#### Alternatives and edge cases

- **Backtracking enumeration:** Generate happy strings in lexical order and stop at the `k`-th. It is simple but spends $O(kn)$ time constructing earlier strings.
- **Generate and sort all strings:** This performs unnecessary exponential generation and sorting.
- **Length one:** The only results are `"a"`, `"b"`, and `"c"`.
- **Rank out of range:** Compare with $3 \cdot 2^{n-1}$ before indexing a block.
- **One-indexed rank:** Subtract one before integer division to avoid selecting the following block at an exact boundary.
- **Adjacent characters:** Remove the previously chosen character before determining the next block order.

</details>
