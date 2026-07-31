## General
**The storage order matches carry propagation**

Decimal addition begins with the ones column because a carry travels toward more significant digits. These lists already store the ones digit first, so their forward direction is exactly the order in which columns must be processed. Reversing the lists or reconstructing whole integers would discard that useful representation.

At each pair of current nodes, read the digit from each list when present and use zero after a pointer reaches `None`. Add both digits and the incoming carry. The result digit is `total % 10`, while `floor(total / 10)` becomes the carry into the next column. Attach the digit as a new node after a dummy head, then advance each available input pointer through `next`.

Continue until both lists are exhausted and the carry is zero. Including the carry in the loop condition is essential: `[9] + [1]` produces the extra most-significant digit in `[0, 1]`.

**A column-by-column trace**

For `l1 = [2, 4, 3]` and `l2 = [5, 6, 4]`:

| Decimal column | Calculation | Appended node value | Carry |
|---:|---|---:|---:|
| Ones | $2 + 5 + 0$ | 7 | 0 |
| Tens | $4 + 6 + 0$ | 0 | 1 |
| Hundreds | $3 + 4 + 1$ | 8 | 0 |

The result nodes are produced directly in the required least-significant-first order: `7 -> 0 -> 8`.

**Why local column decisions form the exact sum**

After processing `i` columns, the output chain fixes precisely the lowest `i` decimal digits of the sum. Integer division separates each column total into the only possible digit for that place and the complete contribution to the next place. No later column can alter an already attached lower digit. When neither input pointer nor a carry remains, the chain is complete.

## Complexity detail
The algorithm processes one node position until the longer list ends, plus at most one final carry, for $O(\max(n, m))$ time. The returned linked list uses $O(\max(n, m))$ space; the dummy head, tail, pointers, and arithmetic state use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Convert each list to an integer:** depends on arbitrary-precision arithmetic and can overflow in fixed-width languages.
- **Reverse both inputs:** adds unnecessary work and moves against the natural carry direction.
- **Recursive addition:** expresses the same recurrence but consumes linear call-stack space and may hit recursion limits.
- Different lengths are handled by treating missing digits as zero. A final carry must become a new result digit.
