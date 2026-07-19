# Linked List Random Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 382 |
| Difficulty | Medium |
| Topics | Linked List, Math, Reservoir Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/linked-list-random-node/) |

## Problem Description
### Goal
Initialize a selector from the head of a nonempty singly linked list whose total length need not be supplied separately. Each `getRandom()` call must choose one node position from the complete list with equal probability.

Return the selected node's stored value. Nodes with equal values remain separate equally likely positions, so their shared value may appear with correspondingly greater probability. Successive calls perform new random selections and must not consume or rearrange the list. Support the intended constant-extra-space reservoir behavior when the list size is not pre-indexed; the app adapter performs the requested number of draws.

### Function Contract
**Inputs**

- `head`: the head of a nonempty singly linked list
- `draws`: for the app adapter, the number of successive random selections to perform

**Return value**

- The app adapter returns a list containing `draws` selected values. Native LeetCode calls `getRandom()` once per requested selection.

### Examples
**Example 1**

- Input: `head = [1,2,3], draws = 4`
- Output: one valid result is `[2,1,3,2]`

**Example 2**

- Input: `head = [7], draws = 3`
- Output: `[7,7,7]`

**Example 3**

- Input: `head = [-2,5,-2], draws = 2`
- Output: one valid result is `[-2,5]`
