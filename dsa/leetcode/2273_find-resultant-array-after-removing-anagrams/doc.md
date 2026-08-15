# Find Resultant Array After Removing Anagrams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2273 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) |

## Problem Description

### Goal

You are given a 0-indexed array `words` whose elements contain only lowercase
English letters. Two words are anagrams when one can be rearranged into the
other using every original letter exactly once, including the same
multiplicity of each letter.

An operation may choose an index $i$ with $0 < i < \lvert\texttt{words}\rvert$
when `words[i - 1]` and `words[i]` are anagrams, then delete `words[i]`. Continue
until no adjacent pair permits another deletion. Although several indices may
be eligible at the same time, every possible order of valid operations leads
to the same final array.

Return that stable array of remaining words. The relative order of all
survivors must stay the same as in the input.

### Function Contract

**Inputs**

- `words`: a nonempty list of between 1 and 100 lowercase English words, each
  with length between 1 and 10

Let $S$ denote the total number of input characters:

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

The words remaining after all valid adjacent-anagram deletions, in their
original relative order.

### Examples

#### Example 1

- **Input:** `words = ["abba", "baba", "bbaa", "cd", "cd"]`
- **Output:** `["abba", "cd"]`

#### Example 2

- **Input:** `words = ["a", "b", "c", "d", "e"]`
- **Output:** `["a", "b", "c", "d", "e"]`

#### Example 3

- **Input:** `words = ["abc", "cba", "bac"]`
- **Output:** `["abc"]`
