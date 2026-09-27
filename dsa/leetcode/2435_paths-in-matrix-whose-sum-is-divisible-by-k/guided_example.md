# Guided Example: Paths in Matrix Whose Sum Is Divisible by K

We walk one 3 × 3 instance from the raw grid to the final count, using the
official first example:

- **Input:** `grid = [[5,2,4],[3,0,5],[0,7,2]]`, `k = 3`
- **Required output:** `2`

The grid is deliberately full of zeros and of values that repeat across rows, so
the instance exposes the central difficulty: path *identity* matters, while the
values the paths collect can coincide.

---

## 1. The instance and the true size of the search space

A legal path starts at `(0, 0)` and reaches `(2, 2)` using only down and right
moves. Reaching the last row costs $m-1 = 2$ down moves and reaching the last
column costs $n-1 = 2$ right moves, so every path has exactly four moves and is
determined by which two of them are down moves. The number of geometric paths is

$$
\binom{m+n-2}{\,m-1\,} = \binom{4}{2} = 6 .
$$

Enumerating those six paths is a legitimate way to see what the answer must be.

| # | Move word | Visited cells | Element sequence | Sum $S$ | $S \bmod 3$ | Divisible? |
|---|---|---|---|---|---|---|
| 1 | `DDRR` | `(0,0),(1,0),(2,0),(2,1),(2,2)` | `5, 3, 0, 7, 2` | `17` | 2 | no |
| 2 | `DRDR` | `(0,0),(1,0),(1,1),(2,1),(2,2)` | `5, 3, 0, 7, 2` | `17` | 2 | no |
| 3 | `DRRD` | `(0,0),(1,0),(1,1),(1,2),(2,2)` | `5, 3, 0, 5, 2` | `15` | 0 | **yes** |
| 4 | `RDDR` | `(0,0),(0,1),(1,1),(2,1),(2,2)` | `5, 2, 0, 7, 2` | `16` | 1 | no |
| 5 | `RDRD` | `(0,0),(0,1),(1,1),(1,2),(2,2)` | `5, 2, 0, 5, 2` | `14` | 2 | no |
| 6 | `RRDD` | `(0,0),(0,1),(0,2),(1,2),(2,2)` | `5, 2, 4, 5, 2` | `18` | 0 | **yes** |

Two of the six sums give remainder zero, so the required answer is `2`.

Path 1 and path 2 are a warning about naive reasoning. They visit *different*
cells — one passes through `(2, 0)`, the other through `(1, 1)` — yet they collect
the identical value sequence `5, 3, 0, 7, 2`, because `grid[1][1] = 0` and
`grid[2][0] = 0`. Any reasoning that groups paths by the multiset of values they
collect, or that treats "two paths through the same values" as one path, will
undercount. The count must be over paths, and the only quantity that may be
collapsed is the sum's residue.

---

## 2. State definition: counting paths by remainder

Let $g_{ij} = \texttt{grid}[i][j] \bmod K$ be the cell value reduced modulo $K$.
Divisibility of the total depends on residues alone, so the dynamic program keeps
one counter per residue instead of per sum:

$$
f(i,j,r) = \#\{\text{monotone paths } (0,0) \to (i,j) \text{ with } \textstyle\sum \texttt{grid} \equiv r \pmod K\}.
$$

| Symbol | Meaning | Range in this instance |
|---|---|---|
| $m, n$ | grid dimensions | $m = 3$, $n = 3$ |
| $K$ | divisor | $K = 3$ |
| $g_{ij}$ | `grid[i][j]` reduced modulo $K$ | $\{0, 1, 2\}$ |
| $f(i,j,r)$ | number of paths from `(0,0)` to `(i,j)` whose element sum has remainder $r$ | non-negative integers |
| requested result | $f(m-1,\,n-1,\,0)$ | `2` |

The start cell is a path of length one, so the base case places a single path into
the bucket of its own remainder: $f(0,0,g_{00}) = 1$ and $f(0,0,r) = 0$ for every
other $r$. Here $g_{00} = 5 \bmod 3 = 2$, giving $f(0,0,\cdot) = (0, 0, 1)$ in the
reading order $(r{=}0, r{=}1, r{=}2)$.

---

## 3. Worked trace, cell by cell in row-major order

Every non-start cell is entered either from above or from the left, and those are
the only two options. Processing rows top to bottom and columns left to right
guarantees both predecessors are already final when a cell is reached. In the
table below, the row-major predecessor for each of the three remainder buckets is
written as the ordered triple $(\,n_0, n_1, n_2\,)$.

