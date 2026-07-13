# Kth Largest Element in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 215 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Problem Description
### Goal
Given a nonempty integer array and a valid one-based rank `k`, identify the element that would occupy position `k` if all array occurrences were arranged from largest to smallest. The rank is based on positions in that ordering, not on distinct values.

Return the value at that rank. Duplicate occurrences therefore occupy separate positions and can cause the same value to represent several ranks. For example, $k = 1$ requests a maximum, while `k` equal to the array length requests a minimum. The function returns only the element value and need not return a sorted array or its original index.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list
- `k`: a one-based rank from the largest end

**Return value**

The value at that rank.

### Examples
**Example 1**

- Input: `[3,2,1,5,6,4], k = 2`
- Output: `5`

**Example 2**

- Input: `[3,2,3,1,2,4,5,5,6], k = 4`
- Output: `4`

**Example 3**

- Input: `[7], k = 1`
- Output: `7`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Convert the requested descending rank to the ascending target index $n - k$. Quickselect can place that index without sorting every other value.

Within an active range, choose a pivot and apply a Dutch-national-flag partition:

- values smaller than the pivot occupy the left region,
- values equal to it occupy one contiguous middle region,
- values greater than it occupy the right region.

After partitioning, every index in the middle region has its final rank value even though the outer regions are internally unsorted. If the target index lies there, return the pivot. Otherwise continue only in the side containing the target.

The three-way partition is particularly important for duplicates. In `[3,2,3,1,2,4,5,5,6]`, a pivot value appearing several times is resolved as one block; the search never repeatedly partitions those equal values. Duplicate occurrences still count as separate ranks because the middle block spans one index per occurrence.

The reference implementation chooses a pivot from the active range and mutates `nums`. If preserving the input is required, a copy is necessary and changes the auxiliary-space bound.

Partitioning establishes that every left-region value is below every pivot-equal value and every right-region value is above it. Thus the equal block occupies exactly the pivot's final rank interval. If the target lies inside, the pivot is the required value. If it lies outside, all values in the discarded regions have final ranks on the wrong side, so restricting the active range preserves the target. Repeating eventually places the target in an equal block and returns the kth-largest value.

#### Complexity detail

With balanced or randomized pivots, the active range shrinks geometrically in expectation and total partition work is expected $O(n)$. A consistently poor deterministic pivot can degrade to $O(n^2)$ worst-case; randomization or median-of-medians addresses adversarial inputs, with median-of-medians guaranteeing linear worst-case time at greater constant complexity. Partitioning is in place and uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- Full sorting takes $O(n \log n)$ time but is simple and deterministic.
- A min-heap of size `k` takes $O(n \log k)$ time and $O(k)$ space and is useful for streaming input.
- Median-of-medians guarantees $O(n)$ worst-case selection but is substantially more complex.
- Ranking only distinct values is incorrect because duplicates count separately.
- All-equal arrays terminate through the middle block; negative values and $k = 1$ or $k = n$ need no special handling.

</details>
