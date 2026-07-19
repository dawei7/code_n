# Convert Binary Number in a Linked List to Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1290 |
| Difficulty | Easy |
| Topics | Linked List, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) |

## Problem Description
### Goal
A nonempty singly-linked list stores the binary representation of a number. Every node contains either zero or one, and the head node holds the most significant bit. Moving toward the tail therefore moves from higher to lower binary place values.

Return the decimal integer represented by the complete linked list. The list contains at most 30 nodes, is guaranteed to be nonempty, and must be interpreted without changing the order of its bits.

### Function Contract
**Inputs**

- `head`: the first node of a nonempty singly-linked list containing $n$ binary digits, where $1 \le n \le 30$.

**Return value**

The nonnegative integer whose base-two digits, from most significant to least significant, are the node values encountered from `head` to the tail.

### Examples
**Example 1**

- Input: `head = [1,0,1]`
- Output: `5`
- Explanation: The stored binary number is $101_2$, which equals $5$.

**Example 2**

- Input: `head = [0]`
- Output: `0`

**Example 3**

- Input: `head = [1,1,1,1]`
- Output: `15`