| Cell | `grid` value | $g_{ij}$ | From above (pulled bucket) | From left (pulled bucket) | $f(i,j,\cdot)$ | Paths reaching this cell |
|---|---|---|---|---|---|---|
| `(0,0)` | `5` | 2 | — | — | $(0, 0, 1)$ | 1 |
| `(0,1)` | `2` | 2 | — | $(0, 0)$ | $(0, 1, 0)$ | 1 |
| `(0,2)` | `4` | 1 | — | $(1, 2)$ | $(0, 0, 1)$ | 1 |
| `(1,0)` | `3` | 0 | $(2, 2)$ | — | $(0, 0, 1)$ | 1 |
| `(1,1)` | `0` | 0 | $(0, 0)$ | $(0, 0)$ | $(0, 1, 1)$ | 2 |
| `(1,2)` | `5` | 2 | $(2, 0)$ | $(1, 2)$ | $(1, 2, 0)$ | 3 |
| `(2,0)` | `0` | 0 | $(0, 0)$ | — | $(0, 0, 1)$ | 1 |
| `(2,1)` | `7` | 1 | $(1, 0)$ | $(2, 2)$ | $(2, 0, 1)$ | 3 |
| `(2,2)` | `2` | 2 | $(0, 2)$ | $(1, 0)$ | $(2, 1, 3)$ | 6 |

Reading the trace:

- At `(1,1)` the two incoming paths have residues 1 (via `5,2,0`) and 2 (via
  `5,3,0`), so the buckets for residues 1 and 2 each hold one path and residue 0
  holds none.
- At `(1,2)` the cell value `5` has residue 2. Incoming residues 1 and 2 shift to
  0 and 1, so the bucket `f(1,2,1)` receives two paths while `f(1,2,0)` receives
  the single path whose predecessor residue was 1.
- The last cell collects all six paths — the total in the final row sums to
  $2 + 1 + 3 = 6$, matching $\binom{4}{2}$ from section 1. That agreement is a
  useful self-check on any trace.
- Only the residue-0 bucket of the destination is requested, so the answer is
  $f(2,2,0) = 2$.

---

## 4. The backward remainder lookup

A predecessor path with remainder $r_0$ becomes a path with remainder
$(r_0 + g_{ij}) \bmod K$ after the current cell is appended. The table is filled by
*target* residue, so the recurrence has to invert that shift:

$$
(r_0 + g_{ij}) \bmod K = r \quad\Longleftrightarrow\quad r_0 = \bigl((r - g_{ij}) \bmod K + K\bigr) \bmod K .
$$

Adding $K$ before the outer reduction keeps the intermediate value
non-negative, which matters in fixed-width languages where a negative remainder
would be produced by the subtraction alone.

| $g_{ij}$ | bucket $r = 0$ pulls | bucket $r = 1$ pulls | bucket $r = 2$ pulls |
|---|---|---|---|
| 0 | 0 | 1 | 2 |
| 1 | 2 | 0 | 1 |
| 2 | 1 | 2 | 0 |

For the destination cell `(2,2)` the value is `2` and $g = 2$, so bucket 0 pulls
predecessor bucket 1, bucket 1 pulls predecessor bucket 2, and bucket 2 pulls
predecessor bucket 0:

| Destination bucket $r$ | Pulled bucket $r_0$ | Paths above, $f(1,2,r_0)$ | Paths left, $f(2,1,r_0)$ | $f(2,2,r)$ |
|---|---|---|---|---|
| 0 | 1 | 2 | 0 | **2** |
| 1 | 2 | 0 | 1 | 1 |
| 2 | 0 | 1 | 2 | 3 |

The two contributions are added, not merged by taking a maximum, because the task
counts paths rather than optimizes over them. Every addition is reduced modulo
$10^9 + 7$; modular addition commutes with the residue bookkeeping, so reducing
early never changes the requested count, which is itself understood modulo that
value.

---

## 5. Why the reasoning is correct: the invariant

> **Invariant.** After cell $(i,j)$ has been processed, $f(i,j,r)$ equals the
> number of monotone paths from `(0,0)` to `(i,j)` whose element sum is congruent
> to $r$ modulo $K$, for every $r \in \{0,\dots,K-1\}$.

The proof is an induction on the row-major order of the cells.

*Base.* Cell `(0,0)` is reached by exactly one path — the empty move word — whose
sum is `grid[0][0]`. Its bucket holds 1 and all others hold 0, so the invariant
holds at the start.

*Step.* Assume the invariant for every cell strictly earlier in row-major order.
Take a cell `(i,j)` that is not the start. Every path to it ends with a down move
from `(i-1,j)` or a right move from `(i,j-1)`, and those two families are
**disjoint**: a path's last move is uniquely determined by its endpoint and the
cell it came from, so no path is counted twice by the two additions. The
backward lookup of section 4 selects exactly those predecessor paths whose sum is
congruent to $r - g_{ij}$, which is precisely the condition for the extended sum
to be congruent to $r$. Every path to `(i,j)` therefore appears in exactly one
term of exactly one bucket, and no path is invented. The invariant is preserved.

