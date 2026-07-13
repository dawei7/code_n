# Minimum Cost to Connect Sticks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1167 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-connect-sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-connect-sticks/).

### Goal
Repeatedly connect two sticks into one stick whose length is their sum. Each connection costs that sum. Return the minimum possible total cost to connect all sticks into one stick.

### Function Contract
**Inputs**

- `sticks`: List of positive stick lengths.

**Return value**

Minimum total connection cost.

### Examples
**Example 1**

- Input: `sticks = [2, 4, 3]`
- Output: `14`

**Example 2**

- Input: `sticks = [1, 8, 3, 5]`
- Output: `30`

**Example 3**

- Input: `sticks = [5]`
- Output: `0`

---

## Solution
### Approach
This is the same greedy structure as Huffman merging: always connect the two shortest available sticks. Any larger early merge would carry that larger cost into later merges unnecessarily.

Use a min-heap, repeatedly pop two lengths, add their sum to the answer, and push the combined stick back.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
