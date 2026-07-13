# Add Two Numbers II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 445 |
| Difficulty | Medium |
| Topics | Linked List, Math, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/add-two-numbers-ii/) |

## Problem Description
### Goal
Two nonempty singly linked lists encode nonnegative integers with one decimal digit per node in most-significant-first order. Add the represented values using ordinary base-ten arithmetic while preserving the forward digit convention.

Return a linked list containing the sum's digits from most significant to least significant, with no leading zero except for the number zero itself. Propagate carries across unequal list lengths and create a new leading digit when needed. Meet the follow-up challenge without reversing the input lists, and return actual linked nodes rather than only a numeric string.

### Function Contract
**Inputs**

- `l1`: the app-local list of digits for the first number in forward order
- `l2`: the app-local list of digits for the second number in forward order

**Return value**

- Return the sum's digits in forward order with no leading zero except for zero itself. The native artifact accepts and returns LeetCode `ListNode` chains.

### Examples
**Example 1**

- Input: `l1 = [7, 2, 4, 3], l2 = [5, 6, 4]`
- Output: `[7, 8, 0, 7]`

**Example 2**

- Input: `l1 = [2, 4, 3], l2 = [5, 6, 4]`
- Output: `[8, 0, 7]`

**Example 3**

- Input: `l1 = [0], l2 = [0]`
- Output: `[0]`

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(m + n)$

<details>
<summary>Approach</summary>

#### General

**Use stacks to reach least-significant digits first**

Addition begins at the rightmost digits, but the input order exposes the most significant digits first and may not be reversed. Copy each list's digits into a stack so popping produces the required right-to-left order.

**Propagate the carry while either stack remains**

Repeatedly pop one digit from each nonempty stack, add them with the carry, and split the total into `digit = total % 10` and `carry = total // 10`. Continue while either stack or the carry remains, which naturally handles unequal operand lengths and a new leading digit.

**Prepend each computed digit**

Digits are computed least-significant first but the result must be forward ordered. In the native linked form, create each new result node with the current head as its `next`. The app-local list adaptation collects reverse digits and reverses them once at the end.

**Why the produced digits equal the arithmetic sum**

At each decimal position, the algorithm adds exactly the two operand digits at that place plus the carry from the previous place. Remainder modulo ten is the result digit and integer division is precisely the carry into the next position. Induction from the units position through the final carry proves the full forward digit sequence represents the sum.

#### Complexity detail

Every digit is pushed and popped once, so time is $O(m + n)$. The operand stacks and returned digits use $O(m + n)$ space; the native result nodes are required output.

#### Alternatives and edge cases

- **Reverse both input lists:** permits ordinary forward addition but violates the requirement not to modify the inputs unless they are restored.
- **Recursive alignment by length:** can propagate carries without explicit stacks but uses $O(m + n)$ call-stack space and more intricate carry handling.
- **Rescan from the head for every right-side digit:** remains correct but takes $O((m + n)^2)$ time.
- **Different lengths:** a missing digit contributes zero.
- **Final carry:** prepend it as a new most-significant digit.
- **Both inputs zero:** return exactly one zero digit.

</details>
