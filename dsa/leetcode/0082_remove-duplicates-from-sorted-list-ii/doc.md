# Remove Duplicates from Sorted List II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 82 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) |

## Problem Description
### Goal
You are given the head of a linked list sorted in ascending order. Duplicate values therefore occur in contiguous runs. Delete every node whose number has a duplicate in the original list.

Return the head of the list containing only the distinct numbers from the original list, still sorted in ascending order and reusing surviving nodes. A duplicate run at the head may change the returned head, and a list made entirely of repeated values becomes empty.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases; it may be empty

**Return value**

The resulting linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1,2,3,3,4,4,5]`
- Output: `[1,2,5]`

**Example 2**

- Input: `head = [1,1,1,2,3]`
- Output: `[2,3]`

**Example 3**

- Input: `head = [1,1]`
- Output: `[]`
