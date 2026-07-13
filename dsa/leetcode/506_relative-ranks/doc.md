# Relative Ranks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 506 |
| Difficulty | Easy |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/relative-ranks/) |

## Problem Description
### Goal
Given the unique competition scores in array `score`, rank athletes in decreasing score order: the highest score has rank 1, the next highest rank 2, and so on. Athlete identity remains the original array index even though ranking is determined by sorted scores.

Return one label for every athlete in original input order. Use `"Gold Medal"`, `"Silver Medal"`, and `"Bronze Medal"` for ranks 1, 2, and 3 respectively; for every later rank, use its decimal string. Preserve all athletes and do not return the scores themselves or reorder the result by placement.

### Function Contract
**Inputs**

- `score`: an array of distinct positive integer scores, one per athlete

**Return value**

- A string array aligned with `score`, containing `"Gold Medal"`, `"Silver Medal"`, `"Bronze Medal"`, or the athlete's numeric rank

### Examples
**Example 1**

- Input: `score = [5, 4, 3, 2, 1]`
- Output: `["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]`

**Example 2**

- Input: `score = [10, 3, 8, 9, 4]`
- Output: `["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]`

**Example 3**

- Input: `score = [1]`
- Output: `["Gold Medal"]`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort identities rather than losing input positions**

Create the index sequence `0` through $n - 1$ and sort those indices by their corresponding scores in descending order. The sorted position is the athlete's rank, while the stored index tells where that label belongs in the returned array.

**Translate ranks into the required labels**

Enumerate the sorted indices starting at rank one. Map ranks one, two, and three to the three medal strings; for every later rank, use `str(rank)`. Write each label directly into a preallocated result at the athlete's original index.

**Why every label is correct**

Scores are distinct, so descending sort establishes one unambiguous order. Exactly `rank - 1` sorted athletes precede the athlete assigned that rank, and all of them have greater scores. Thus the numeric position and medal mapping match the definition, while writing by original index restores the requested output alignment.

#### Complexity detail

Sorting `n` indices takes $O(n \log n)$ time, and assigning labels takes $O(n)$ additional time. The index order and result array use $O(n)$ space.

#### Alternatives and edge cases

- **Sort score-index pairs:** has the same bounds and keeps the association explicit, at the cost of constructing tuples.
- **Max-heap:** repeatedly extracts the next highest score in $O(n \log n)$ total time and needs the original index in each heap entry.
- **Count greater scores for every athlete:** is correct but performs $O(n^2)$ comparisons.
- **Single athlete:** receives `"Gold Medal"` even though the other medal positions do not exist.
- **Two athletes:** receive gold and silver only.
- **Large score gaps:** do not affect ranks; only relative order matters.
- **Original order:** must determine output positions, not the descending rank order.

</details>
