# Guided Example: Count the Number of Good Subsequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabb"}`
- **Required output:** `11`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **subsequence** of a string is good if it is not empty and the frequency of each one of its characters is the same.

The objective is to compute `11` from `{"s": "aabb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Group good subsequences by their common frequency

In a good non-empty subsequence, choose some non-empty set of distinct character values. Every chosen character must appear the same positive number `i` of times.

The common frequency `i` is unique for that subsequence. The method iterates `i` from one through the maximum frequency present in `s` and counts all good subsequences having exactly that common frequency.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose occurrences by index

Suppose character `c` occurs `v` times in the original string. To include `c` with frequency `i`, choose any `i` of those `v` occurrence indices:

$$
\binom vi
$$

choices.

Once indices are chosen, their order in the subsequence is forced by their original string positions. There is no additional permutation factor.

If `v<i`, that character cannot participate at this common frequency.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Include or exclude each character independently

For a character with `v>=i`:

- exclude it: one choice;
- include it by choosing `i` occurrences: $\binom vi$ choices.

That gives $\binom vi+1$ choices.

Choices for different character values are independent, so multiplying these quantities counts every selection of characters and occurrence indices.

Characters with `v<i` contribute only the forced exclude choice one, so the source simply skips them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `11` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `11` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Backward inverse-factorial fill:** Compute one inverse at `N-1` and derive the rest in $O(N)$ preprocessing.
- **All characters distinct:** Only common frequency one contributes, producing $2^n-1$ non-empty subsequences.
- **One repeated character:** Every non-empty choice of its occurrences is good.
- **Character frequency below `i`:** It must be excluded for that iteration.
- **Empty selection:** Subtract exactly one from each frequency product.
- **Indexed occurrences:** Binomial coefficients count different position choices.
- **Unique common frequency:** It prevents cross-iteration double counting.
- **Modulo inverse:** It is valid because factorial factors are below the prime modulus.
- **Maximum table index:** 10,000 fits inside arrays of length 10,001.
- **Global cost:** Exact preprocessing uses repeated `pow` calls.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert s\rvert$, $F$ be the maximum character frequency, and $A\le26$ the number of distinct lowercase characters. The method loops through $F$ frequencies and at most $A$ counts, taking $O(AF)=O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
