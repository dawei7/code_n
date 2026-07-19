# Before and After Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1181 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/before-and-after-puzzle/) |

## Problem Description

### Goal

A phrase contains lowercase English words separated by single spaces. A Before and After puzzle is formed from two different phrase indices when the last word of the first phrase equals the first word of the second phrase. Merge the phrases in that order, writing the shared boundary word only once.

Consider every ordered pair `(i, j)` with `i != j`; reversing a pair can therefore produce another result. Return all distinct merged phrases after removing duplicates, sorted in lexicographic order. Equal phrase text at two different indices still represents two eligible phrases.

### Function Contract

**Inputs**

- `phrases`: Between $1$ and $100$ strings, each with length from $1$ through $100$. A phrase contains only lowercase English letters and spaces, has no leading or trailing space, and has no consecutive spaces.
- Define

$$
S=\sum_{x\in\texttt{phrases}} \lvert x\rvert.
$$

- Let $R$ be the number of distinct returned phrases and let $G$ be the total character count of all compatible merged candidates constructed before deduplication.

**Return value**

- The lexicographically sorted list of distinct Before and After puzzle strings formed from different input indices.

### Examples

**Example 1**

- Input: `phrases = ["writing code","code rocks"]`
- Output: `["writing code rocks"]`

**Example 2**

- Input: `phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]`
- Output: `["a chip off the old block party","a man on a mission impossible","a man on a mission statement","a quick bite to eat my words","chocolate bar of soap"]`

**Example 3**

- Input: `phrases = ["a","b","a"]`
- Output: `["a"]`

The two `"a"` entries have different indices, so they may be paired even though their text is equal.
