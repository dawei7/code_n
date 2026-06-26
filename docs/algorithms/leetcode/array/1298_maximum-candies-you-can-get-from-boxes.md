# Maximum Candies You Can Get from Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1298 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Graph Theory |
| Official Link | [maximum-candies-you-can-get-from-boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/) |

## Problem Description & Examples
### Goal
Starting with some boxes, collect the maximum candies possible. A box can be opened if it is already open or if you have found its key. Opened boxes may contain candies, keys, and more boxes.

### Function Contract
**Inputs**

- `status`: `status[i]` is `1` if box `i` is open initially, else `0`.
- `candies`: candies inside each box.
- `keys`: `keys[i]` lists keys found inside box `i`.
- `containedBoxes`: `containedBoxes[i]` lists boxes found inside box `i`.
- `initialBoxes`: boxes available at the start.

**Return value**

The maximum candies collectable.

### Examples
**Example 1**

- Input: `status = [1,0,1,0]`, `candies = [7,5,4,100]`, `keys = [[],[],[1],[]]`, `containedBoxes = [[1,2],[3],[],[]]`, `initialBoxes = [0]`
- Output: `16`

**Example 2**

- Input: `status = [1,0,0,0,0,0]`, `candies = [1,1,1,1,1,1]`, `keys = [[1,2,3,4,5],[],[],[],[],[]]`, `containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]`, `initialBoxes = [0]`
- Output: `6`

**Example 3**

- Input: `status = [1,1,1]`, `candies = [10,20,30]`, `keys = [[],[],[]]`, `containedBoxes = [[],[],[]]`, `initialBoxes = [1]`
- Output: `20`

---

## Underlying Base Algorithm(s)
Graph traversal with gated nodes.

---

## Complexity Analysis
- **Time Complexity**: `O(n + total_keys + total_contained_boxes)`
- **Space Complexity**: `O(n)`
