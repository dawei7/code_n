## General

Ordinary column addition begins at the least significant digit, because a column may produce a carry that must be added to the column immediately to its left. These linked lists are stored in the opposite direction: their heads contain the most significant digits. For example, the chain `7 -> 2 -> 4 -> 3` represents `7243`, but addition must begin with the tail digit `3`.

The exact solution uses two stacks to obtain the needed right-to-left access while leaving both input lists unchanged. A Python list works as a stack: `append` pushes onto its top, and `pop` removes the most recently pushed item.

**Turning forward lists into reverse access**

Traverse `l1` from head to tail and append every node value to `s1`; do the same for `l2` and `s2`. If the first number is `7 -> 2 -> 4 -> 3`, then `s1` becomes `[7, 2, 4, 3]`. Calling `s1.pop()` yields `3`, then `4`, then `2`, then `7`: precisely the least-significant-to-most-significant order required for addition.

Only digit values are stored. The original nodes and their `next` links are never changed. The local variables `l1` and `l2` advance through the lists, but reassigning those variables does not mutate the caller's linked lists.

**Adding one decimal column at a time**

The addition loop continues while `s1`, `s2`, or `carry` is nonempty or nonzero. In each iteration, it takes one digit from each stack when available. Once the shorter number runs out of digits, its contribution is zero. The current total is therefore

$$
s = \text{next digit of the first number} + \text{next digit of the second number} + \text{carry}.
$$

`divmod(s, 10)` returns the quotient and remainder of division by ten. The quotient becomes the carry for the next column, and the remainder is the current output digit. Since two input digits are each at most `9` and the incoming carry is at most `1`, $s \le 19$. Consequently the new carry is always either `0` or `1`, and the remainder is always a valid decimal digit from `0` through `9`.

The key state after each iteration is simple: all columns to the right of the current position have been added correctly, `carry` is exactly the amount that must enter the next column to the left, and the nodes already built represent the correct suffix of the sum.

**Why new digits are prepended**

Digits are computed from right to left, but the required output list is ordered from left to right. Appending new result nodes would therefore create the answer backward. Instead, the code inserts every new node at the front:

`dummy.next = ListNode(val, dummy.next)`

The new digit becomes the head, and the previously produced less significant digits follow it. Despite its name, `dummy` is not a node that is eventually attached to the returned list. It is a stable holder whose `next` field always points at the current answer head.

Consider `7243 + 564`:

1. Pop `3` and `4`: $3+4+0=7$. Prepending `7` gives `7`.
2. Pop `4` and `6`: $4+6+0=10$. The digit is `0`, the carry is `1`, and prepending gives `0 -> 7`.
3. Pop `2` and `5`: $2+5+1=8$. Prepending gives `8 -> 0 -> 7`.
4. Only `s1` remains. Pop `7`: $7+0+0=7$. Prepending gives `7 -> 8 -> 0 -> 7`.

The returned chain is therefore `[7, 8, 0, 7]`, representing `7807`.

Including `carry` in the loop condition handles an overflow beyond both input lengths without a special case. For example, `999 + 1` produces three `0` digits and leaves carry `1`. Both stacks are then empty, but `or carry` causes one final iteration, which creates the leading `1`. Conversely, when the final carry is zero, no extra leading-zero node is created.

**Why every output digit is correct**

At the start of an iteration, the stack tops are the next unprocessed digits at the same decimal place, because both stacks were filled from most significant to least significant and are popped in reverse. The previous iteration supplied exactly the carry from the place to the right. Decimal quotient and remainder therefore produce exactly the carry and digit dictated by column addition. Prepending places that digit immediately before all already-computed less significant digits. Repeating this step exhausts both numbers and any final carry, so the returned list represents their complete sum in most-significant-first order.

Fresh result nodes are important. The output shares no node with either input, so constructing the answer cannot corrupt the input chains. The problem guarantees nonempty lists, but the loop logic also naturally handles unequal lengths because an empty stack contributes zero.

## Complexity detail

Let $m$ and $n$ be the numbers of nodes in `l1` and `l2`.

Filling `s1` visits the first list once in $O(m)$ time, and filling `s2` visits the second once in $O(n)$ time. The addition loop performs at most $\max(m,n)+1$ iterations: one per digit position and possibly one for a final carry. Every iteration does constant-time stack, arithmetic, and node operations. Total time is $O(m+n)$.

The two stacks hold exactly $m+n$ digit values, so the auxiliary working space is $O(m+n)$. The newly allocated result contains at most $\max(m,n)+1$ nodes. Complexity conventions often separate required output storage from auxiliary storage; either way, the overall additional memory remains $O(m+n)$.

The call stack is constant because the method is iterative. Moving the local input pointers uses only constant space and does not copy or reverse the original nodes.

## Alternatives and edge cases

- **Reverse both input lists:** Reversing allows direct least-significant-first traversal with constant auxiliary pointer space, but it mutates the inputs and must either restore them or accept that side effect. The stack method satisfies the follow-up without reversing either input.
- **Recursive processing to the tails:** Recursion can align digits by list length and build the result while unwinding, but it is harder to reason about and consumes $O(m+n)$ call-stack space in the worst case.
- **Convert to machine integers:** Parsing all digits, adding integers, and converting back is concise in languages with arbitrary-precision integers, but it avoids the intended linked-list arithmetic and is not portable to fixed-width integer types.
- **Unequal lengths:** Once one stack is empty, its digit is treated as zero. The remaining digits of the longer number continue to be combined with the carry.
- **Final carry:** Inputs such as `[9,9,9]` and `[1]` require one more output node than either input. Keeping `carry` in the loop condition creates it automatically.
- **Zero plus zero:** The first iteration computes digit `0` and creates exactly one node. Since no carry remains, the result is `[0]`, not an empty list and not a list with multiple leading zeros.
- **Internal zero digits:** A computed zero is retained whenever it represents a real decimal place, as in `7243 + 564 = 7807`; only a nonexistent extra leading zero is avoided.
- **Input preservation:** Reassigning `l1` and `l2` while traversing changes only local references. No input node value or `next` pointer is modified.
