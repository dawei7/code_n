# Maximum Units on a Truck

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1710 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/) |

## Problem Description
### Goal

You must load boxes onto one truck. Each entry in `boxTypes` describes how many boxes of one type are available and how many units each box of that type contains. Boxes within a type have equal value, but boxes from different types may contain different numbers of units.

The truck can carry at most `truckSize` boxes. You may choose any available boxes and do not have to fill the truck when fewer boxes exist. Return the greatest total number of units that can be loaded without exceeding the box-count capacity.

### Function Contract
**Inputs**

- `boxTypes`: a list of $t$ pairs `[numberOfBoxes, unitsPerBox]`
- `truckSize`: the maximum number of boxes the truck can hold
- $1 \le t \le 1000$
- every box count and units-per-box value is between $1$ and $1000$, and $1 \le \texttt{truckSize} \le 10^6$

**Return value**

The maximum total units obtainable by loading at most `truckSize` available boxes.

### Examples
**Example 1**

- Input: `boxTypes = [[1, 3], [2, 2], [3, 1]], truckSize = 4`
- Output: `8`

Load the one three-unit box, both two-unit boxes, and one one-unit box.

**Example 2**

- Input: `boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]], truckSize = 10`
- Output: `91`

Taking the types in descending units-per-box order fills the truck with the ten most valuable boxes.

**Example 3**

- Input: `boxTypes = [[2, 4], [3, 2]], truckSize = 3`
- Output: `10`

Both four-unit boxes and one two-unit box are optimal.
