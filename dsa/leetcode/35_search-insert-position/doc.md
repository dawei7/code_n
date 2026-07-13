# Search Insert Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 35 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-insert-position/) |

## Problem Description
### Goal
You are given a sorted array of distinct integers and a target value. If the target already appears, return its zero-based index. Otherwise identify the position where inserting it would preserve the array's sorted order.

Equivalently, return the first index whose current value is at least `target`; if every value is smaller, return `len(nums)`. Insertion before the first element and after the last are both valid outcomes. The required logarithmic running time calls for exploiting the sorted order rather than scanning from one end.

### Function Contract
**Inputs**

- `nums`: strictly increasing `List[int]`
- `target`: `int`

**Return value**

The first index whose value is at least target, or `len(nums)` when all values are smaller.

### Examples
**Example 1**

- Input: `nums = [1, 3, 5, 6], target = 5`
- Output: `2`

**Example 2**

- Input: `nums = [1, 3, 5, 6], target = 2`
- Output: `1`

**Example 3**

- Input: `nums = [1, 3, 5, 6], target = 7`
- Output: `4`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search directly for the lower-bound insertion point**

Initialize the half-open unknown interval `[left, right)` as `[0, len(nums))`. When `nums[mid] < target`, every index through the midpoint is too small, so set `left = mid + 1`. Otherwise the midpoint is a possible insertion position, but an earlier position might also work, so retain it by setting `right = mid`.

Stop when the interval is empty. The shared boundary is the lower-bound insertion position.

**The boundaries partition proven-small and viable positions**

Every index before `left` contains a value below target, and every index at or after `right` contains a value at least target or lies just beyond the array. Each midpoint comparison preserves these partitions while halving the unknown interval.

**Trace an insertion between two values**

For `[1, 3, 5, 6]` and target 2, midpoint value 5 is not smaller, moving right to index 2. Midpoint value 3 again moves right to 1. Value 1 is smaller, moving left to 1. The boundaries meet at insertion index 1.

**One boundary serves search and insertion**

Throughout lower-bound search, every discarded index left of `left` holds a value smaller than target, while every discarded index at or right of `right` holds a value not smaller. When the half-open interval becomes empty, the shared boundary is therefore the first position whose value can be at least target.

If that position contains target, it is the target's index. Otherwise all earlier values are smaller and all later values are no smaller, so inserting at the boundary is the unique placement that preserves sorted order.

#### Complexity detail

The unknown half-open interval is at least halved on every iteration, giving $O(\log n)$ time. Only `left`, `right`, and `mid` are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Linear scan:** finds the boundary directly but requires $O(n)$ time.
- **Closed-interval binary search plus saved answer:** also works, but the half-open lower-bound form returns the insertion boundary naturally.
- **Insert and search afterward:** mutates the input and incurs linear array shifting.
- Targets below the first value converge to index `0`; targets above the last value converge to the valid boundary `len(nums)`.
- Although the given array is strictly increasing, the same lower-bound algorithm returns the first valid insertion position in a nondecreasing array with duplicates.

</details>
