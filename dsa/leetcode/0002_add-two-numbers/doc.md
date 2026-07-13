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

### Required Complexity

- **Time:** $O(\max(n, m))$
- **Space:** $O(\max(n, m))$

<details>
<summary>Approach</summary>

#### General

**The storage order matches carry propagation**

Decimal addition begins with the ones column because a carry travels toward more significant digits. These lists already store the ones digit first, so their forward direction is exactly the order in which columns must be processed. Reversing the lists or reconstructing whole integers would discard that useful representation.

At position `i`, read the digit from each list when present and use zero after a list ends. Add both digits and the incoming carry. The result digit is `total % 10`, while `floor(total / 10)` becomes the carry into the next column.

Continue until both lists are exhausted and the carry is zero. Including the carry in the loop condition is essential: `[9] + [1]` produces the extra most-significant digit in `[0, 1]`.

**A column-by-column trace**

For `l1 = [2, 4, 3]` and `l2 = [5, 6, 4]`:

| Decimal column | Calculation | Appended digit | Carry |
|---:|---|---:|---:|
| Ones | $2 + 5 + 0$ | 7 | 0 |
| Tens | $4 + 6 + 0$ | 0 | 1 |
| Hundreds | $3 + 4 + 1$ | 8 | 0 |

The digits are produced directly in the required least-significant-first order: `[7, 0, 8]`.

**Why local column decisions form the exact sum**

After processing `i` columns, the output fixes precisely the lowest `i` decimal digits of the sum. Integer division separates each column total into the only possible digit for that place and the complete contribution to the next place. No later column can alter an already emitted lower digit. When no input digit or carry remains, the representation is complete.

#### Complexity detail

The algorithm processes one position until the longer list ends, plus at most one final carry, for $O(\max(n, m))$ time. The returned digit list uses $O(\max(n, m))$ space; the arithmetic state itself is constant-size.

#### Alternatives and edge cases

- **Convert each list to an integer:** depends on arbitrary-precision arithmetic and can overflow in fixed-width languages.
- **Reverse both inputs:** adds unnecessary work and moves against the natural carry direction.
- **Recursive addition:** expresses the same recurrence but consumes linear call-stack space and may hit recursion limits.
- Different lengths are handled by treating missing digits as zero. A final carry must become a new result digit.

</details>
