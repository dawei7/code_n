## General
**Account for untouched rows immediately.** A row with no reservation in seats `2` through `9` can hold both disjoint outer blocks, `2-5` and `6-9`. Because `n` can be enormous, start from two families per row and inspect only rows whose relevant seats are reserved.

**Compress each touched row.** Store a bitmask for reserved seats `2` through `9`. Test that mask against the left, middle, and right block masks. If both outer blocks are free, the row contributes two families. Otherwise it contributes one when any of the three blocks is free, and zero when all are blocked.

The outer blocks are the only pair that can coexist; the middle block overlaps both. Therefore these three tests cover every legal allocation within a row, and summing independent row optima gives the global maximum. Reservations in seats `1` and `10` never affect a family block.

## Complexity detail
Each of the $r$ reservations is processed once, and each touched row receives constant mask work, so time is $O(r)$. At most $min(n,r)$ rows have relevant reservations, giving $O(\min(n,r))$ space.

## Alternatives and edge cases
- **Scan every row:** Build reservation masks and examine all `n` rows. It is correct but takes $O(n+r)$ time and is impossible when `n` approaches $10^9$.
- **Store every seat:** A set of coordinate pairs works but uses more state than one bitmask per touched row.
- **Seats 1 and 10:** Ignore them because no allowed family block contains either seat.
- **Only middle block free:** When both outer blocks are blocked, seats `4-7` may still hold one family.
- **Both outer blocks free:** Count two families and do not also count the overlapping middle block.
- **No reservations:** Every row contributes exactly two.
- **All blocks obstructed:** A touched row can contribute zero.
