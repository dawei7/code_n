# Shortest Word Distance III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 245 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-word-distance-iii/) |

## Problem Description
### Goal
Given a word list and two target strings known to have the required occurrences, find the smallest distance between positions containing the targets. Unlike the distinct-target version, `word1` and `word2` may be the same string.

Return the minimum absolute index difference between two valid, distinct occurrences. When the targets differ, pair one occurrence of each word. When they are equal, pair two separate appearances of that same word; a position cannot pair with itself and produce distance zero. The function returns only the minimum distance, not the chosen indices, and repeated occurrences anywhere in the list must be considered.

### Function Contract
**Inputs**

- `wordsDict`: a word list containing the required occurrences
- `word1`: the first target
- `word2`: the second target, possibly equal to `word1`

**Return value**

The minimum distance between valid distinct target occurrences.

### Examples
**Example 1**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "coding"`
- Output: `1`

**Example 2**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "makes"`
- Output: `3`

**Example 3**

- Input: `wordsDict = ["a","a"], word1 = "a", word2 = "a"`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Equal target words change which positions may pair**

For distinct targets, retain each latest index as in Problem 243. For equal targets, retain the previous occurrence and compare it with every new occurrence.

The stored positions are the latest valid endpoints, and the running answer is the smallest distance among pairs ending within the processed prefix.

**Consecutive compatible occurrences are sufficient**

For distinct words, the closest earlier compatible endpoint is the latest occurrence of the other word. When both targets are equal, it is the immediately preceding occurrence of that same word. Any older compatible position is farther from the current index, so checking the latest valid partner for every occurrence necessarily checks an optimal pair.

#### Complexity detail

The list is scanned once for $O(n)$ time, and only indices plus the minimum are stored.

#### Alternatives and edge cases

- **Occurrence lists:** simplify post-processing but use linear space.
- **All-pairs comparison:** is quadratic.
- Equal targets require at least two occurrences and must never pair one position with itself.

</details>
