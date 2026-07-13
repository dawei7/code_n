# Minimum Number of People to Teach

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1733 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-people-to-teach](https://leetcode.com/problems/minimum-number-of-people-to-teach/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-people-to-teach/).

### Goal
People know different languages, and some friendship pairs need to communicate. Teach one chosen language to the fewest people so every friendship pair has at least one common language.

### Function Contract
**Inputs**

- `n`: the number of available languages.
- `languages`: `languages[i]` lists the languages person `i + 1` knows.
- `friendships`: pairs of people who should be able to communicate.

**Return value**

Return the minimum number of people who must be taught one language.

### Examples
**Example 1**

- Input: `n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]`
- Output: `1`

**Example 2**

- Input: `n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]`
- Output: `2`

**Example 3**

- Input: `n = 3, languages = [[1,2],[2,3],[1,3]], friendships = [[1,2],[2,3]]`
- Output: `0`

---

## Solution
### Approach
First identify the people in friendship pairs that currently share no language; only those people matter. For every candidate language, count how many of those affected people do not already know it. The minimum count is the answer.

### Complexity Analysis
- **Time Complexity**: `O(F * L + n * P)`, where `P` is affected people
- **Space Complexity**: `O(P + total known languages)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
