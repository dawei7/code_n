# Longest Common Prefix Between Adjacent Strings After Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3598 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/) |

## Problem Description
### Goal
For every index of a string array `words`, consider a separate experiment in which the word at that index is removed while all remaining words keep their relative order. Examine every pair that is adjacent in the resulting array and measure the length of that pair's longest common prefix.

Return one value per original index. The value for index `i` is the greatest adjacent-pair prefix length available after removing `words[i]`. Use `0` when fewer than two words remain or when every remaining adjacent pair differs at its first character. Each removal is independent; the original array is restored before considering the next index.

### Function Contract
**Inputs**

- `words`: the ordered array of nonempty lowercase English strings

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

The number of words is at most $10^5$, every word has length at most $10^4$, and $S \le 10^5$.

**Return value**

An integer array of the same length as `words`, where position `i` contains the maximum longest-common-prefix length among adjacent words after removing index `i`.

### Examples
**Example 1**

- Input: `words = ["jump", "run", "run", "jump", "run"]`
- Output: `[3, 0, 0, 3, 3]`

Removing the first word preserves an adjacent `"run"`, `"run"` pair with prefix length `3`. Removing either of those two originally adjacent copies separates them and leaves only zero-length common prefixes.

**Example 2**

- Input: `words = ["dog", "racer", "car"]`
- Output: `[0, 0, 0]`

No removal leaves an adjacent pair with a shared first character.

**Example 3**

- Input: `words = ["abx", "zzz", "aby"]`
- Output: `[0, 2, 0]`

Only removing the middle word makes `"abx"` and `"aby"` adjacent; their longest common prefix is `"ab"`.
