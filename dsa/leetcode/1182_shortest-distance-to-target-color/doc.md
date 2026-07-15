# Shortest Distance to Target Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1182 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-to-target-color/) |

## Problem Description

### Goal

An array `colors` describes a row of items, and every item has one of the three colors `1`, `2`, or `3`. You must answer a collection of independent queries about this fixed row without modifying it.

Each query is `[i, c]`: begin at index `i` and find the shortest distance to any array index whose value is the target color `c`. The distance between indices $i$ and $j$ is $\lvert i-j\rvert$, so the answer is zero when `colors[i] == c`. Return one answer per query in the original order, using `-1` if the requested color does not occur anywhere in `colors`.

### Function Contract

**Inputs**

- `colors`: A list of length $n$, where $1\le n\le 5\cdot 10^4$ and every value is `1`, `2`, or `3`.
- `queries`: A list of $q$ pairs `[i, c]`, where $1\le q\le 5\cdot 10^4$, $0\le i<n$, and `c` is `1`, `2`, or `3`.

**Return value**

- A list of $q$ integers. Entry $k$ is the minimum $\lvert i-j\rvert$ for query `queries[k] = [i, c]` over indices satisfying `colors[j] == c`, or `-1` when no such index exists.

### Examples

**Example 1**

- Input: `colors = [1,1,2,1,3,2,2,3,3]`, `queries = [[1,3],[2,2],[6,1]]`
- Output: `[3,0,3]`

For the first query, the nearest `3` to index `1` is at index `4`. The second query already points to color `2`, and the nearest `1` to index `6` is at index `3`.

**Example 2**

- Input: `colors = [1,2]`, `queries = [[0,3]]`
- Output: `[-1]`

Color `3` does not appear in the array.

### Required Complexity

- **Time:** $O(n+q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn repeated searches into nearest-distance data.** There are only three possible colors, so store three distances for every index. After this table is built, a query `[i, c]` needs only the cell for index `i` and color `c` rather than another search through `colors`.

**Find the nearest occurrence on the left.** Sweep indices from left to right while remembering the latest index of each color. At index `i`, first record `i` as the latest occurrence of `colors[i]`; for every color already seen, `i - last[color]` is its closest distance from the left. Any earlier occurrence is farther away because `last[color]` is the greatest eligible index at most `i`.

**Combine the nearest occurrence on the right.** Sweep back from right to left and analogously remember the next index of each color. For each index and color, minimize the stored left distance with `next[color] - i`. Every occurrence lies on the left or right of `i`, and each sweep selects the closest occurrence on its side, so the smaller of those two distances is the global minimum. A sentinel distance at least $n$ survives exactly when the color never occurs; convert that sentinel to `-1` when answering a query.

#### Complexity detail

Each directional sweep performs three constant-size color updates at each of the $n$ indices, and the $q$ queries take constant time apiece. The total time is therefore $O(n+q)$. The table contains three entries per array index, which is $O(n)$ space; the two three-element state arrays are $O(1)$.

#### Alternatives and edge cases

- **Sorted positions plus binary search:** Store each color's occurrence indices and binary-search around every query index. This uses $O(n)$ space and $O(n+q\log n)$ time, which is effective but not constant time per query.
- **Scan the array for every query:** Taking the minimum distance over all matching indices is direct, but it costs $O(nq)$ time in the worst case.
- **Target at the query index:** The shortest distance is `0`; both sweeps preserve that value.
- **Missing target color:** Its sentinel is never replaced, so the corresponding answer must be `-1`.
- **One-sided nearest occurrence:** At an array boundary, or when all occurrences lie on one side, the valid directional distance wins over the other sentinel.
- **Equal nearest distances:** Two target occurrences may be equally close; only their shared distance is returned, not an index.

</details>
