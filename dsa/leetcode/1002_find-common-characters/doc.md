# Find Common Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1002 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-common-characters/) |

## Problem Description

### Goal

Given an array of lowercase strings `words`, return every character that appears in all of the strings. Character multiplicity matters: a letter occurring at least twice in every word must appear twice in the answer, while a third copy is included only if every word also contains a third copy.

The answer may be returned in any order. Each returned element is a one-character string, and the result represents the multiset intersection of the character occurrences in all input words.

### Function Contract

**Inputs**

- `words`: a list of $W$ nonempty lowercase English strings, where $1\le W\le100$ and every string has length from $1$ through $100$.

Define the total input length as

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

**Return value**

- The characters common to every word, repeated according to their minimum frequency across the words, in any order.

### Examples

**Example 1**

- Input: `words = ["bella", "label", "roller"]`
- Output: `["e", "l", "l"]`

**Example 2**

- Input: `words = ["cool", "lock", "cook"]`
- Output: `["c", "o"]`

**Example 3**

- Input: `words = ["aaa", "aa", "aaaa"]`
- Output: `["a", "a"]`
- Explanation: Every word contains at least two copies of `"a"`, but not every word contains three.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the smallest frequency seen for each letter:** Count the 26 lowercase letters in the first word. For each later word, build another 26-entry frequency array and replace every stored count with the smaller of its current value and the new word's count.

**Expand the final multiset:** After all words have been processed, the stored count for a letter is its minimum occurrence count over every word. Append that one-character string exactly that many times. Iterating letters alphabetically gives a deterministic order even though the contract accepts any order.

A character belongs to the multiset intersection exactly as many times as the least number of copies supplied by any input word. Taking componentwise minima therefore neither omits a universally available copy nor includes a copy missing from some word.

#### Complexity detail

Counting scans all $S$ input characters once. Updating 26 minima for each of $W$ words costs $O(26W)$, which is bounded by $O(S)$ because every word is nonempty. The fixed-size frequency arrays use $O(1)$ auxiliary space; the returned list is output space.

#### Alternatives and edge cases

- **Repeated list membership and removal:** Intersecting occurrence lists is intuitive, but removing from an array-backed list can shift many elements and lead to quadratic work per word.
- **Set intersection:** Sets discard duplicate occurrences and therefore fail the multiplicity requirement.
- **One input word:** Every character occurrence in that word belongs in the answer.
- **No common character:** Return an empty list.
- **High multiplicity:** Repeat a letter according to the minimum count, not its total count across all words.

</details>
