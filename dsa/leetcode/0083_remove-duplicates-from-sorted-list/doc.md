# Remove Duplicates from Sorted List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 83 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) |

## Problem Description
### Goal
You are given the head of a linked list sorted in ascending order. Equal values appear next to one another, possibly in runs longer than two.

Delete duplicate nodes so that exactly one node remains for each distinct value, then return the head. Keep the values in sorted order and reuse one node from every run. Unlike the variant that removes duplicated values entirely, this task always preserves a single representative. Empty and one-node lists are unchanged.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases; it may be empty

**Return value**

The resulting linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1,1,2]`
- Output: `[1,2]`

**Example 2**

- Input: `head = [1,1,2,3,3]`
- Output: `[1,2,3]`

**Example 3**

- Input: `head = []`
- Output: `[]`
