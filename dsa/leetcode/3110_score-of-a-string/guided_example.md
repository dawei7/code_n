# Guided Example: Score of a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "hello"}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the **ASCII** values of adjacent characters.

The objective is to compute `13` from `{"s": "hello"}` while avoiding redundant calculations and unnecessary overhead.

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

**The score is a sum over adjacent edges of the string.** For a string of length $n$, the relevant pairs are positions $(0,1),(1,2),\ldots,(n-2,n-1)$. There are exactly $n-1$ pairs. Each pair contributes the absolute difference between the numeric character codes of its two letters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "hello"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source expresses the complete computation in one return statement:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`sum(abs(a - b) for a, b in pairwise(map(ord, s)))`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "hello"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Index loop:** Iterate `i` from zero through `len(s)-2` and add `abs(ord(s[i]) - ord(s[i+1]))`. It is equally correct and may be easier for beginners to debug.
- **List of codes:** Precompute `[ord(c) for c in s]`, but that uses $O(n)$ extra space without improving time.
- **Alphabet positions:** Subtracting `ord("a")` from both characters gives the same differences because the common offset cancels.
- **Minimum length two:** The contract guarantees at least one adjacent pair.
- **Equal adjacent letters:** Contribution is zero.
- **Increasing pair:** Absolute value returns the positive upward gap.
- **Decreasing pair:** Absolute value removes the negative sign.
- **Alternating extremes:** A string such as `"azaz"` gives the largest contribution 25 at every boundary.
- **ASCII versus Unicode:** For lowercase English letters, `ord` returns the ASCII values required by the task.
- **No input mutation:** Iterators only read `s`.
- **Lazy map:** Character codes are produced on demand, not stored.
- **Lazy pairwise:** Only two neighboring codes need to be retained.
- **Empty generator concern:** Not relevant because length is at least two; even for a shorter input, `sum` would safely return zero.
- **Numeric result:** The method returns an integer, not the transformed characters or individual differences.
- **Every pair exactly once:** Overlapping adjacency is intentional and does not double-count an index pair.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each of the $n$ characters is converted once, and each of the $n-1$ adjacent pairs is processed once. Every conversion, subtraction, absolute value, and addition is constant time for this character range. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
