# Maximum Number of Occurrences of a Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1297 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) |

## Problem Description
### Goal
Given a lowercase English string `s`, consider every substring whose length is between `minSize` and `maxSize`, inclusive. A candidate is valid only when it contains at most `maxLetters` distinct characters. Occurrences are identified by their positions in `s`, so equal substrings may overlap and each starting position contributes separately.

Among all valid substring values, return the greatest number of occurrences of one value. If no substring satisfies the distinct-character limit, return zero. The requested result is a frequency, not the substring itself.

### Function Contract
**Inputs**

- `s`: a string of length $n$ containing only lowercase English letters, where $1 \le n \le 10^5$.
- `maxLetters`: the maximum permitted number of distinct characters, where $1 \le \texttt{maxLetters} \le 26$.
- `minSize` and `maxSize`: inclusive substring-length bounds satisfying $1 \le \texttt{minSize} \le \texttt{maxSize} \le \min(26,n)$.

**Return value**

The maximum occurrence count among valid substrings, or $0$ when none is valid.

### Examples
**Example 1**

- Input: `s = "aababcaab"`, `maxLetters = 2`, `minSize = 3`, `maxSize = 4`
- Output: `2`
- Explanation: `"aab"` occurs twice and uses only two distinct letters.

**Example 2**

- Input: `s = "aaaa"`, `maxLetters = 1`, `minSize = 3`, `maxSize = 3`
- Output: `2`
- Explanation: The two occurrences of `"aaa"` overlap.

**Example 3**

- Input: `s = "abcde"`, `maxLetters = 2`, `minSize = 3`, `maxSize = 3`
- Output: `0`
- Explanation: Every length-three substring contains three distinct letters.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Why only the shortest permitted length is needed**

Suppose a valid substring of length greater than `minSize` occurs $f$ times. Its length-`minSize` prefix appears at each of those same starting positions, cannot contain more distinct characters than the longer substring, and is therefore also valid. That prefix occurs at least $f$ times. Consequently, no longer candidate can produce an answer larger than the best valid substring of the minimum length.

**Count fixed windows**

Slide one window of length `minSize` across `s`. Maintain the frequency of each letter and a distinct-letter counter as the right edge enters and the left edge leaves. Whenever the full window uses at most `maxLetters` distinct characters, increment that exact window string in a frequency map and update the maximum.

Every eligible starting position is examined once. The prefix argument proves that restricting the scan to `minSize` does not discard a potentially better answer, while the map counts overlapping occurrences naturally.

#### Complexity detail

There are $O(n)$ fixed-length windows. Updating the 26-letter frequency table is constant time, and materializing a window costs at most 26 character operations because `minSize` is bounded by 26. Thus the total time is $O(n)$. The substring-frequency map can contain $O(n)$ keys and uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every allowed length:** This is correct, but repeats work for lengths that cannot improve on their minimum-length prefixes.
- **Compare every pair of windows:** Directly recounting each candidate's occurrences can take $O(n^2)$ time.
- **No valid window:** If every minimum-length window exceeds `maxLetters`, the frequency map stays empty and the answer is $0$.
- **Overlapping occurrences:** Advancing the window by one position ensures overlaps are counted.
- **`minSize = maxSize`:** The same fixed-window scan applies without special handling.
- **Repeated single character:** With `minSize = 1`, every matching position contributes to that character's frequency.

</details>
