# Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 527 |
| Difficulty | Hard |
| Topics | Array, String, Greedy, Trie, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/word-abbreviation/) |

## Problem Description
### Goal
Given a list of distinct lowercase words, abbreviate a word by retaining a nonempty prefix and its final character while replacing the omitted middle run with that run's decimal length. Do not abbreviate when the resulting text would be no shorter than the original word.

Return one abbreviation per input position in the same order. All returned abbreviations must be unique within the list; when two words collide, lengthen their retained prefixes only as far as needed to distinguish them. For each word, use the shortest valid abbreviation under those rules, and leave a word unchanged when no shorter unique form exists.

### Function Contract
**Inputs**

- `words`: a list of distinct lowercase words

**Return value**

- The required abbreviation for each word, preserving the input order

### Examples
**Example 1**

- Input: `words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]`
- Output: `["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]`

**Example 2**

- Input: `words = ["abcdef", "abqdef"]`
- Output: `["abc2f", "abq2f"]`

**Example 3**

- Input: `words = ["localization"]`
- Output: `["l10n"]`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Identify words that can conflict**

Two generated abbreviations can match only when their original words have the same length, first character, and last character. Partition the words by that signature. Words from different groups need no comparison because at least one fixed abbreviation component differs.

**Count prefixes in a trie per group**

Insert every word into its group's trie and increment the visit count of each traversed node. A node count states exactly how many words share the prefix represented by that path. Across all groups, insertion touches each input character once.

**Stop at the first distinguishing prefix**

Traverse a word's trie path until reaching the first node with count one. That prefix distinguishes the word, while every shorter prefix reaches a node shared by at least two group members and would create the same abbreviation structure for those words. A singleton group therefore stops after its first character.

**Keep an abbreviation only when it saves characters**

For prefix length `p`, the omitted count is `len(word) - p - 1`. The abbreviated form is shorter only when at least two characters are omitted; otherwise return the original word. This rule explains why heavily conflicting short words may remain unabbreviated.

**Why the results are minimal and unique**

Within a group, each chosen trie prefix is unique, so no other word can produce the same prefix-count-final-character form. Across groups, a length or endpoint component differs. Stopping at the first unique trie node proves no shorter prefix could distinguish the word, and the final length check selects the mandated original form whenever compression would not help.

#### Complexity detail

Let `S` be the sum of all word lengths. Grouping, trie insertion, and the second traversal each process $O(S)$ characters, so time is $O(S)$. Trie nodes and the output require $O(S)$ space.

#### Alternatives and edge cases

- **Sort each signature group:** only the immediate sorted neighbors can have the maximum common prefix with a word; this uses less specialized machinery but sorting adds comparison cost.
- **Compare every pair in a group:** directly finds each required prefix but can take quadratic time in the number of mutually conflicting words.
- **Repeatedly lengthen colliding abbreviations:** is correct when conflicts are regrouped after every round, but may rebuild the same prefixes many times.
- **Words of length three or less:** cannot be shortened by this format and remain unchanged.
- **Long common prefix:** may force the original word when fewer than two middle characters would be omitted.
- **Different lengths or endpoints:** belong to different conflict groups even when their visible prefixes match.
- **Input order:** grouping may rearrange internal processing, but results must be written back at their original indices.

</details>
