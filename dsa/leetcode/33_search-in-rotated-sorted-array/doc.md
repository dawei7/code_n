# Search in Rotated Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 33 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) |

## Problem Description
### Goal
You are given an integer array `nums` sorted in ascending order with distinct values. Before being provided, it may have been rotated at an unknown pivot, moving one leading segment behind the other while preserving the sorted order within both segments.

Find `target` and return its current zero-based index, or return `-1` when it is absent. The array may be unrotated, rotated at any valid boundary, or contain one element. The required logarithmic running time rules out a simple full scan.

### Function Contract
**Inputs**

- `nums`: `List[int]` containing distinct values in rotated increasing order
- `target`: `int`

**Return value**

The target's zero-based index, or `-1` when absent.

### Examples
**Example 1**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`
- Output: `4`

**Example 2**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 3`
- Output: `-1`

**Example 3**

- Input: `nums = [1], target = 0`
- Output: `-1`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Rotation leaves at least one half ordinarily sorted**

At any binary-search interval, at most one of its two halves can cross the rotation boundary. Therefore at least one half is in ordinary increasing order. With distinct values, `nums[left] <= nums[mid]` proves the left half is sorted; otherwise the right half must be sorted.

Check `nums[mid] = target` first. The remaining range comparisons can then use one strict endpoint around the midpoint without accidentally retaining or discarding the already-tested value.

**Use the sorted half's endpoints to choose the next interval**

For a sorted left half, test whether `nums[left] <= target < nums[mid]`. Keep that half when true; otherwise the target, if present, must be in the right half. For a sorted right half, use `nums[mid] < target <= nums[right]` symmetrically.

The unsorted half cannot be classified from endpoint values alone because it crosses the rotation. The algorithm never tries to do so; it makes its decision using whichever half has a normal sorted interval.

**The target-containing interval shrinks geometrically**

Before each iteration, if target exists, its index lies within `[left, right]`. The sorted-half range test proves whether target can lie in that half. Discarding the other half therefore preserves the invariant while reducing the interval by at least half.

**Trace a search across the rotation**

For `[4, 5, 6, 7, 0, 1, 2]` and target 0, midpoint value 7 makes the left half sorted, but 0 is outside its range, so keep the right half. Its midpoint is 1; the left portion `[0, 1]` contains the target range, leading directly to index 4.

**The sorted half makes one side disposable**

With distinct values, at least one half around the midpoint is sorted, and endpoint comparisons identify it unambiguously. Inside that half, the target belongs there exactly when its value lies between the sorted endpoints. If it does, the other half can be discarded; if it does not, the sorted half can be discarded.

Each decision preserves every possible target position while removing at least half the interval. Returning occurs only on an equality comparison, and exhausting the interval after these safe eliminations proves no target position exists.

#### Complexity detail

Each comparison discards at least half of the current interval, so there are $O(\log n)$ iterations. The search stores only boundary and midpoint indices, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Linear scan:** simple but violates the required logarithmic time.
- **Find the rotation point, then binary search:** also $O(\log n)$ and correct, but requires two searches rather than one combined invariant.
- **Restore sorted order by copying:** costs linear time and space and loses original indices without extra bookkeeping.
- An unrotated array is handled because its left side is repeatedly recognized as sorted. A one-element interval is checked directly at its midpoint.
- Distinct values are essential to the unambiguous half test. With duplicates, equal endpoint and midpoint values may require shrinking a boundary and can degrade worst-case time to linear.

</details>
