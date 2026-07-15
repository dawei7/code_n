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

### Required Complexity

- **Time:** $O(m \log m + C)$
- **Space:** $O(m + C)$

<details>
<summary>Approach</summary>

#### General

**Reconstruct each user's chronology.** The input rows may mix users and need not already be ordered. Sorting the combined records by timestamp places every visit in global chronological order. Appending each sorted website to its user's history then produces exactly the order needed for subsequence patterns. Because every matching pattern uses three different timestamps, choosing three increasing positions in one history captures every legal visit triple, including triples whose website names repeat.

**Count users instead of occurrences.** A user with a long history can form the same website tuple from several different triples of positions. Generating `combinations(sites, 3)` and converting that user's results to a set removes those duplicates before the global counter is updated. Consequently, one increment means one distinct matching user, which is precisely the definition of the score. Conversely, every user who matches a pattern has at least one increasing triple that generates it, so no qualifying user is omitted.

**Apply both selection rules together.** After all histories have contributed, compare patterns by decreasing score and then by increasing tuple order. Selecting the minimum key `(-count, pattern)` therefore chooses the greatest user count first and the lexicographically smallest pattern among equal counts. Returning the winning tuple as a list gives the required result.

#### Complexity detail

Sorting the $m$ visit records costs $O(m \log m)$. A user with $\ell_u$ visits has $\binom{\ell_u}{3}$ triples, so generating all user-local patterns costs $O(C)$ in total. The histories and sorted records use $O(m)$ space, while the per-user sets and global counter can collectively contain $O(C)$ generated patterns. Thus the overall bounds are $O(m \log m + C)$ time and $O(m + C)$ space.

#### Alternatives and edge cases

- **Enumerate patterns and rescan every history:** This can calculate the same scores, but repeatedly checking every user for every candidate adds an unnecessary factor of up to $m$.
- **Count every generated triple directly:** This incorrectly lets one user increase a pattern's score multiple times when repeated visits produce the same tuple through different position choices.
- **Assume the input is already chronological:** Parallel log arrays may arrive out of timestamp order, so combinations must be formed only after sorting.
- **Repeated website names:** A pattern such as `["x", "x", "y"]` is valid, but its two `"x"` entries must correspond to two different visits at increasing timestamps.
- **Nonconsecutive visits:** Unrelated visits between the three selected websites do not prevent a match; the pattern is a subsequence, not necessarily a contiguous slice.
- **Tied scores:** Tuple comparison must be applied to the full three-site pattern so the lexicographically smallest maximum-score pattern wins.

</details>
