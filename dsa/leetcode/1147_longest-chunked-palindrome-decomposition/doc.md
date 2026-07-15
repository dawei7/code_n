# Longest Chunked Palindrome Decomposition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1147 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming, Greedy, Rolling Hash, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) |

## Problem Description

### Goal

Given a string `text`, split it into $k$ non-empty substrings $(t_1,t_2,\ldots,t_k)$. Concatenating the substrings in order must reproduce all of `text`; chunks cannot overlap, omit characters, or change their order.

The sequence of chunks must itself be palindromic: $t_i=t_{k-i+1}$ for every $1 \le i \le k$. Individual chunks do not need to be palindromes, and their lengths may differ from other, nonpaired chunks. Return the largest possible value of $k$ among all decompositions satisfying these conditions.

### Function Contract

**Inputs**

- `text`: a string of length $n$, where $1 \le n \le 1000$.
- `text` consists only of lowercase English characters.

**Return value**

The maximum number of non-empty chunks in a valid chunked palindrome decomposition.

### Examples

**Example 1**

- Input: `text = "ghiabcdefhelloadamhelloabcdefghi"`
- Output: `7`
- Explanation: One maximum decomposition is `(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)`.

**Example 2**

- Input: `text = "merchant"`
- Output: `1`
- Explanation: No proper matching outer chunks exist, so the complete string is the only chunk.

**Example 3**

- Input: `text = "antaprezatepzapreanta"`
- Output: `11`
- Explanation: It can be decomposed as `(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Take the shortest available matching outer pair.** Scan inward from both ends while building a candidate prefix from left to right and a candidate suffix from right to left. As soon as the two candidates are equal and non-overlapping, fix them as two chunks and restart on the remaining middle.

**Why the greedy boundary preserves an optimum.** Suppose a longer valid outer chunk contains the shorter matching pair chosen first. Removing the equal short prefix and suffix leaves equal remainders at the two ends of that longer pair. Those remainders can still be paired later, so selecting the earliest match never reduces the number of chunks available inside. It may instead expose more boundaries, which is exactly what maximizing $k$ requires. If no outer pair matches, the entire unresolved middle must contribute one final chunk.

**Compare candidates incrementally.** Maintain two rolling hashes for each growing candidate under different moduli. Adding the next left character extends the prefix hash, while adding the next right character with the appropriate positional power constructs the suffix in forward order. When both hash pairs agree, compare the actual characters to preserve exact equality, then count two chunks and reset the hashes. Actual comparisons across successful, disjoint chunks inspect $O(n)$ characters in total.

#### Complexity detail

The two pointers consume every character once. Rolling-hash updates take constant time, and exact checks of accepted disjoint chunk pairs inspect at most $n$ characters altogether, for $O(n)$ time. The pointers, counters, powers, and hash values use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Direct substring search:** Trying every prefix length and comparing newly sliced prefix and suffix strings is correct but can copy or inspect $O(n^2)$ characters.
- **Dynamic programming:** States for every interval can express the decomposition, but they add unnecessary quadratic time and space once the shortest-match greedy property is established.
- **Hash equality without verification:** A modular collision could incorrectly create a boundary; checking the underlying characters makes the result exact.
- **No proper outer match:** The unresolved string forms one middle chunk, so the answer is at least `1`.
- **Odd number of chunks:** One non-empty chunk remains in the center and is counted once rather than as a pair.
- **Single-character matches:** A conventional palindrome can decompose into individual characters, yielding as many chunks as its length.

</details>
