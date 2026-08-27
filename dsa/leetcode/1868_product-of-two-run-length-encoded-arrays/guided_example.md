# Guided Example: Product of Two Run-Length Encoded Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"encoded1": [[1, 3], [2, 3]], "encoded2": [[6, 3], [3, 3]]}`
- **Required output:** `[[6, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

**Run-length encoding** is a compression algorithm that allows for an integer array `nums` with many segments of **consecutive repeated** numbers to be represented by a (generally smaller) 2D array `encoded`. Each $\text{encoded}[i] = [\text{val}_{i}, \text{freq}_{i}]$ describes the $$i^{\text{th}}$$ segment of repeated numbers in `nums` where $\text{val}_{i}$ is the value that is repeated $\text{freq}_{i}$ times.

The objective is to compute `[[6, 6]]` from `{"encoded1": [[1, 3], [2, 3]], "encoded2": [[6, 3], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Intersect runs instead of expanding them.** At any expanded position, the product is determined by the currently active run from `encoded1` and the currently active run from `encoded2`. If those runs have remaining frequencies `f1` and `f2`, their values overlap for exactly `min(f1, f2)` positions. That entire block has one product value and can be emitted at once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"encoded1": [[1, 3], [2, 3]], "encoded2": [[6, 3], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution iterates each first encoding run `[vi, fi]`. `fi` is unpacked into a local integer, so reducing it does not modify `encoded1`. Pointer `j` identifies the current second-array run.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution iterates each first encoding run `[vi, fi]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Consume the current overlap.** While local `fi` is positive:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[6, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"encoded1": [[1, 3], [2, 3]], "encoded2": [[6, 3], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[6, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Expand both arrays:** It is conceptually simpl:** - **Expand both arrays:** It is conceptually simple but can require memory and time proportional to enormous expanded length.
- **Copy second frequencies first:** This preserves `encoded2` while retaining the same algorithm and asymptotic bounds.
- **One run versus many:** The while loop naturally intersects the single long run with each shorter opposing run.
- **Both runs end together:** Both remaining frequencies reach zero; the outer loop and `j` advance consistently.
- **Equal adjacent products from different factors:** Immediate merging is required for minimum-length encoding.
- **Single expanded position:** One overlap emits one run with frequency one.
- **Unequal run counts:** Complexity depends on total run boundaries, not on counts being equal.
- **Equal expanded lengths:** This guarantee prevents `j` from running past the second encoding before the first finishes.
- **Positive frequencies:** Every overlap length is positive, ensuring loop progress.
- **Large products:** Values reach at most the product of source bounds and fit safely in Python integers.
- **Input mutation:** Every consumed `encoded2` frequency is reduced in place, usually to zero.
- **First input preservation:** Unpacked `fi` changes locally and leaves `encoded1` intact.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + N)$. Let `M` and `N` be the numbers of runs in the two encodings. Every overlap iteration exhausts at least one current run. Thus there are at most `M + N - 1` overlaps, giving `O(M + N)` time.
- **Auxiliary Space Complexity:** $O(M + N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
