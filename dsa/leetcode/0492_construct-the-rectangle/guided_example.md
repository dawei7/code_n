# Guided Example: Construct the Rectangle

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"area": 4}`
- **Required output:** `[2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The objective is to compute `[2, 2]` from `{"area": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The area condition requires `L * W = area`, so `L` and `W` must form an integer factor pair. The condition `L >= W` means `W` is the smaller factor. Among all such pairs, the one with the smallest difference lies closest to a square.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"area": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

To see why, write `L = area / W` for a valid divisor `W`. As `W` grows from `1` toward `sqrt(area)`, `L` decreases while `W` increases. Their difference

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

therefore becomes smaller. Once `W` exceeds the square root, the factors swap order and violate the chosen `L >= W` orientation. Consequently, the desired width is the largest divisor of `area` that does not exceed `sqrt(area)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"area": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Search upward from one:** Every divisor can be remembered as the latest width, but this always scans to the square root. Descending search can stop as soon as the optimal divisor appears.
- **Enumerate all factor pairs:** This is unnecessary because factor closeness is monotonic as the smaller factor approaches the square root.
- **Exact integer square root:** `math.isqrt(area)` would compute the starting width without floating point and is preferable if the numeric constraint were much larger.
- **Perfect square:** The square root divides immediately, returning equal dimensions and the minimum possible difference zero.
- **Prime area:** Only one is a feasible width below the square root, so the answer is `[area, 1]`.
- **`area = 1`:** The starting width is one and the result is `[1, 1]`.
- **Ordering requirement:** Returning `[w, area // w]` would reverse length and width for non-square areas. The source returns the larger quotient first.
- **Guaranteed termination:** Width one divides every positive area, so the decrement loop cannot pass below one under the stated constraints.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{\textit{area}})$. The loop starts at approximately `sqrt(area)` and may decrement to one. In the worst case, such as a prime area, it performs $O(\sqrt{\textit{area}})$ divisibility tests. Each test is treated as constant-time under the standard fixed-width integer model, giving the manifest's $O(\sqrt{\textit{area}})$ time bound.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
