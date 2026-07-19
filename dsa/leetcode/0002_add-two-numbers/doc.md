# Add Two Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/add-two-numbers/) |

## Problem Description
### Goal
Two non-negative integers are stored as singly linked lists, one decimal digit per node. Their digits are stored in reverse order: each head contains the ones digit, its successor contains the tens digit, and so on. Except for the number zero itself, an input does not contain unnecessary leading zeroes at the far end of the list.

Add the represented integers and return a new linked list using the same least-significant-digit-first convention. Carries may propagate through several nodes and may create one final node beyond both inputs. Each output node must contain a single digit from `0` through `9`.

### Function Contract
**Inputs**

- `l1`: the first number's digits in least-significant-first order
- `l2`: the second number's digits in least-significant-first order

**Return value**

The sum's digits in least-significant-first order.

### Examples
**Example 1**

- Input: `l1 = [2, 4, 3], l2 = [5, 6, 4]`
- Output: `[7, 0, 8]`

**Example 2**

- Input: `l1 = [0], l2 = [0]`
- Output: `[0]`

**Example 3**

- Input: `l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]`
- Output: `[8, 9, 9, 9, 0, 0, 0, 1]`
