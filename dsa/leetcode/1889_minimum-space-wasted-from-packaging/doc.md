# Minimum Space Wasted From Packaging

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1889 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-space-wasted-from-packaging](https://leetcode.com/problems/minimum-space-wasted-from-packaging/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-space-wasted-from-packaging/).

### Goal
Choose one supplier's box sizes to package every package. Each package must go into one box of at least its size. Minimize total wasted space, or report that no supplier can package all items.

### Function Contract
**Inputs**

- `packages`: package sizes.
- `boxes`: each supplier's available box sizes.

**Return value**

Return the minimum total waste modulo `1_000_000_007`, or `-1` if impossible.

### Examples
**Example 1**

- Input: `packages = [2,3,5], boxes = [[4,8],[2,8]]`
- Output: `6`

**Example 2**

- Input: `packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]`
- Output: `-1`

**Example 3**

- Input: `packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]`
- Output: `9`

---

## Solution
### Approach
Sort packages and build prefix sums. For each supplier, sort and deduplicate box sizes. If its largest box is too small, skip it. Otherwise, for each box size, binary search how many remaining packages fit and add `box_size * count - sum(package_sizes)` for that segment. Take the minimum over suppliers.

### Complexity Analysis
- **Time Complexity**: `O(p log p + total_boxes log total_boxes + total_boxes log p)`
- **Space Complexity**: `O(p)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
