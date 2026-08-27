# Guided Example: Find the Number of Copy Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"original": [1, 2, 3, 4], "bounds": [[1, 2], [2, 3], [3, 4], [4, 5]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `original` of length `n` and a 2D array `bounds` of length `n x 2`, where $\text{bounds}[i] = [u_{i}, v_{i}]$.

The objective is to compute `2` from `{"original": [1, 2, 3, 4], "bounds": [[1, 2], [2, 3], [3, 4], [4, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Equal adjacent differences force one global shift.** The condition

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"original": [1, 2, 3, 4], "bounds": [[1, 2], [2, 3], [3, 4], [4, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\texttt{copy}[i]-\texttt{copy}[i-1]
=
\texttt{original}[i]-\texttt{original}[i-1]
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | $$
\texttt{copy}[i]-\texttt{copy}[i-1]
=
\texttt{original}[i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

$$
\texttt{copy}[i]-\texttt{original}[i]
=
\texttt{copy}[i-1]-\texttt{original}[i-1].
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"original": [1, 2, 3, 4], "bounds": [[1, 2], [2, 3], [3, 4], [4, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming over possible copied value:** - **Dynamic programming over possible copied values:** Bounds can span up to $10^9$, making value-by-value states infeasible and unnecessary.
- **Construct each candidate array:** There may be up to a billion possible first values, while interval intersection counts all of them at once.
- **Track the global shift \(c\) instead of the first value:** This is equally valid; each bound becomes `bounds[i][0] - original[i] <= c <= bounds[i][1] - original[i]`.
- **Use only the tightest original bound width:** Offsets move intervals relative to one another, so their full translated intersection is required.
- **Empty intersection:** When `lower > upper`, no first value satisfies all indices and the source correctly returns zero.
- **Single remaining integer:** When `lower == upper`, exactly one complete copy array is forced.
- **Negative offsets:** A decreasing portion of `original` produces negative offsets; subtracting them correctly shifts the allowable first-value interval upward.
- **Large positive offsets:** Later upper bounds may force `upper` downward and eliminate otherwise plausible first values.
- **Repeated original values:** Their offset from `base` can be equal, but each position still contributes its own independent bound restriction.
- **Inclusive endpoints:** The `+1` is necessary because both lower and upper bound values are allowed.
- **No input mutation:** The method derives scalar restrictions and leaves `original` and `bounds` unchanged.
- **Early exit opportunity:** The code could return zero as soon as `lower > upper`, but continuing the linear scan does not change correctness or asymptotic complexity.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `original`. The source scans indices one through $n-1$ once, performing constant-time arithmetic and interval updates per index. Time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