*Conclusion.* Applying the invariant at `(m-1, n-1)` with $r = 0$ gives exactly
the requested count, since a sum is divisible by $K$ if and only if its residue
modulo $K$ is zero. Because only residues are ever stored, and because addition of
$g_{ij}$ distributes over congruence classes, replacing each partial sum by its
residue loses no information about the final divisibility test — this is the
substitution principle for modular arithmetic, and it is what allows the table to
have $K$ entries per cell rather than one entry per reachable sum.

---

## 6. Boundaries and traps this instance exposes

| Situation | Behaviour | Reason |
|---|---|---|
| Single cell, `grid = [[6]]`, `k = 3` | returns `1` | $g_{00} = 0$, so the base case puts one path in bucket 0 |
| Single cell, `grid = [[5]]`, `k = 3` | returns `0` | $g_{00} = 2$; the nonzero buckets are never read at the destination |
| One row or one column | exactly one geometric path | only one predecessor direction exists, and the guards suppress the missing one |
| $K = 1$ | every path qualifies, so the answer is $\binom{m+n-2}{m-1}$ | all values reduce to $g = 0$, so every bucket update keeps residue 0 and the counts simply add |
| Zero-valued cells | residue unchanged, $r_0 = r$ | appending 0 does not move a path between buckets; this is why `(1,1)` and `(2,0)` pass residues through unchanged |
| Distinct paths, equal value sequences | both are counted separately | paths 1 and 2 of section 1 show that identity is positional, not value-based |
| First row / first column | only one contribution | there is no cell above row 0 nor left of column 0, so one addend is absent rather than zero-valued |
| Destination buckets other than 0 | must be ignored | a sum congruent to 1 or 2 is not divisible by `K`; summing the whole destination triple would overcount |
| Large counts | reduced modulo $10^9+7$ at each state | the true count grows like $\binom{m+n-2}{m-1}$, far beyond fixed-width integers, and only the reduced value is requested |
| Extreme aspect ratio | $m = 1$ with $n = 50000$ is legal | the constraints bound only the product $m \cdot n \le 5 \cdot 10^4$, not each dimension separately |

---

## 7. Alternative formulations and their trade-offs

| Approach | Time | Auxiliary space | Why it is or is not preferable here |
|---|---|---|---|
| Enumerate all move words and sum each path | $\Theta\!\left(\binom{m+n-2}{m-1}(m+n)\right)$ | $O(m+n)$ per path | Correct but exponential; on the largest square grid the constraints allow, $m = n = 223$, the path count exceeds $10^{130}$ |
| Recurrence over exact path sums, keyed by the sum itself | $O(mn \cdot S)$ | $O(mnS)$ | $S$ can reach $100(m+n)$, hundreds of times larger than $K$; residues suppress exactly this waste |
| Memoized recursion on `(i,j,r)` | $O(mnK)$ expected | $O(mnK)$ states plus call stack of depth $m+n$ | Same state count, but the recursion depth can reach $m+n$, which is the risky part for very elongated grids |
| Full three-dimensional table filled row-major | $O(mnK)$ | $O(mnK)$ | Simple, and the order guarantees both predecessors are complete; costs $mnK$ count slots |
| Two rolling rows of remainder vectors | $O(mnK)$ | $O(nK)$ | Retains only the row above and the row being built; the left neighbour of the current row stays available, so the recurrence is unaffected |
| Suffix formulation counting paths from `(i,j)` to the destination | $O(mnK)$ | $O(mnK)$ | Symmetric mirror of the same idea by reversing the grid traversal; no asymptotic gain |

---

## 8. Complexity derivation

Let $m$ and $n$ be the grid dimensions and $K$ the divisor.

**Time.** The table has one state per triple $(i,j,r)$, that is $m \cdot n \cdot K$
states. Filling a state performs one modulo subtraction to find the pulled bucket
index, at most two additions (one per existing predecessor), and one modular
reduction — a constant number of operations independent of $m$, $n$ and $K$.
The total time is therefore

$$
O(m \cdot n \cdot K).
$$

**Auxiliary space.** The full table stores $m \cdot n \cdot K$ counters, so the
straightforward implementation uses $O(m \cdot n \cdot K)$ auxiliary space. Only
the row above and the current row are ever read, so a rolling-row variant reduces
this to $O(n \cdot K)$; the recurrence itself requires no other structure. The
input grid is read but never copied, and the scalar loop indices and pulled
bucket indices add $O(1)$.

**Concrete magnitude.** The constraints give $m \cdot n \le 5 \cdot 10^4$ and
$K \le 50$, so the number of states is at most $2.5 \cdot 10^6$. That is small
enough that the $O(mnK)$ time bound is comfortable, while the choice between the
full table and two rolling rows is the difference between roughly $2.5 \cdot 10^6$
and roughly $n \cdot K$ stored counters. The answer itself is the single value
$f(m-1, n-1, 0)$ taken modulo $10^9+7$.
