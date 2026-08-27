# Guided Example: Count Special Triplets

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [6, 3, 6]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `1` from `{"nums": [6, 3, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map meanings

`right` initially counts every value in the complete array. `left` begins empty.

Immediately before counting current `x`, the source decrements `right[x]`. After that update:

- `left` contains exactly indices strictly before `j`;
- `right` contains exactly indices strictly after `j`.

The current position belongs to neither side, which is essential because triplet indices must satisfy strict inequalities.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [6, 3, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Contribution of one middle

`left[x*2]` is the number of choices for `i`, and `right[x*2]` is the number of choices for `k`. Every left choice can pair with every right choice independently, so multiplication counts all and only triplets with this middle.

After adding the contribution, `left[x]` increments, making the current position available as a left endpoint for later middles.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `left[x*2]` is the number of choices for `i`, and `right[x*2... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why update order handles zero

When `x=0`, target `2x` is also zero. If the current zero remained in `right` during counting, it would be incorrectly available as its own `k` endpoint.

Decrementing `right[x]` first excludes it. Incrementing `left[x]` only after counting prevents it from serving as its own `i` endpoint. The same ordering is correct for every value and particularly visible for zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [6, 3, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Triple enumeration:** Checking all index tripl:** - **Triple enumeration:** Checking all index triples costs `O(n^3)` and ignores the fixed-middle counting structure.
- **Position lists plus binary search:** Store indices per value and count positions on each side in `O(\log n)` per middle, yielding `O(n\log n)`.
- **One total map plus prefix counts:** Right count can be derived as total minus processed occurrences, but the explicit two-map invariant is easy to verify.
- **All zeros:** Each middle contributes zeros-left times zeros-right, summing to `\binom{n}{3}` modulo the modulus.
- **Current value equals target:** This happens only for zero under nonnegative values, and the update ordering excludes the current index.
- **No doubled value:** Counter lookup returns zero and contributes nothing.
- **Repeated endpoints:** Distinct occurrences represent distinct index choices and are correctly multiplied.
- **Boundary positions:** First and last positions have an empty side and therefore cannot be a valid middle.
- **Large answer:** Modulo is applied after each contribution.
- **Counter missing keys:** Access returns zero rather than requiring membership branches.
- **Input preservation:** Only counts change; `nums` remains untouched.
- **Value bound:** Doubling can produce up to `2\cdot10^5`, and Counter lookups support absent larger keys without array bounds.
- **Strict order:** Moving the current item from right to left around its contribution enforces `i<j<k` exactly.
- **Multiplication principle:** Left and right endpoint selections do not constrain one another after the middle is fixed. Choosing one occurrence on the left never removes or changes a right occurrence, so multiplying counts is exact rather than an approximation.
- **Why values, not positions, belong in the maps:** Position order is already encoded by when an occurrence moves between `right` and `left`. The maps need only aggregate equal values within each side; storing complete index lists would duplicate information the scan already provides.
- **Modulo placement:** Reducing the product before adding and reducing the sum afterward is algebraically equivalent to reducing the complete integer answer once. It also prevents a language with bounded integers from accumulating an unnecessarily large intermediate, even though Python itself would remain safe.
- **One pass after initialization:** The only preliminary work is the complete `right` count. No second positional preprocessing is hidden; every occurrence crosses from the future map to the past map exactly once during the main loop.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Constructing `right` takes `O(n)` time. The scan performs expected constant-time Counter operations per element, so total expected time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
