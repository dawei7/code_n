# Guided Example: Count the Number of Computer Unlocking Permutations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"complexity": [1, 2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `complexity` of length `n`.

The objective is to compute `2` from `{"complexity": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why every later complexity must exceed complexity[0]

To unlock computer `i>0`, some already unlocked computer `j` must satisfy both:

$$
j<i
\quad\text{and}\quad
complexity[j] < complexity[i].
$$

Suppose some non-root computer has complexity at most `complexity[0]`. Consider a non-root computer with globally minimum complexity among all such problematic computers and, more broadly, among the array’s minimum values.

If its complexity is below the root’s, no computer has a strictly smaller complexity available anywhere, so it cannot be unlocked.

If its complexity equals the root’s and this is the global minimum, computer zero is not strictly lower, and no other computer is strictly lower either. It also cannot be unlocked.

Index restrictions cannot rescue either case; they only reduce the possible helpers further. Therefore the existence of any later value `<= complexity[0]` implies answer zero.

The source detects exactly this condition during the loop and returns immediately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"complexity": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the condition is sufficient

Now suppose every `complexity[i]` for `i>0` is strictly greater than `complexity[0]`.

For every such computer:

- helper computer zero has label `0<i`;
- its complexity is strictly lower;
- it is already decrypted from the beginning.

So every non-root computer is eligible immediately, independently of which other computers have been unlocked. No dependency among computers one through `n-1` remains.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Now suppose every `complexity[i]` for `i>0` is strictly grea... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Counting valid orders

Computer zero must be the initially unlocked root, so it occupies the first position in every represented unlocking order. The remaining `n-1` distinct labels can be arranged arbitrarily.

The number of orders is

$$
(n-1)!.
$$

The source initializes `ans=1` and, for loop indices `i=1` through `n-1`, multiplies `ans` by `i`. The product is exactly `1\cdot2\cdots(n-1)`.

Modulo `10^9+7` is applied after every multiplication. The identity

$$
(ab)\bmod M
= ((a\bmod M)(b\bmod M))\bmod M
$$

ensures this produces the required factorial residue without building the enormous exact factorial.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"complexity": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort by complexity:** Sorting can reveal wheth:** - **Sort by complexity:** Sorting can reveal whether the root is uniquely smallest, but costs `O(n\log n)` and loses the simplicity of a direct scan.
- **Build dependency edges:** Explicitly connecting each computer to eligible helpers can create quadratic work. The root-minimum observation makes the graph unnecessary.
- **Topological permutation DP:** General dependency-order counting is difficult, but this instance collapses to either no order or all orders of the non-root labels.
- **Root tied for minimum:** Strict inequality is required, so any later equal minimum makes the answer zero.
- **A later value below the root:** Some global-minimum non-root computer has no lower-complexity helper and blocks all complete permutations.
- **Root uniquely smallest:** Every later computer is available from the start, even if their complexities are equal to one another.
- **Later duplicate complexities:** They do not conflict when all exceed the root; each can independently use computer zero.
- **Index condition:** Root label zero is less than every non-root label, which is why it serves universally.
- **Smallest valid n:** With two computers and a valid root minimum, `(n-1)!=1`, so only order `[0,1]` exists.
- **Early failure:** Returning on the first bad complexity is safe because one impossible computer already prevents a full permutation.
- **Modulo:** Applying it incrementally preserves the factorial residue and bounds intermediate values.
- **Computer zero fixed first:** It is pre-unlocked by label, not chosen dynamically from the permutation.
- **Unique passwords:** Password identity does not alter the count; only complexity comparisons and labels matter.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop visits each non-root complexity once. It performs a comparison and, if valid, one modular multiplication. Time complexity is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
