# Add Two Polynomials Represented as Linked Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1634 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Math, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) |

## Problem Description
### Goal
A polynomial linked list stores one term per `PolyNode`. Each node contains an integer `coefficient`, a nonnegative integer `power`, and a pointer to the next term. Lists are in standard form: powers decrease strictly from head to tail, and zero-coefficient terms are omitted.

Given the heads `poly1` and `poly2`, add terms with equal powers and preserve every term whose power occurs in only one polynomial. Omit any equal-power term whose summed coefficient is zero. Return the head of the sum in the same strictly descending standard form. An empty list represents the zero polynomial.

### Function Contract
**Inputs**

- `poly1` and `poly2`: polynomial linked lists, serialized by cOde(n) as `[coefficient,power]` pairs in strictly decreasing power order.
- Each list has at most $10^4$ nodes; let their lengths be $n$ and $m$.
- Coefficients are nonzero integers from $-10^9$ through $10^9$, and powers range from 0 through $10^9$.

**Return value**

Return the standard-form sum as a `PolyNode` head. The cOde(n) harness serializes that list back to `[coefficient,power]` pairs; complete cancellation is returned as an empty list.

### Examples
**Example 1**

- Input: `poly1 = [[1,1]], poly2 = [[1,0]]`
- Output: `[[1,1],[1,0]]`

The polynomials $x$ and 1 sum to $x+1$.

**Example 2**

- Input: `poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]`
- Output: `[[5,2],[2,0]]`

The power-1 terms cancel, while the power-2 and constant coefficients add.

**Example 3**

- Input: `poly1 = [[1,2]], poly2 = [[-1,2]]`
- Output: `[]`

The only two terms cancel, leaving the zero polynomial.
