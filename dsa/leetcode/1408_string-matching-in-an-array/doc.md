# String Matching in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1408 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/string-matching-in-an-array/) |

## Problem Description

### Goal

Given an array `words` of distinct lowercase English strings, identify every array entry that occurs as a contiguous substring of a different entry in the same array.

Return all qualifying words. Each word appears at most once because the input strings are distinct, and the result may be returned in any order. A word does not qualify merely by being a substring of itself.

### Function Contract

**Inputs**

- `words`: an array of $n$ distinct lowercase strings, where $1 \le n \le 100$ and every word has length from 1 through 30.

Let $L$ be the maximum word length.

**Return value**

- The words that occur contiguously inside at least one other array word, in any order.

### Examples

**Example 1**

- Input: `words = ["mass","as","hero","superhero"]`
- Output: `["as","hero"]`

**Example 2**

- Input: `words = ["leetcode","et","code"]`
- Output: `["et","code"]`

**Example 3**

- Input: `words = ["blue","green","red"]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n^2L^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

For each candidate word, examine every other array entry. Skip the candidate's own index, and use substring search to test whether the candidate occurs contiguously in the other word. Append it as soon as one containing word is found, then stop checking that candidate so it is emitted once.

If a word is appended, the successful comparison supplies a distinct containing entry, so it satisfies the contract. Conversely, every qualifying word has at least one such other entry, and the complete pair scan eventually tests that pair. The early stop affects only duplicate discovery, not membership in the result.

#### Complexity detail

There are $O(n^2)$ ordered word pairs. Under a straightforward substring-search model, checking strings of length at most $L$ costs $O(L^2)$, giving $O(n^2L^2)$ time. The result and loop state use $O(n)$ space; language substring routines may use implementation-specific temporary storage.

#### Alternatives and edge cases

- **Aho-Corasick automaton:** Match all words against all texts together for stronger large-input behavior, but it is substantially more machinery for the small source bounds.
- **Repeat every pairwise decision:** Recomputing the entire answer once per word remains correct but adds a factor of $n$.
- **Self-match:** Skip equal indices; every string trivially contains itself.
- **Several containers:** Emit the candidate only once after its first match.
- **Equal lengths:** Since words are distinct, neither equal-length word can be a substring of the other.
- **No matches:** Return an empty list.
- **Output order:** Any order is valid, so judging must compare membership rather than one serialization.

</details>
