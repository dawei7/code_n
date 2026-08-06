## General
**The storage order matches carry propagation**

Decimal addition begins with the ones column because a carry travels toward more significant digits. These lists already store the ones digit first, so their forward direction is exactly the order in which columns must be processed. Reversing the lists or reconstructing whole integers would discard that useful representation.

At each pair of current nodes, read the digit from each list when present and use zero after a pointer reaches `None`. Compute `carry, digit = divmod(left + right + carry, 10)`: the remainder is the result digit for this column, and the quotient is the carry into the next column. Attach `digit` as a new node after the dummy head's tail, then advance each available input pointer through `next`.

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

After processing $i$ columns, the output chain fixes precisely the lowest $i$ decimal digits of the sum. The `divmod` result separates each column total into the only possible digit for that place and the complete contribution to the next place. No later column can alter an already attached lower digit. When neither input pointer nor a carry remains, the chain is complete.

## Complexity detail
Let $n$ and $m$ be the lengths of `l1` and `l2`. The algorithm processes each digit position through the longer list and may append one final carry, for $O(\max(n, m))$ time. The returned list uses $O(\max(n, m))$ space; the dummy head, tail, pointers, and arithmetic state use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Convert each list to an integer:** depends on arbitrary-precision arithmetic and can overflow in fixed-width languages.
- **Reverse both inputs:** adds unnecessary work and moves against the natural carry direction.
- **Recursive addition:** expresses the same recurrence but consumes linear call-stack space and may hit recursion limits.
- **Unequal lengths:** missing digits contribute zero, so either input may end first without a separate remainder loop.
- **Final carry:** a nonzero carry keeps the loop active after both input pointers reach `None` and becomes a new result node.
