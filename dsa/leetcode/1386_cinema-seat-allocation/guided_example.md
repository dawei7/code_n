# Guided Example: Cinema Seat Allocation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "reservedSeats": [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

![](images/cinema_seats_1.png)

The objective is to compute `4` from `{"n": 3, "reservedSeats": [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Most rows need no individual processing

An entirely unreserved row can seat two families: one in seats 2 through 5 and one in seats 6 through 9. Those blocks are disjoint. Since $n$ may be as large as one billion while there are at most ten thousand reservation records, iterating through every row would be impossible.

The solution stores information only for rows that appear in `reservedSeats`. If `d` contains $q$ such row keys, the other $n-q$ rows are completely empty and contribute exactly

`(n - len(d)) * 2`

families. This bulk calculation is the reason the running time depends on reservations rather than on $n$.

A row reserved only at seat 1 or seat 10 still appears in `d` even though those aisle-edge seats do not affect any valid four-seat block. That row is removed from the bulk count, but its explicit mask processing will correctly add two families back.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "reservedSeats": [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Encode ten seats in one integer

For a reservation at row `i` and seat `j`, the code sets bit `10 - j`:

`d[i] |= 1 << (10 - j)`.

Seat 1 maps to bit 9, seat 2 to bit 8, and seat 10 to bit 0. A one bit means reserved; a zero bit means available. Bitwise OR accumulates all reserved seats in the same row without disturbing earlier ones.

The three legal blocks are encoded in matching ten-bit masks:

- `0b0111100000` represents seats 2, 3, 4, and 5.
- `0b0000011110` represents seats 6, 7, 8, and 9.
- `0b0001111000` represents the middle block, seats 4, 5, 6, and 7.

For row mask `x` and candidate `mask`, `x & mask` keeps only bits occupied in both. A result of zero means none of the candidate seats is reserved or already allocated.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a reservation at row `i` and seat `j`, the code sets bit... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Treat allocated seats like reservations

When a block is free, the code performs `x |= mask` and increments `ans`. Setting those bits marks the group's seats unavailable to later groups in the same row. The local integer `x` therefore represents both original reservations and allocations already chosen by the greedy loop.

The candidate order is left block, right block, then middle block. This ordering is deliberate and safe:

- The left and right blocks are disjoint, so if both are free, selecting them yields two families, the maximum possible in one row.
- The middle block overlaps both outer blocks. It can contribute at most one family and should not be allowed to block two available outer groups.
- If only one outer block is free, selecting it yields one family. The middle block cannot coexist with that selected outer block, so no two-family solution was lost.
- If neither outer block is free but the middle block is free, the first two checks add nothing and the third adds the one possible family.

Thus greedily testing the two nonoverlapping outer blocks first always attains the per-row optimum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "reservedSeats": [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean array per reserved row:** Store ten av:** - **Boolean array per reserved row:** Store ten availability flags and test the three blocks. It is readable but uses more per-row objects than one integer mask.
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
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of reservation records and $q$ the number of distinct rows containing at least one reservation. Building masks takes $O(r)$ expected time. Processing each of the $q$ masks tests exactly three constant-size candidates, taking $O(q)$. Since $q\le r$, total time is $O(r)$.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
