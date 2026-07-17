# Maximum Repeating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1668 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Dynamic Programming, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-repeating-substring/) |

## Problem Description
### Goal
A string `word` is called $k$-repeating within `sequence` when the concatenation of exactly $k$ consecutive copies of `word` occurs as a substring of `sequence`. The copies must touch one another; separate occurrences elsewhere in `sequence` do not combine into a larger value.

Given the two nonempty lowercase strings, return the greatest integer $k$ for which that repeated block occurs. If even one copy of `word` is absent from `sequence`, return $0$. A repeated block may begin and end anywhere inside `sequence`; it does not need to consume the entire string.

### Function Contract
**Inputs**

- `sequence`: a nonempty string of lowercase English letters in which to search.
- `word`: a nonempty lowercase English string whose adjacent repetitions are counted.

Let $n = \lvert\texttt{sequence}\rvert$ and $m = \lvert\texttt{word}\rvert$.

**Return value**

Return the maximum nonnegative integer $k$ such that $k$ consecutive copies of `word` form a substring of `sequence`.

### Examples
**Example 1**

- Input: `sequence = "ababc", word = "ab"`
- Output: `2`
- Explanation: `"abab"` occurs in `sequence`.

**Example 2**

- Input: `sequence = "ababc", word = "ba"`
- Output: `1`
- Explanation: one copy occurs, but `"baba"` does not.

**Example 3**

- Input: `sequence = "ababc", word = "ac"`
- Output: `0`

### Required Complexity
- **Time:** $O(n + m)$
- **Space:** $O(n + m)$

<details>
<summary>Approach</summary>

#### General

**Find every occurrence in one scan.** Build the Knuth-Morris-Pratt prefix table for `word`. While scanning `sequence`, the table tells how much of a partial match remains useful after a mismatch, so characters are not repeatedly compared from scratch. Whenever the matched length reaches $m$, an occurrence of `word` ends at the current index.

**Link only adjacent occurrences.** Let `repeats[i]` be the number of consecutive copies in the repeated block ending at sequence index `i`, with zero when no occurrence ends there. If `word` ends at `i`, the preceding adjacent copy would end exactly at `i - m`. Therefore set `repeats[i]` to one plus `repeats[i - m]` when that index exists. Taking the maximum of these values gives the requested $k$.

**Overlapping matches remain available.** After recording a full KMP match, fall back through the prefix table instead of resetting the matched length to zero. This preserves legitimate overlapping occurrences. The dynamic-programming link still counts only matches separated by exactly $m$ characters, so an overlap that is not a complete adjacent copy cannot inflate the answer.

**Why the maximum is correct.** Every nonzero state corresponds to one occurrence ending at `i` plus exactly the adjacent chain ending one word-width earlier, so it describes a valid repeated substring. Conversely, every block of $k$ consecutive copies has occurrence endpoints spaced by $m$; the recurrence links those endpoints and assigns $k$ to the last one. The largest state therefore represents precisely the maximum repeating value.

#### Complexity detail

Building the prefix table costs $O(m)$ time, and KMP scans all $n$ sequence characters in $O(n)$ time. The prefix table and endpoint states use $O(m)$ and $O(n)$ space respectively, for $O(n + m)$ auxiliary space. A ring buffer could reduce the endpoint storage, but the direct array keeps the recurrence explicit.

#### Alternatives and edge cases

- **Grow and search repeated candidates:** Test `word`, then `word + word`, and so on until a candidate is absent. This is concise under the small limits but can repeat substantial substring-search work and grow quadratically.
- **Substring dynamic programming:** Compare each length-$m$ slice with `word` and link matching endpoints. It expresses the same recurrence simply, but direct slicing costs $O(m)$ per position in common languages.
- **Binary search on $k$:** Existence is monotone, but constructing and searching repeated candidates still needs an efficient string matcher and adds unnecessary machinery at these limits.
- If $m > n$, no copy can occur and the answer is $0$.
- Occurrences must be adjacent; separated matches do not combine.
- Overlapping matches count only when their endpoints are exactly $m$ positions apart.
- A one-character `word` reduces to finding the longest run of that character.
- The repeated substring may be surrounded by unrelated prefix and suffix characters.

</details>
