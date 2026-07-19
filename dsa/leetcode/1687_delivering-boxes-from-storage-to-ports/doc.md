# Delivering Boxes from Storage to Ports

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1687 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Segment Tree, Queue, Heap (Priority Queue), Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/) |

## Problem Description
### Goal

A single ship must deliver a queue of boxes from storage. Each entry `boxes[i] = [port_i, weight_i]` gives the destination and weight of the next box. The ship may load a nonempty prefix of the remaining queue, but one load may contain at most `maxBoxes` boxes and have total weight at most `maxWeight`. Consequently, every load is a consecutive segment of the original order; boxes cannot be skipped or rearranged.

For each load, the ship leaves storage and visits the loaded boxes' destination ports in order. Consecutive boxes for the port where the ship is already located require no additional movement. After unloading the batch, the ship returns to storage before loading again, and it must also end at storage after the final delivery. Return the minimum total number of movements between storage and ports or between distinct ports. `portsCount` specifies the available port identifiers but does not change a batch's travel cost by itself.

### Function Contract
**Inputs**

- `boxes`: a length-$n$ list of `[port, weight]` pairs in mandatory delivery order
- `portsCount`: the number of destination ports, numbered from 1 through this value
- `maxBoxes`: the largest number of boxes one load may contain
- `maxWeight`: the largest total weight one load may contain

**Return value**

The minimum number of location-to-location trips required to deliver every box and finish back at storage.

### Examples
**Example 1**

- Input: `boxes = [[1,1], [2,1], [1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3`
- Output: `4`

Loading all boxes visits port 1, port 2, port 1, and then storage.

**Example 2**

- Input: `boxes = [[1,2], [3,3], [3,1], [3,1], [2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6`
- Output: `6`

The optimal loads contain the first box, the middle three boxes, and the final box.

**Example 3**

- Input: `boxes = [[1,4], [1,2], [2,1], [2,1], [3,2], [3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7`
- Output: `6`

The weight limit makes three same-port batches optimal.
