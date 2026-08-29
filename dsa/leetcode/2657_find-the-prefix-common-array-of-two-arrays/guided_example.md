# Guided Example: Find the Prefix Common Array of Two Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"A": [1, 3, 2, 4], "B": [3, 1, 2, 4]}`
- **Required output:** `[0, 2, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed **integer** **permutations `A` and `B` of length `n`.

The objective is to compute `[0, 2, 3, 4]` from `{"A": [1, 3, 2, 4], "B": [3, 1, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain what each growing prefix has seen

At index $i$, the desired value is:

$$
|\{A[0],\ldots,A[i]\}
\cap
\{B[0],\ldots,B[i]\}|.
$$

The exact solution uses two counters:

- `cnt1` for values in the current prefix of `A`;
- `cnt2` for values in the current prefix of `B`.

Because both arrays are permutations, each frequency is either zero or one. Counters still provide a uniform way to express how much multiplicity the two prefixes share.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"A": [1, 3, 2, 4], "B": [3, 1, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Grow both prefixes together

`zip(A, B)` produces pairs `(A[i], B[i])` in increasing index order. The arrays have equal length, so no value is truncated.

For each pair `(a,b)`:

- increment `cnt1[a]`;
- increment `cnt2[b]`;
- compute the size of their current multiset intersection;
- append it to `ans`.

The count is measured after both current values are inserted, which matches prefixes ending at the current index inclusively.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the minimum of two frequencies measures overlap

For value $x$, the number of copies shared by two multisets is:

$$
\min(\texttt{cnt1[x]},\texttt{cnt2[x]}).
$$

Summing over values seen in the first prefix gives:

`sum(min(v, cnt2[x]) for x, v in cnt1.items())`.

Under the permutation guarantee, this contribution is one exactly when $x$ has appeared in both prefixes and zero otherwise.

Thus the sum is the number of common distinct values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 2, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"A": [1, 3, 2, 4], "B": [3, 1, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 2, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Incremental frequency array:** Update a running common count only when a value has appeared in both prefixes, achieving $O(n)$ time.
- **Two prefix sets and intersection:** Rebuilding `setA & setB` each time is also potentially quadratic.
- **Brute nested search:** Repeated membership scans can become cubic if implemented carelessly.
- **Length one:** The same sole permutation value appears in both, so result is `[1]`.
- **Different first values:** The first answer is zero.
- **Same current value:** It can add one newly common value, not two.
- **Cross-completed values:** Different `a` and `b` can raise the count by two.
- **Final prefix:** Both contain all values from one through $n$, so final answer is $n$.
- **Permutation guarantee:** Counter frequencies never exceed one.
- **Input preservation:** Both arrays are read only.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. At prefix length $i+1$, the exact sum scans $i+1$ keys. Across all prefixes, time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
