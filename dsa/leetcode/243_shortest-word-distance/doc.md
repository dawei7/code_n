# Shortest Word Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 243 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-word-distance/) |

## Problem Description
### Goal
Given a list of words and two distinct target strings known to occur in it, choose one occurrence of `word1` and one occurrence of `word2`. Their distance is the absolute difference between their zero-based positions in the list.

Return the minimum distance over all valid pairs of target occurrences. Each word may appear several times, so an early pair is not necessarily closest and every relevant occurrence can affect the answer. Because the target strings are distinct, one position cannot represent both targets. Return only the positive distance, not the indices or the words themselves.

### Function Contract
**Inputs**

- `wordsDict`: a list of words containing both targets
- `word1`: the first target word
- `word2`: the distinct second target word

**Return value**

The minimum absolute difference between an index containing `word1` and an index containing `word2`.

### Examples
**Example 1**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "coding", word2 = "practice"`
- Output: `3`

**Example 2**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "coding"`
- Output: `1`

**Example 3**

- Input: `wordsDict = ["a","b"], word1 = "a", word2 = "b"`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A new occurrence needs only the latest opposite occurrence**

Scan once, updating the most recent index of each target. Whenever both are known, their distance is the best distance ending at the newly seen target occurrence.

After index `i`, the two stored positions are the latest occurrences at or before `i`, and the answer is the minimum distance among every target pair whose later endpoint is at most `i`.

**Every optimal pair is considered at its later endpoint**

Fix a target occurrence as the later endpoint of a pair. Among all earlier occurrences of the other word, the most recent one has the greatest index and therefore the smallest distance. The scan checks precisely that occurrence. Repeating this for every possible later endpoint considers the best pair ending there, and the smallest of those candidates is the global optimum.

#### Complexity detail

One scan takes $O(n)$ time, while two indices and the current minimum use constant space.

#### Alternatives and edge cases

- **Store all occurrence indices:** works but uses $O(n)$ space.
- **Compare every pair:** can take $O(n^2)$.
- Adjacent targets yield one; repeated target occurrences continually tighten the candidate distance.

</details>
