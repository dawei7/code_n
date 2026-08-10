## General

**Most rows need no individual processing**

An entirely unreserved row can seat two families: one in seats 2 through 5 and one in seats 6 through 9. Those blocks are disjoint. Since $n$ may be as large as one billion while there are at most ten thousand reservation records, iterating through every row would be impossible.

The solution stores information only for rows that appear in `reservedSeats`. If `d` contains $q$ such row keys, the other $n-q$ rows are completely empty and contribute exactly

`(n - len(d)) * 2`

families. This bulk calculation is the reason the running time depends on reservations rather than on $n$.

A row reserved only at seat 1 or seat 10 still appears in `d` even though those aisle-edge seats do not affect any valid four-seat block. That row is removed from the bulk count, but its explicit mask processing will correctly add two families back.

**Encode ten seats in one integer**

For a reservation at row `i` and seat `j`, the code sets bit `10 - j`:

`d[i] |= 1 << (10 - j)`.

Seat 1 maps to bit 9, seat 2 to bit 8, and seat 10 to bit 0. A one bit means reserved; a zero bit means available. Bitwise OR accumulates all reserved seats in the same row without disturbing earlier ones.

The three legal blocks are encoded in matching ten-bit masks:

- `0b0111100000` represents seats 2, 3, 4, and 5.
- `0b0000011110` represents seats 6, 7, 8, and 9.
- `0b0001111000` represents the middle block, seats 4, 5, 6, and 7.

For row mask `x` and candidate `mask`, `x & mask` keeps only bits occupied in both. A result of zero means none of the candidate seats is reserved or already allocated.

**Treat allocated seats like reservations**

When a block is free, the code performs `x |= mask` and increments `ans`. Setting those bits marks the group's seats unavailable to later groups in the same row. The local integer `x` therefore represents both original reservations and allocations already chosen by the greedy loop.

The candidate order is left block, right block, then middle block. This ordering is deliberate and safe:

- The left and right blocks are disjoint, so if both are free, selecting them yields two families, the maximum possible in one row.
- The middle block overlaps both outer blocks. It can contribute at most one family and should not be allowed to block two available outer groups.
- If only one outer block is free, selecting it yields one family. The middle block cannot coexist with that selected outer block, so no two-family solution was lost.
- If neither outer block is free but the middle block is free, the first two checks add nothing and the third adds the one possible family.

Thus greedily testing the two nonoverlapping outer blocks first always attains the per-row optimum.

**Why two is the maximum for one row**

Every family needs four seats among the eight relevant seats 2 through 9. Three families would require twelve distinct seats, so at most two fit. The only pair of legal blocks that does not overlap is left `[2,5]` plus right `[6,9]`. This limited geometry makes the greedy proof complete; no large interval-scheduling algorithm is needed.

**A reservation-mask example**

Suppose a row has reserved seat 5. The left mask intersects the reservation, so it is unavailable. The right block 6 through 9 is free, so it is allocated and its bits are added to `x`. The middle block overlaps both reserved seat 5 and the newly allocated right block, so it is rejected. The row contributes one family, which is optimal.

If only seats 1 and 10 are reserved, neither outer mask intersects `x`. Both outer groups are added, and the middle then intersects their allocated bits. The row contributes two.

**Why the algorithm is correct**

Every unrecorded row is empty and contributes exactly two groups. For each recorded row, mask intersection accepts only blocks containing no reserved or previously allocated seat, so every counted family is feasible and no seat is reused.

The outer-first case analysis proves the loop counts two exactly when both disjoint outer blocks are available, otherwise one exactly when any legal block is available, and zero otherwise. These are all possible per-row optima. Rows are independent because groups never span rows. Summing their exact optima therefore gives the global maximum.

## Complexity detail

Let $r$ be the number of reservation records and $q$ the number of distinct rows containing at least one reservation. Building masks takes $O(r)$ expected time. Processing each of the $q$ masks tests exactly three constant-size candidates, taking $O(q)$. Since $q\le r$, total time is $O(r)$.

The dictionary stores one integer per distinct reserved row, so space is $O(q)=O(\min(n,r))$, matching the manifest. The enormous value of $n$ affects only constant-time arithmetic, not iteration or allocation.

## Alternatives and edge cases

- **Boolean array per reserved row:** Store ten availability flags and test the three blocks. It is readable but uses more per-row objects than one integer mask.
- **Set of reserved coordinates:** For each affected row, ask whether any block seat pair occurs in the set. It can work but performs more hashing and obscures block overlap.
- **Iterate every row:** This is infeasible because $n$ can reach one billion even though the reservation list is small.
- **Test the middle block first:** It can greedily consume seats 4 through 7 and prevent two free outer groups, producing one instead of the optimal two.
- **No reservations in a row:** The bulk term awards two groups.
- **Reservations only at seats 1 or 10:** Those bits intersect no family mask, so the row still receives two groups.
- **Both outer blocks free:** They are allocated first and contribute two.
- **Outer blocks blocked, middle free:** The third mask contributes one.
- **All legal blocks blocked:** No mask has zero intersection and the row contributes zero.
- **Overlapping allocations:** OR-ing a chosen mask into `x` prevents any later overlap.
- **Distinct reservation records:** Repeated input pairs are excluded, though bitwise OR would tolerate them.
- **Seat-bit direction:** The reversed mapping `10-j` is consistent with all three binary literals; changing one without the other would corrupt checks.
- **Required import:** `defaultdict` must be available, normally from `collections`.
