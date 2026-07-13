# Shortest Word Distance II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 244 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-word-distance-ii/) |

## Problem Description
### Goal
Construct a `WordDistance` service for a fixed list of words that may contain repeated entries. After construction, multiple queries provide two distinct words known to exist in that original list, without changing the list between calls.

For each `shortest(word1, word2)` query, return the minimum absolute difference between an occurrence index of the first word and an occurrence index of the second. Process queries independently and preserve construction-time index information so repeated requests do not rescan unrelated words unnecessarily. The app adapter returns query answers in order; the native interface exposes the same behavior through persistent method calls.

### Function Contract
**Inputs**

- `wordsDict`: the fixed list of words to index
- `queries`: a list of `[word1, word2]` pairs; each pair contains distinct words present in the list

**Return value**

A list containing the minimum index distance for each query in order.

### Examples
**Example 1**

- Input: `wordsDict = ["practice","makes","perfect","coding","makes"], queries = [["coding","practice"],["makes","coding"]]`
- Output: `[3,1]`

**Example 2**

- Input: `wordsDict = ["a","b","a","c"], queries = [["a","c"],["a","b"]]`
- Output: `[1,1]`

**Example 3**

- Input: `wordsDict = ["x","y"], queries = [["x","y"]]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n + qn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Preprocess once for repeated queries**

Map each word to its increasing list of positions during one preprocessing pass.

**Merge the two sorted occurrence lists**

Use two pointers. Compare current positions, update the minimum, and advance the pointer at the smaller position because keeping it cannot improve a future distance against a larger opposing position.

Before each pointer step, every pair involving a discarded position has already been compared with its closest possible opposing position encountered so far, and the running minimum covers all such pairs.

**Advancing the smaller position cannot hide a better pair**

Suppose the current positions are $a < b$. Keeping `a` while advancing the other list can only produce positions at least as large as `b`, so every future distance from `a` is at least $b - a$. After recording that distance, `a` can be discarded safely. The symmetric argument applies when $b < a$, so the merge cannot skip the optimal cross-list pair.

#### Complexity detail

Index construction is $O(n)$. A query is linear in the two occurrence-list lengths and at most $O(n)$, so `q` queries cost $O(n+qn)$ in the worst case. All stored positions use $O(n)$ space.

#### Alternatives and edge cases

- **Rescan the entire dictionary per query:** uses no index but repeats $O(n)$ work regardless of occurrence frequency.
- **Compare all occurrence pairs:** can be quadratic per query.
- A word may appear many times; every query word is guaranteed present.

</details>
