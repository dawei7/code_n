## General

The classroom has at most eight columns, which makes a bitmask suitable for representing one row. Bit `c` equals one when column `c` is available or occupied, depending on the particular mask being discussed. The solution performs dynamic programming row by row while remembering how the previous row’s students restrict diagonal seats in the next row.

**Convert each physical row to an availability mask**

The helper `f` starts with zero and scans a row. For every usable `'.'` seat at column `i`, it sets bit `i` using `mask |= 1 << i`. Broken `'#'` seats leave their bits zero.

The list `ss` contains one such base availability mask per classroom row. A one bit means a student may potentially sit there before cheating restrictions from the preceding row are applied.

**Define the memoized state**

`dfs(seat, i)` returns the maximum number of students that can be placed from row `i` through the last row. The `seat` mask describes positions currently allowed in row `i` after combining that row’s unbroken-seat mask with diagonal restrictions caused by students chosen in row `i - 1`.

The same row index can be reached with different availability masks depending on the preceding placement. Caching by both `seat` and `i` preserves exactly the information future decisions need and prevents repeated computation of identical subproblems.

**Enumerate every placement in the current row**

`mask` ranges from zero through `2^n - 1`, representing every subset of columns. It is a legal current-row placement only if two conditions hold.

First, `(seat | mask) == seat` means every one bit selected by `mask` was already a one bit in `seat`. If `mask` selected a broken or diagonally forbidden seat, the union would add a bit and differ from `seat`.

Second, `mask & (mask << 1)` must be zero. Shifting the occupied mask left aligns every occupied seat with the column immediately beside it. A common one bit means two selected students are horizontally adjacent and could see each other’s answers. Rejecting such masks enforces both left and right adjacency because every neighboring pair is detected once.

For a legal placement, `mask.bit_count()` gives the number of students seated in the current row.

**Pass diagonal restrictions to the next row**

If row `i` is not the last row, `nxt = ss[i + 1]` begins with the next row’s unbroken seats. A student in current column `c` can be seen from the next row at columns `c - 1` and `c + 1`.

`mask << 1` marks one diagonal direction, and `mask >> 1` marks the other. The statements
`nxt &= ~(mask << 1)` and `nxt &= ~(mask >> 1)` clear both sets of forbidden positions from the next availability mask.

Python’s bitwise complement has infinitely many leading one bits conceptually, but this is safe: `nxt` contains only the finite row bits, so the conjunction merely clears the shifted occupied positions among those bits.

There is no need to clear the same column. Students cannot see directly in front of or behind themselves, so vertical alignment is allowed.

The candidate total is the current `cnt` plus `dfs(nxt, i + 1)`. On the final row there is no future state, so the candidate is simply `cnt`. Taking the maximum over every legal `mask` gives the best placement for the state.

**Why row-local choices are sufficient**

Cheating conflicts exist only within one row and between two adjacent rows. Once the current placement has converted its diagonal effect into `nxt`, no earlier row can directly affect row `i + 1` or anything below it. Thus `nxt` and the next row index contain all information required for the remaining problem.

Every globally valid seating arrangement chooses one legal mask per row. The enumeration includes its current mask, and recursion includes its remaining row masks. Conversely, every combination accepted by the subset, horizontal, and diagonal checks is globally valid. Maximizing over these exact possibilities returns the greatest number of students.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

There are at most $m2^n$ distinct `(seat, i)` states because each row index can pair with at most $2^n$ availability masks. Each state enumerates all $2^n$ placement masks and performs constant-time bit operations under the small-width model. The worst-case time is $O(m4^n)$.

The cache can store $O(m2^n)$ state results. The recursion depth is at most $m$, and `ss` stores $m$ masks. Thus the symbolic auxiliary-space bound is $O(m2^n)$. Since the stated constraint fixes $m \le 8$, this is sometimes simplified to $O(2^n)$, which is the manifest form.

The exponential dependence is practical because both dimensions are at most eight; at most 256 masks exist for a row.

## Alternatives and edge cases

- **Iterative row DP:** Map each legal current placement to its best total and transition to compatible next-row masks. It avoids recursion and has comparable exponential bounds.
- **Precompute legal row masks:** Filter out horizontally adjacent masks once, then reuse that list for every state. This improves constants without changing the worst-case class.
- **Maximum independent set view:** Seats are graph vertices and cheating relations are edges. A generic graph algorithm ignores the narrow layered structure and is less efficient or harder to implement.
- **Broken seats:** A placement bit outside `seat` is rejected by the subset test.
- **Horizontal neighbors:** `mask & (mask << 1)` detects and rejects every adjacent occupied pair.
- **Diagonal neighbors:** Shifting the current mask both directions clears precisely the two forbidden columns in the next row.
- **Vertical neighbors:** Same-column students in adjacent rows are allowed and are intentionally not removed.
- **Empty placement:** `mask == 0` is always legal and ensures every state has at least one candidate.
- **All seats broken:** Only the zero mask is legal in every row, so the answer is zero.
- **Single row:** The method chooses the largest nonadjacent subset of its usable seats and never creates a next state.
- **Single column:** Horizontal and diagonal conflicts disappear within bounds, so every usable seat can hold a student.
- **Complement width:** Python’s unbounded complement is harmless only because it is immediately ANDed with the finite nonnegative `nxt` mask.
