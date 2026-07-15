# Last Substring in Lexicographical Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1163 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/last-substring-in-lexicographical-order/) |

## Problem Description

### Goal

You are given a string `s`. A substring is a contiguous, non-empty sequence of its characters, and substrings are compared in lexicographical order.

Consider every substring that can be taken from `s`. Return the one that appears last in lexicographical order—that is, the lexicographically largest substring. The input contains only lowercase English letters, and its length may be large enough that explicitly creating and sorting all substrings is not practical.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters with length $n$, where $1 \le n \le 4 \cdot 10^5$.

**Return value**

- The substring of `s` that is last in lexicographical order.

### Examples

**Example 1**

- Input: `s = "abab"`
- Output: `"bab"`

The distinct substrings include `"b"`, `"ba"`, and `"bab"`; `"bab"` is lexicographically largest.

**Example 2**

- Input: `s = "leetcode"`
- Output: `"tcode"`

**Example 3**

- Input: `s = "zzzz"`
- Output: `"zzzz"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce substrings to suffixes.** Fix a starting position. Among substrings beginning there, the longest one—the suffix ending at the final character—is lexicographically at least every shorter one: either an earlier mismatch already decides the comparison, or the shorter substring is a prefix of the suffix and therefore smaller. The answer is consequently the largest suffix, so only its starting index must be found.

**Compare two surviving starts.** Let `i` be the best surviving start and `j` the next competing start, with `k` counting the equal characters already seen. While `s[i + k] == s[j + k]`, advance `k`. At the first mismatch, the suffix containing the smaller character loses.

If `s[i + k] < s[j + k]`, start `i` and every position through `i + k` can be discarded: those intervening suffixes begin inside the matched region and meet the same winning continuation no later than the suffix at `j`. Set `i = max(i + k + 1, j)` and restart `j` immediately after it. If instead `s[i + k] > s[j + k]`, discard starts `j` through `j + k` by setting `j = j + k + 1`. Reset `k` after either elimination.

Each mismatch permanently removes a non-empty interval of starting positions. Thus no discarded suffix can later become the maximum, and when `j + k` reaches the end, `i` is the only maximum-suffix candidate left. Return `s[i:]`.

#### Complexity detail

The three indices move only forward, and each interval skipped after a mismatch is never reconsidered. Across the entire scan this performs $O(n)$ character comparisons. Apart from the returned slice, the algorithm stores only `i`, `j`, `k`, and $n$, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate and sort all substrings:** This creates $\Theta(n^2)$ substrings and far more copied character data, which is infeasible at the maximum input length.
- **Compare every suffix:** Keeping the largest suffix while comparing each new suffix character by character is correct but can take $O(n^2)$ time on highly repetitive strings.
- **Suffix array:** A suffix array can identify the maximum suffix, but its construction and storage are unnecessary for this single query.
- **Repeated characters:** Long equal runs are handled by `k`; the interval skip is essential to avoid quadratic rescanning.
- **Single character:** Its only non-empty substring is the entire string, so the scan returns it unchanged.
- **Returned storage:** In languages where slicing copies characters, constructing the final returned string costs $O(n)$ output space; the stated space bound describes auxiliary working storage.

</details>
