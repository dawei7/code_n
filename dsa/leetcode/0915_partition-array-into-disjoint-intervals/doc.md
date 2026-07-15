# Partition Array into Disjoint Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 915 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) |

## Problem Description
### Goal

Given an integer array `nums`, divide it at one boundary into two contiguous subarrays named `left` and `right`. Both subarrays must be non-empty, and every element in `left` must be less than or equal to every element in `right`.

Among all boundaries satisfying that ordering condition, choose the one that gives `left` the smallest possible size. Return the length of `left`. The input is guaranteed to admit at least one valid partition.

### Function Contract
**Inputs**

- `nums`: an array of $n$ integers, where $2 \le n \le 10^5$ and $0 \le \textit{nums}[i] \le 10^6$.

**Return value**

The smallest index count $k$, with $1 \le k<n$, such that every value in `nums[:k]` is less than or equal to every value in `nums[k:]`.

### Examples
**Example 1**

- Input: `nums = [5,0,3,8,6]`
- Output: `3`
- Explanation: `left = [5,0,3]` and `right = [8,6]`.

**Example 2**

- Input: `nums = [1,1,1,0,6,12]`
- Output: `4`
- Explanation: The zero forces the first four values into `left`.

**Example 3**

- Input: `nums = [1,2]`
- Output: `1`
- Explanation: The first element alone already satisfies the condition.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the requirement imposed by the current left side**

Start with the first value in `left`. Maintain `left_max`, the maximum of every value that the current boundary has committed to `left`, and `seen_max`, the maximum value encountered anywhere in the scan so far. Also store the last index currently belonging to `left`.

When the next value is at least `left_max`, it is compatible with the present boundary: it could remain in `right` without violating the requirement that every left value be no greater. Continue scanning because a later smaller value may still invalidate that boundary.

**Repair an invalid boundary without losing earlier maxima**

If `nums[i] < left_max`, the current element cannot belong to `right`. Any valid partition must move its boundary through index `i`, so update the last left index to `i`. The enlarged left side contains every value seen so far, making its new maximum the previous `seen_max`.

This update is forced, which establishes minimality: the algorithm extends `left` only when the current value proves every earlier boundary invalid. Once the scan ends, no later value is below the final `left_max`, so that boundary is valid; because every extension was necessary, it is also the smallest valid one.

#### Complexity detail

Let $n$ be the length of `nums`. The scan examines each value once and performs constant work per value, for $O(n)$ time. The two maxima and one boundary index use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix maxima and suffix minima:** Precomputing both arrays makes each boundary test direct and still takes $O(n)$ time, but it uses $O(n)$ additional space.
- **Test each split independently:** Computing `max(nums[:k])` and `min(nums[k:])` for every $k$ is straightforward but takes $O(n^2)$ time in the worst case.
- **Equality across the boundary:** The requirement is less than or equal, so values equal to `left_max` do not force the boundary to move.
- **Boundary at one:** If the first value is no greater than every later value, the minimum answer is $1$.
- **Boundary at $n-1$:** The guarantee allows the only valid partition to leave a single element in `right`.
- **Repeated low values:** Every value below the committed `left_max` must be absorbed into `left`, even when a previous low value already moved the boundary.

</details>
