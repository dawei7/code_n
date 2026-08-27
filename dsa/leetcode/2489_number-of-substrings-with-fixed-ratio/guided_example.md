# Guided Example: Number of Substrings With Fixed Ratio

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "0110011", "num1": 1, "num2": 2}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary string `s`, and two integers `num1` and `num2`. `num1` and `num2` are coprime numbers.

The objective is to compute `4` from `{"s": "0110011", "num1": 1, "num2": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert a ratio into an equality

Suppose a substring contains $z$ zeros and $o$ ones. The required ratio is

$$
z:o=\texttt{num1}:\texttt{num2}.
$$

Cross-multiplication avoids division:

$$
z\cdot\texttt{num2}
=
o\cdot\texttt{num1}.
$$

Rearranging gives a zero-valued weighted balance,

$$
o\cdot\texttt{num1}
-
z\cdot\texttt{num2}
=0.
$$

The method assigns each encountered one a contribution of `num1` and each zero a contribution of `-num2`. A substring has the desired ratio exactly when the sum of its contributions is zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "0110011", "num1": 1, "num2": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use prefix scores to describe every substring

After scanning a prefix of `s`, the code has counts `n0` and `n1`. Its score is

`x = n1*num1 - n0*num2`.

Consider two prefix boundaries, an earlier one with score $X_a$ and a later one with score $X_b$. The substring between them has weighted balance $X_b-X_a$, because all contributions before the earlier boundary cancel.

That substring has the fixed ratio exactly when its balance is zero, which is equivalent to $X_b=X_a$. The problem has therefore become: count pairs of prefix boundaries with equal scores.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After scanning a prefix of `s`, the code has counts `n0` and... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The empty prefix is a real boundary

Before reading any characters, both digit counts are zero and the prefix score is zero. The counter starts as `Counter({0:1})` to record this empty prefix.

This initialization is essential for substrings beginning at index zero. If the current prefix itself has the target ratio, its score is zero and `cnt[0]` contributes the empty boundary as its starting point.

For example, with ratio $1:2$, prefix `"011"` has one zero and two ones. Its score is $2\cdot1-1\cdot2=0$, so it matches the empty prefix and is counted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "0110011", "num1": 1, "num2": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct running score:** Update one balance var:** - **Direct running score:** Update one balance variable instead of storing `n0` and `n1`. It uses the same map and proof.
- **Enumerate all substrings:** Maintaining counts for every start still costs $O(n^2)$ time.
- **Normalize every substring with gcd:** It repeats expensive work and is unnecessary because cross-multiplication tests the ratio exactly.
- **Substring beginning at zero:** The preloaded empty-prefix score counts it.
- **Non-empty requirement:** Looking up before inserting the current score prevents pairing a boundary with itself.
- **Many equal scores:** Every earlier occurrence must contribute, so use frequencies rather than a set.
- **All zeros or all ones:** No non-empty substring can meet a ratio with both positive parts, and the answer remains zero.
- **Ratio multiples:** Counts such as $2\cdot\texttt{num1}$ and $2\cdot\texttt{num2}$ are valid.
- **Large answer:** Use an integer type capable of holding a quadratic count.
- **Coprime inputs:** No reduction step is required inside the algorithm.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert s\rvert$. The loop processes each character once. Counter lookup and update take expected $O(1)$ time, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
