# Double a Number Represented as a Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2816 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Math, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/) |

## Problem Description

### Goal

You are given the head of a non-empty singly linked list whose node values are the decimal digits of a non-negative integer. The most significant digit comes first, and the representation has no leading zero unless the number itself is `0`.

Double the represented integer and return the head of a linked-list representation of the result. The result must keep the same most-significant-first digit order and may require one additional leading node when doubling produces a carry beyond the original first digit.

### Function Contract

**Inputs**

- `head`: The first node of a non-empty singly linked list containing the integer's decimal digits.

Let $n$ be the number of nodes. Then $1 \leq n \leq 10^4$, every node value is between $0$ and $9$, and the first value is nonzero unless the list is exactly `[0]`.

**Return value**

Return the head of a linked list whose digits represent twice the input integer, with no leading zero unless the result is zero.

### Examples

#### Example 1

- **Input:** `head = [1,8,9]`
- **Output:** `[3,7,8]`
- **Explanation:** The input represents $189$, and $2 \cdot 189 = 378$.

#### Example 2

- **Input:** `head = [9,9,9]`
- **Output:** `[1,9,9,8]`
- **Explanation:** The input represents $999$, and doubling it produces the four-digit value $1998$.

#### Example 3

- **Input:** `head = [0]`
- **Output:** `[0]`
- **Explanation:** Doubling zero leaves the single valid zero representation unchanged.
