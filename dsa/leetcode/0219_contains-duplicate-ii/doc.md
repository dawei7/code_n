# Contains Duplicate II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 219 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/) |

## Problem Description
### Goal
Given an integer array `nums` and a nonnegative distance bound `k`, look for two distinct indices `i` and `j` that store equal values. In addition to value equality, their absolute index distance must satisfy $| i - j | \le k$.

Return `True` when at least one pair meets both conditions and `False` otherwise. Duplicate values farther apart than `k` do not qualify, and an occurrence cannot pair with itself even when `k` is zero. If a value occurs several times, any sufficiently close pair is enough; the function does not return the value, indices, or smallest distance.

### Function Contract
**Inputs**

- `nums`: an integer list
- `k`: maximum allowed index distance

**Return value**

`True` when a qualifying equal-value pair exists; otherwise `False`.

### Examples
**Example 1**

- Input: `[1,2,3,1], k = 3`
- Output: `True`

**Example 2**

- Input: `[1,2,3,1,2,3], k = 2`
- Output: `False`

**Example 3**

- Input: `[1,1], k = 0`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

For each value, only its most recent occurrence matters. At index `i`, that occurrence gives the smallest distance from `i` among all earlier equal values; every still earlier occurrence is farther away.

Maintain a map from value to latest index. Before overwriting an entry, check whether `i - latest[value] <= k`. If so, the two distinct indices witness a valid pair. Otherwise update the entry to `i`, because this occurrence is the best candidate for all future positions.

For `[1,2,1,1]` with $k = 1$, the occurrence of `1` at index 2 is too far from index 0, but the map is updated. The next `1` at index 3 is only one position from index 2 and correctly qualifies. Keeping only the first occurrence would miss that pair.

Before index `i`, the map stores the greatest earlier index for each encountered value. If the current value's stored index lies within `k`, a valid equal pair exists. If it lies farther than `k`, every other earlier equal index is smaller and therefore even farther, so none can pair with `i`. Updating to `i` preserves the latest-index property. Thus every current occurrence is compared with the only earlier occurrence capable of giving its minimum distance, and the final result is exact.

#### Complexity detail

Expected $O(1)$ map work per element gives expected $O(n)$ time. The map can contain one entry for every distinct value, using $O(n)$ space.

#### Alternatives and edge cases

- A set containing only the previous `k` values uses $O(\min(n,k))$ space, but must expire the value leaving the window in the correct order.
- Comparing every index with the preceding `k` indices costs $O(nk)$.
- Storing the first occurrence rather than the latest can miss a closer later pair.
- $k = 0$ cannot satisfy two distinct indices. Adjacent duplicates qualify whenever $k \ge 1$.

</details>
