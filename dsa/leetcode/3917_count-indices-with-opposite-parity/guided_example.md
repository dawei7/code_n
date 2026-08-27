# Guided Example: Count Indices With Opposite Parity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `[2, 1, 1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `[2, 1, 1, 0]` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encoding parity as zero or one

For an integer $x$:

$$
x\mathbin{\&}1
=
\begin{cases}
0,&x\text{ is even},\\
1,&x\text{ is odd}.
\end{cases}
$$

The two-element list `cnt` uses that bit directly as an index:

- `cnt[0]` is the number of even values;
- `cnt[1]` is the number of odd values.

The first loop visits every `x` and increments `cnt[x & 1]`. At its end, the list describes the whole array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Converting whole-array counts into suffix counts

At the beginning of forward iteration $i$, the counters still include `nums[i]` and every value to its right, while earlier values have already been removed.

The source first executes



After this decrement, `cnt` contains exactly the values at indices $j>i$:

$$
\texttt{cnt}[0]
=
\#\{j>i:\texttt{nums}[j]\text{ is even}\},
$$

$$
\texttt{cnt}[1]
=
\#\{j>i:\texttt{nums}[j]\text{ is odd}\}.
$$

This order matters. Reading the opposite count first would not change the numerical answer for the current value—because the current value belongs to its own parity rather than the opposite one—but decrementing first establishes the clean strict-suffix invariant and makes the reasoning direct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the beginning of forward iteration $i$, the counters stil... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Selecting the opposite count

XOR with one flips a parity bit:

$$
0\mathbin{\hat{}}1=1,
\qquad
1\mathbin{\hat{}}1=0.
$$

The source reads



Python evaluates `&` before `^`, so this is



For a current even value, the expression selects `cnt[1]`, the number of odd suffix values. For a current odd value, it selects `cnt[0]`, the number of even suffix values.

Every one of those suffix values has opposite parity, and no same-parity value is included. That count is exactly `ans[i]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Right-to-left scan:** Start both counts at zer:** - **Right-to-left scan:** Start both counts at zero, answer from the opposite count, then add the current value. This matches the manifest summary and has the same bounds.
- **Quadratic pair checking:** Testing every $i,j$ pair costs $O(N^2)$ and stores no useful reusable suffix summary.
- **Suffix parity arrays:** Precomputing even and odd counts for every suffix works in $O(N)$ time but uses $O(N)$ extra storage instead of two mutable totals.
- **Single element:** Removing it leaves both counters zero, so its score is zero.
- **All values even:** The odd counter is always zero, and every score is zero.
- **All values odd:** The even counter is always zero, and every score is zero.
- **Alternating parity:** Scores decrease according to how many opposite-class positions remain, and the counters track them exactly.
- **Repeated values:** Magnitude and distinctness are irrelevant; each index contributes one occurrence to its parity count.
- **Last index:** Its decrement empties the represented suffix, so its answer is always zero.
- **Expression precedence:** The source relies on `&` binding before `^`; explicit parentheses would improve readability without changing behavior.
- **Positive-value constraint:** The low-bit parity test also works for zero and Python negative integers, though only positive values are required.
- **Manifest/source traversal difference:** Both directions are linear, but the explanation follows the actual left-to-right decrement strategy.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{nums}\rvert$. The source makes one pass to count total parity frequencies and one pass to produce scores. Each pass performs constant work per element.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
