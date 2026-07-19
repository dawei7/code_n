# Max Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 716 |
| Difficulty | Hard |
| Topics | Linked List, Stack, Design, Doubly-Linked List, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/max-stack/) |

## Problem Description
### Goal
Design a maximum stack that supports ordinary last-in-first-out behavior and efficient maximum-value operations. Implement `push(x)`, `pop()`, and `top()` together with `peekMax()`, which reads the largest stored value, and `popMax()`, which removes and returns it.

When the maximum value occurs more than once, `popMax()` must remove the occurrence closest to the top of the stack. Only removal operations modify the sequence; reading the top or maximum leaves it unchanged, and all remaining elements keep their relative stack order after a maximum is removed.

### Function Contract
**Inputs**

- `operations`: ordered calls named `push` with one integer argument or `pop`, `top`, `peekMax`, and `popMax` with no arguments

**Return value**

- A list containing the result of every non-`push` call in operation order

### Examples
**Example 1**

- Input: `operations = [["push",5],["push",1],["push",5],["top"],["popMax"],["top"],["peekMax"],["pop"],["top"]]`
- Output: `[5,5,1,5,1,5]`

**Example 2**

- Input: `operations = [["push",7],["push",7],["push",3],["peekMax"],["popMax"],["top"],["pop"],["top"]]`
- Output: `[7,7,3,3,7]`

**Example 3**

- Input: `operations = [["push",-2],["push",-5],["push",-2],["popMax"],["peekMax"],["top"]]`
- Output: `[-2,-2,-5]`
