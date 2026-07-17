# Largest Subarray Length K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1708 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-subarray-length-k/) |

## Problem Description
### Goal

You are given an integer array `nums` whose values are all distinct and a positive integer `k`. Consider every contiguous subarray containing exactly `k` elements. Compare two such arrays lexicographically: at the first position where their values differ, the one with the greater value is larger.

Return the lexicographically largest length-`k` subarray. The result must preserve the original contiguous order; elements cannot be rearranged or selected with gaps. Since all input values are distinct, the best subarray is unique.

### Function Contract
**Inputs**

- `nums`: a list of $n$ distinct integers
- `k`: the required subarray length, with $1 \le k \le n$
- $1 \le n \le 10^5$, and every value in `nums` lies between $1$ and $10^9$

**Return value**

A new list containing the lexicographically largest contiguous subarray of `nums` with exactly `k` elements.

### Examples
**Example 1**

- Input: `nums = [1, 4, 5, 2, 3], k = 3`
- Output: `[5, 2, 3]`

The eligible starting values are `1`, `4`, and `5`. The window beginning with `5` is lexicographically largest.

**Example 2**

- Input: `nums = [1, 4, 5, 2, 3], k = 4`
- Output: `[4, 5, 2, 3]`

Only indices `0` and `1` can start a four-element window, and `4` is the larger of those first values.

**Example 3**

- Input: `nums = [1, 4, 5, 2, 3], k = 1`
- Output: `[5]`

For one-element subarrays, lexicographic order is simply the order of their only values.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Restrict attention to legal starting positions**

A length-`k` subarray beginning at index `i` ends at `i + k - 1`, so its start must satisfy $0 \le i \le n-k$. Values after index `n-k` can occur inside a candidate but cannot begin one. Scan exactly this legal prefix of starting positions.

**Use the first differing value**

Every pair of candidates has different first elements because all values in `nums` are distinct. Their lexicographic comparison is therefore decided immediately at position zero; no later element can overturn it. The candidate whose starting value is greatest is the unique largest candidate.

Track the index of the greatest value among `nums[0]` through `nums[n-k]`. Once the scan finishes, return the `k` consecutive elements starting at that index. The scan considers every legal candidate, and the distinctness guarantee proves that the chosen starting value beats every other candidate at their first comparison position.

#### Complexity detail

Scanning the $n-k+1$ legal starting positions and copying the $k$ result elements takes $O(n-k+1+k)=O(n)$ time. Apart from the returned length-$k$ list, the scan stores only one index, so total space is $O(k)$ and auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Materialize and compare every window:** generating all slices and taking their maximum is direct, but copying $k$ elements for each of $n-k+1$ windows costs $O((n-k+1)k)$ time and space across the generated candidates.
- **Sort candidate starts:** sorting the legal indices by their first values finds the same start in $O(n\log n)$ time, although only one maximum is needed.
- **Compare candidates element by element:** this is unnecessary under the distinct-values guarantee because candidates always differ at their first element.
- **Entire array:** when `k == n`, index `0` is the only legal start and the whole array is returned.
- **Single element:** when `k == 1`, choose the maximum value as a one-element result.
- **Late maximum:** the largest value in the entire array may lie after index `n-k` and therefore cannot start a valid window.
- **Value magnitudes:** only relative order matters; the greedy argument does not depend on the gaps between values.
- **Contiguity:** return a slice of the original order rather than the globally largest `k` values.

</details>
