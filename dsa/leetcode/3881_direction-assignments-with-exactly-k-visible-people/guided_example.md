# Guided Example: Direction Assignments with Exactly K Visible People

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "pos": 1, "k": 0}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three integers `n`, `pos`, and `k`.

The objective is to compute `2` from `{"n": 3, "pos": 1, "k": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate people by which side of the observer they occupy

There are

$$
l=\texttt{pos}
$$

people to the observer's left and

$$
r=n-\texttt{pos}-1
$$

people to the right.

A left-side person is visible exactly when choosing `'L'`. A right-side person is visible exactly when choosing `'R'`. The observer's own direction never changes visibility.

Suppose exactly `a` visible people are selected from the left. Then exactly

$$
b=k-a
$$

must be selected from the right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "pos": 1, "k": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose visible subsets; all other directions are forced

There are

$$
\binom la
$$

ways to choose which left-side people are visible. Once chosen, their directions are forced to `'L'`, while every unchosen left-side person must choose `'R'` to remain invisible.

Similarly, there are

$$
\binom rb
$$

ways to choose the visible right-side people. Chosen people must face `'R'` and unchosen people must face `'L'`.

Thus a fixed feasible split `(a,b)` gives

$$
\binom la\binom rb
$$

assignments for everyone except the observer.

The observer may independently choose either direction, doubling every count:

$$
2\binom la\binom rb.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate every feasible visibility split

The source loops

`a = 0,1,\ldots,min(k,l)`.

This ensures `a` is nonnegative, does not exceed the number of left people, and does not exceed the total required visible count. It computes `b=k-a`, which is automatically nonnegative, and includes the term only when `b<=r`.

Every assignment with exactly `k` visible people has one unique value of `a`, the number visible on the left. Different loop iterations therefore represent disjoint assignment sets. Summing all feasible terms counts every valid direction assignment once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "pos": 1, "k": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use Vandermonde directly:** Return `2*C(n-1,k)`. This is simpler, independent of `pos`, and constant-time per query after factorial preprocessing.
- **Enumerate all direction strings:** There are `2^n` assignments and is infeasible.
- **Dynamic programming by people and visible count:** Correct in `O(nk)` time but unnecessary because each visible subset uniquely fixes directions.
- **Pascal-triangle combinations:** Avoid modular inverses but requires `O(nk)` preprocessing or space.
- **Efficient inverse-factorial table:** Compute `g[N-1]` once, then use `g[i-1]=g[i]\cdot i\bmod MOD` while descending. This replaces 100,000 exponentiations with one.
- **Observer direction:** Always contributes a factor of two, including when there are no other people.
- **Observer at an endpoint:** One side count is zero; the loop naturally forces all visible people to come from the other side.
- **`k=0`:** Every non-observer's direction is forced invisible, while the observer remains free, yielding two.
- **`k=n-1`:** Every non-observer is forced visible, again with two observer choices.
- **Invalid split:** `b>r` is skipped; `b<0` cannot occur because `a\le k`.
- **Modulo arithmetic:** Reduce the sum because the number of assignments may be large.
- **Position independence:** Though side-specific directions differ, the total count is always `2\binom{n-1}{k}`.
- **Global source cost:** Do not describe the exact file as truly constant-space without stating that it allocates two large shared arrays.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. After preprocessing, the method loop has at most `min(k,l)+1\le n` iterations. Each combination lookup and modular arithmetic operation is constant time, so per-call time is `O(n)` and extra per-call space is `O(1)`. This matches the manifest if shared precomputed tables are excluded.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
