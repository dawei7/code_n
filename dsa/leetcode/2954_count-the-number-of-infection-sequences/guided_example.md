# Guided Example: Count the Number of Infection Sequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "sick": [0, 4]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` and an array `sick` sorted in increasing order, representing positions of infected people in a line of `n` people.

The objective is to compute `4` from `{"n": 5, "sick": [0, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Orders inside an exterior gap

In the leading gap, infection begins from its right boundary, next to the first initially sick person. People must become infected from right to left in one forced order.

The trailing gap is symmetric: infection progresses from left to right from the last initially sick person. Each exterior gap therefore has exactly one internal order, regardless of length.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "sick": [0, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Orders inside an internal gap

An internal gap has infected people on both ends. At any stage, the next infected person in that gap can be the leftmost remaining healthy position or the rightmost remaining healthy position.

For a gap of length $x$:

- during the first $x-1$ infections, choose left or right independently;
- after those choices, only one person remains, so the final infection is forced.

This gives

$$
2^{x-1}
$$

orders when $x>0$. For $x=1$, this is one. The source multiplies `pow(2, x - 1, mod)` only when `x > 1` because factors of one need no work.

Different left/right choice sequences produce different infection orders, and every legal order must repeatedly choose one of those two frontiers, so the count is exact.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An internal gap has infected people on both ends.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interleave the gaps

Fix one legal internal order for every gap. Infections belonging to different gaps do not constrain each other: at any moment, each nonempty gap's next frontier person is adjacent to an infected person within that gap.

We may therefore merge the gap-specific sequences while preserving order inside each gap. The number of such interleavings is the multinomial coefficient

$$
\binom{S}{g_0,g_1,\ldots,g_t}
=
\frac{S!}{\prod_i g_i!}.
$$

The source starts with `fac[S]` and multiplies by the modular inverse of `fac[x]` for every positive gap length $x$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "sick": [0, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate infection choices:** Enumerating sequ:** - **Simulate infection choices:** Enumerating sequences is exponential and repeats equivalent substructure.
- **Dynamic programming over infected sets:** State space is exponential in $n$.
- **Leading gap:** Only infection from right to left is legal; do not multiply it by a power of two.
- **Trailing gap:** Only left-to-right infection is legal.
- **Empty gap:** Its factorial is $0!=1$ and it contributes no internal order factor.
- **Internal gap of one:** It has one order, corresponding to $2^0$.
- **Adjacent sick people:** Their internal gap length is zero and requires no special branch beyond the existing checks.
- **All but one initially sick:** $S=1$, and exactly one infection sequence exists.
- **Sorted sick input:** Gap construction relies on the promised increasing order.
- **Factorial bound:** The fixed table size is safe only because $n\le100000$.
- **Modulo inverses:** Ordinary integer division after modular reduction would be invalid; Fermat inverses are required.
- **Why interleavings remain legal:** Taking the next scheduled infection from any gap preserves that gap's frontier order, so the chosen person is still adjacent to an already infected boundary or predecessor.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Module initialization computes `fac[0..100000]` in $O(100000)$ time and space once, independent of an individual call.
- **Auxiliary Space Complexity:** $O(n_{\max})$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
