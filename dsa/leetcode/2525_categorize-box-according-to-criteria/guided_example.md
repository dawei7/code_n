# Guided Example: Categorize Box According to Criteria

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"length": 1000, "width": 35, "height": 700, "mass": 300}`
- **Required output:** `"Heavy"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given four integers `length`, `width`, `height`, and `mass`, representing the dimensions and mass of a box, respectively, return *a string representing the **category** of the box*.

The objective is to compute `"Heavy"` from `{"length": 1000, "width": 35, "height": 700, "mass": 300}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Evaluate two independent properties

The final category depends on two Boolean facts:

- whether the box is bulky;
- whether the box is heavy.

Neither property changes the definition of the other. The method computes them independently and then maps their four possible combinations to the required label.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"length": 1000, "width": 35, "height": 700, "mass": 300}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute volume exactly

`v=length*width*height` is the box volume.

The box is bulky if either:

- at least one dimension is at least 10,000;
- volume is at least $10^9$.

These alternatives are joined by logical OR. A box with small individual dimensions can still be bulky through their product, and one very large dimension makes it bulky even if volume is otherwise below the threshold.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `v=length*width*height` is the box volume.

The box is bulky... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check dimensions with `any`

The generator

`x>=10000 for x in (length,width,height)`

tests each of the three dimensions. `any` returns true when at least one test succeeds.

The outer `or v>=10**9` then incorporates the volume rule.

Boundary equality matters: `>=` correctly classifies a dimension exactly 10,000 or a volume exactly one billion as bulky.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Heavy"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"length": 1000, "width": 35, "height": 700, "mass": 300}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Heavy"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nested conditionals:** Explicitly test both, b:** - **Nested conditionals:** Explicitly test both, bulky only, heavy only, and neither; it is equally correct but longer.
- **Tuple lookup:** Use `(bulky,heavy)` as a dictionary key instead of a bit index.
- **Dimension exactly 10,000:** It is bulky.
- **Volume exactly $10^9$:** It is bulky.
- **Mass exactly 100:** It is heavy.
- **Large dimension and heavy mass:** Return `"Both"`.
- **Large volume with small dimensions:** Volume alone is sufficient for bulky status.
- **Neither threshold met:** Return `"Neither"`.
- **Overflow:** Fixed-width implementations need safe volume arithmetic.
- **Independent predicates:** Compute both before selecting a label.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a fixed number of comparisons, multiplications, Boolean operations, and one list lookup. Time is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
