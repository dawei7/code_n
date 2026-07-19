# Analyze User Website Visit Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1152 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/analyze-user-website-visit-pattern/) |

## Problem Description

### Goal

You are given three parallel arrays describing website visits. For every index `i`, `username[i]` identifies the user, `website[i]` is the site that user visited, and `timestamp[i]` is the time of that visit. Every recorded `(username[i], timestamp[i], website[i])` tuple is unique.

A pattern is a list of three websites, and its websites are not required to be distinct. A user matches a pattern when the user visited its first, second, and third websites in that order at three different timestamps; other visits may occur between those three visits. The pattern's score is the number of distinct users who match it, so repeated ways for one user to form the same pattern still contribute only one to the score.

Return the pattern with the highest score. If several patterns have the same maximum score, return the lexicographically smallest one. The input guarantees that at least one user has made three or more visits, so a valid pattern always exists.

### Function Contract

**Inputs**

- `username`: An array of $m$ lowercase user names, one for each visit.
- `timestamp`: An array of $m$ distinct visit-record timestamps, with each value between $1$ and $10^9$.
- `website`: An array of $m$ lowercase website names aligned with the other two arrays.

The three arrays have the same length, where $3 \le m \le 50$. For each user $u$, let $\ell_u$ be that user's number of visits after chronological ordering, and define the total number of generated three-visit combinations as

$$
C = \sum_u \binom{\ell_u}{3}.
$$

**Return value**

- A list of three website names representing the maximum-score pattern, with lexicographic order breaking ties.

### Examples

**Example 1**

- Input: `username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]`, `timestamp = [1,2,3,4,5,6,7,8,9,10]`, `website = ["home","about","career","home","cart","maps","home","home","about","career"]`
- Output: `["home", "about", "career"]`

**Example 2**

- Input: `username = ["ua","ua","ua","ub","ub","ub"]`, `timestamp = [1,2,3,4,5,6]`, `website = ["a","b","a","a","b","c"]`
- Output: `["a", "b", "a"]`

**Example 3**

- Input: `username = ["u","u","u"]`, `timestamp = [3,1,2]`, `website = ["c","a","b"]`
- Output: `["a", "b", "c"]`
