# Remove Zero Sum Consecutive Nodes from Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1171 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-zero-sum-consecutive-nodes-from-linked-list](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/).

### Goal
Given the head of a linked list, repeatedly remove any consecutive block of nodes whose values sum to `0`. Return the head after no such removable block remains.

### Function Contract
**Inputs**

- `head`: Head of a singly linked list.

**Return value**

Head of the modified linked list.

### Examples
**Example 1**

- Input: `head = [1,2,-3,3,1]`
- Output: `[3,1]`

**Example 2**

- Input: `head = [1,2,3,-3,4]`
- Output: `[1,2,4]`

**Example 3**

- Input: `head = [1,2,3,-3,-2]`
- Output: `[1]`

---

## Solution
### Approach
Use prefix sums with a dummy node before the head. If two positions have the same prefix sum, the nodes between them sum to zero.

First walk the list and store the last node seen for each prefix sum. Then walk again from the dummy node, recomputing prefix sums and jumping `node.next` to the node after the last occurrence of the same prefix. This removes the longest zero-sum ranges and handles cascaded removals naturally.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
