# Find K-th Smallest Pair Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 719 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) |

## Problem Description
### Goal
The distance between integers `a` and `b` is their absolute difference. Given an integer array `nums`, form the distance `abs(nums[i] - nums[j])` for every distinct index pair satisfying `0 <= i < j < len(nums)`.

Sort this multiset of pair distances and return its `k`th smallest value, where `k` is one-based. Different index pairs count separately even when they contain equal values or produce the same distance, so duplicate distances occupy separate ranks.

### Function Contract
**Inputs**

- `nums`: an integer array containing at least two values
- `k`: a one-based rank between `1` and the number of distinct index pairs

**Return value**

- The pair distance occupying rank `k` after all `abs(nums[i] - nums[j])` values for $i < j$ are sorted

### Examples
**Example 1**

- Input: `nums = [1,3,1], k = 1`
- Output: `0`

**Example 2**

- Input: `nums = [1,1,1], k = 2`
- Output: `0`

**Example 3**

- Input: `nums = [1,6,1], k = 3`
- Output: `5`

### Required Complexity

- **Time:** $O(n \log n + n \log W)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Search the distance domain instead of materializing pairs**

After sorting the values, every distance lies between zero and `W = maximum - minimum`. Binary-search this numeric interval for the smallest distance threshold that contains at least `k` pairs.

**Count pairs beneath one threshold**

For each right endpoint in sorted order, move a left pointer forward until `values[right] - values[left]` is at most the candidate threshold. Every index from that left pointer through `right - 1` forms a qualifying pair with `right`, contributing `right - left` pairs. The left pointer never moves backward, so one count takes linear time.

**Use the monotone rank predicate**

Increasing the threshold cannot remove a qualifying pair, so the predicate “at least `k` pair distances are at most this threshold” changes from false to true only once. If a midpoint qualifies, retain it as a possible answer by moving the upper boundary down; otherwise move the lower boundary above it.

**Why the lower boundary is the requested distance**

At convergence, fewer than `k` pairs have distance below the boundary, while at least `k` pairs have distance at most the boundary. Therefore the sorted multiset's `k`-th element equals that boundary. Counting index pairs rather than distinct numeric differences also preserves multiplicity from duplicates.

#### Complexity detail

Sorting takes $O(n \log n)$ time. Each of $O(\log W)$ distance checks scans the sorted array once, adding $O(n \log W)$ time. Keeping a sorted copy uses $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate and sort every distance:** it directly exposes the rank but stores $O(n^2)$ values and takes $O(n^2 \log n)$ time.
- **Heap-merge sorted distance rows:** it can be attractive when `k` is small, but its worst-case work grows with `k` and can approach quadratic.
- **Frequency counting over a small value domain:** convolution-style or prefix techniques can help when the coordinate range is tightly bounded, but their cost depends on that range rather than only on `n`.
- Duplicate values create zero-distance pairs and can make the answer zero.
- Each unordered index pair is counted exactly once when its larger sorted index is the right endpoint.
- $k = 1$ asks for the minimum distance, while the largest legal `k` asks for `maximum - minimum`.
- Large coordinate gaps affect only the logarithmic number of threshold checks.

</details>
