# Guided Example: Minimum Cost to Equalize Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 1], "cost1": 5, "cost2": 2}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and two integers `cost1` and `cost2`. You are allowed to perform **either** of the following operations **any** number of times:

The objective is to compute `15` from `{"nums": [4, 1], "cost1": 5, "cost2": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Describe a target by its deficits

All operations only increase values, so any common target $T$ must satisfy

$$
T\ge M=\max(\texttt{nums}).
$$

For index $i$, define its deficit as $d_i=T-\texttt{nums}[i]$. Every unit of deficit must be supplied by an operation. Let

$$
D=\sum_i d_i=nT-S,
$$

where $S=\sum_i\texttt{nums}[i]$. Let

$$
L=\max_i d_i=T-m,
$$

where $m=\min(\texttt{nums})$. The largest deficit always belongs to a minimum element.

A single operation fills one deficit unit for `cost1`. A pair operation fills two units belonging to different indices for `cost2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 1], "cost1": 5, "cost2": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When pair operations are irrelevant

If `cost2 >= 2 * cost1`, one pair operation costs at least as much as two single operations. Singles can reproduce its effect without restriction, so pairs never improve the answer.

For $n\le2$, raising the target above $M$ also cannot improve the cost. With two values, any paired increments above $M$ raise both sides together and do not eliminate the original gap; the smaller value's initial gap still needs singles. The cheapest target is $M$, where total deficit is `deficit_at_maximum = n * maximum - total`.

The early branch therefore returns

`deficit_at_maximum * cost1`

when either pairs are not cheaper than two singles or there are at most two elements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maximum usable pairs for a fixed target

Now assume $n\ge3$ and `cost2 < 2 * cost1`. We should use as many pair operations as possible.

Two independent limits apply:

1. Each pair consumes two of the $D$ units, so there can be at most $\lfloor D/2\rfloor$ pairs.
2. A pair cannot use the same index twice. If the largest-deficit index contributes one unit to a pair, the other unit must come from the remaining deficits, whose total is $D-L$. Thus there can be at most $D-L$ pairs when one index dominates.

Both limits are attainable by pairing deficit units from different indices, so

$$
P=\min\left(\left\lfloor\frac D2\right\rfloor,D-L\right).
$$

The remaining single units are

$$
R=D-2P.
$$

The nested `cost(target)` function implements exactly these formulas and returns

$$
P\cdot\texttt{cost2}+R\cdot\texttt{cost1}.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 1], "cost1": 5, "cost2": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every target:** The optimum may lie above the maximum, and scanning an unbounded or large target range is unnecessary. The piecewise-linear analysis reduces it to four candidates.
- **Priority queue of deficits:** Repeatedly pair the two largest remaining deficits. It can realize the fixed-target pairing count but would be far slower than the closed formula and still needs target selection.
- **Use singles only:** This is optimal when `cost2 >= 2 * cost1`, but can be much more expensive when pairs are cheap.
- **Always target the maximum:** It fails when a dominant minimum deficit forces many singles and a slightly larger target creates enough other deficits for cheap pairing.
- **One element:** It is already equal to itself; `deficit_at_maximum` is zero and the result is zero.
- **Two elements:** Raising both toward a higher target cannot remove their original difference. Pair increments cover only equal extra growth, so the gap is optimally paid with singles at the current maximum.
- **All values already equal:** Deficit at the maximum is zero. Candidate evaluation also yields zero at that target.
- **Pair cost equal to two singles:** Pairing offers no benefit, so the early single-only branch is valid.
- **Dominant largest deficit:** Pair count is limited by $D-L$, because every pair using that index needs a unit from some other index.
- **Balanced deficits with odd total:** One single unit remains after $\lfloor D/2\rfloor$ pairs. This parity effect is why a neighbor of the balance target is checked.
- **Ceiling boundary:** Both `balance - 1` and `balance` are evaluated because the formula changes regimes at the first balanced integer.
- **Modulo timing:** Taking each candidate cost modulo before `min` could select a much larger true cost whose residue is small; the exact source correctly minimizes first.
- **Generated-source note:** The repository solution is marked AI-generated because its upstream source was unavailable. The mathematical derivation above validates the behavior of this exact implementation rather than relying on that provenance note.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
