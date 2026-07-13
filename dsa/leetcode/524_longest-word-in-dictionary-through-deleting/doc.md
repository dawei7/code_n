# Longest Word in Dictionary through Deleting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 524 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) |

## Problem Description
### Goal
Given a string `s` and a dictionary of candidate words, a candidate can be formed by deleting characters from `s` only when its letters appear as a subsequence in the same relative order. Deletions may skip any positions but cannot reorder or substitute characters.

Return the longest dictionary word obtainable this way. If several qualifying words share the maximum length, return the lexicographically smallest one; if none qualifies, return `""`. The function returns the dictionary word itself rather than deleted indices, and a candidate equal to `s` is valid without any deletion.

### Function Contract
**Inputs**

- `s`: the source string
- `dictionary`: an array of candidate words

**Return value**

- The longest candidate that is a subsequence of `s`, using lexicographic order to break ties, or `""` when no candidate qualifies

### Examples
**Example 1**

- Input: `s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"]`
- Output: `"apple"`

**Example 2**

- Input: `s = "abpcplea", dictionary = ["a", "b", "c"]`
- Output: `"a"`

**Example 3**

- Input: `s = "bab", dictionary = ["ba", "ab", "a", "b"]`
- Output: `"ab"`

### Required Complexity

- **Time:** $O(|dictionary| \cdot |s|)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Test one candidate with two forward pointers**

Scan `s` from left to right while tracking the next unmatched position in a candidate. Advance the candidate pointer whenever the characters agree. The candidate is a subsequence exactly when this pointer reaches its length, because the matched indices are increasing and every retained character appears in order.

**Maintain the best answer without sorting**

For each qualifying word, replace the current answer if the word is longer. When lengths tie, replace it only if the candidate is lexicographically smaller. Starting with the empty string naturally handles the case where nothing qualifies.

**Why the update rule selects the required word**

Every dictionary entry is tested exactly once, so no eligible candidate is omitted. The maintained answer is the best qualifying word among the processed prefix: a longer candidate dominates, an equal-length smaller candidate wins the stated tie, and every other candidate is inferior. Induction over the dictionary leaves the global optimum.

**Why skipped source characters are harmless**

Characters in `s` that do not match the next required candidate character are simply passed over, which is exactly deletion. The scan never moves backward, so it cannot manufacture a reordered word.

#### Complexity detail

Each of `abs(dictionary)` candidates scans at most $| s |$ source characters, giving $O(|dictionary| \cdot |s|)$ time. The pointers and current answer reference use $O(1)$ auxiliary space, excluding the returned string.

#### Alternatives and edge cases

- **Sort candidates by length and lexicographic order:** permits returning the first subsequence match but adds $O(d \log d)$ sorting and may mutate or copy the dictionary.
- **Precompute next-character transitions:** answers each subsequence test faster after $O(|s| \cdot alphabet)$ preprocessing, useful for many long queries but requiring extra space.
- **Enumerate all subsequences of `s`:** is correct for membership lookup but takes exponential time and space.
- **No qualifying word:** return the empty string.
- **Equal-length candidates:** choose lexicographically smallest, not the earliest dictionary entry.
- **Repeated source characters:** the forward pointer selects a valid increasing occurrence sequence.
- **Candidate longer than `s`:** cannot qualify and may be rejected immediately.

</details>
