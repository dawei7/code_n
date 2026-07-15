# Best Sightseeing Pair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1014 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/best-sightseeing-pair/) |

## Problem Description

### Goal

You are given an integer array `values`, where `values[i]` is the value of sightseeing spot `i`. For two spots at indices `i < j`, their distance is $j-i$.

The pair's score is the sum of both sightseeing values minus that distance, written as `values[i] + values[j] + i - j`. Choose two distinct spots in their array order and return the maximum possible score among all such pairs.

### Function Contract

**Inputs**

- `values`: an array of $N$ sightseeing values, where $2\le N\le5\cdot10^4$ and $1\le\texttt{values[i]}\le1000$.

**Return value**

- The maximum score over all index pairs `i < j`.

### Examples

**Example 1**

- Input: `values = [8, 1, 5, 2, 6]`
- Output: `11`
- Explanation: Indices `0` and `2` score `8 + 5 + 0 - 2 = 11`.

**Example 2**

- Input: `values = [1, 2]`
- Output: `2`
- Explanation: The only pair scores `1 + 2 + 0 - 1 = 2`.

**Example 3**

- Input: `values = [4, 7, 5, 8]`
- Output: `13`
- Explanation: Indices `1` and `3` score `7 + 8 + 1 - 3 = 13`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the two index contributions:** Rewrite the score as `(values[i] + i) + (values[j] - j)`. For a fixed right index `j`, the second term is known, so only the largest `values[i] + i` among earlier indices is needed.

**Carry the best left spot forward:** Initialize `best_left = values[0]`. For each `j` from `1` onward, combine `best_left` with `values[j] - j` to update the answer. Only after scoring pairs ending at `j`, update `best_left` with `values[j] + j`; this ordering preserves the strict requirement `i < j`.

**Why one stored value is sufficient:** Any earlier spot with a smaller `values[i] + i` can never outperform the stored spot for the current or any future right endpoint, because every candidate receives the same `values[j] - j` term. Discarding it therefore loses no optimal pair.

Every possible right endpoint is processed, and `best_left` represents the best legal left endpoint at that moment. The maximum recorded score is consequently the maximum over all valid pairs.

#### Complexity detail

The scan processes each of the $N$ sightseeing values once, giving $O(N)$ time. The best left contribution and answer use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every pair:** Directly evaluating all `i < j` choices is correct but takes $O(N^2)$ time.
- **Prefix maximum array:** Precomputing the best left contribution for every position gives $O(N)$ time but unnecessarily uses $O(N)$ space.
- **Two spots:** The single available pair is the answer.
- **Equal values:** Distance favors the closest pair, so adjacent equal maximum values are optimal among those values.
- **Large late value:** It may serve as the right endpoint now and become the best left contribution for later endpoints.

</details>
