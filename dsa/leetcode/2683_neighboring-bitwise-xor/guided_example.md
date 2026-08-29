# Guided Example: Neighboring Bitwise XOR

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"derived": [1, 1, 0]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **0-indexed** array `derived` with length `n` is derived by computing the **bitwise XOR** (⊕) of adjacent values in a **binary array** `original` of length `n`.

The objective is to compute `true` from `{"derived": [1, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Write all circular XOR equations together

For a candidate binary array `original`, the derived values are:

$$
\begin{aligned}
d_0 &= o_0\oplus o_1,\\
d_1 &= o_1\oplus o_2,\\
&\ \vdots\\
d_{n-1} &= o_{n-1}\oplus o_0.
\end{aligned}
$$

The last equation closes the circle. That closure creates one global consistency condition that is enough to answer whether a solution exists.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"derived": [1, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: XOR every equation

XOR is associative and commutative, so all right-hand sides can be rearranged.

Every original bit appears exactly twice:

- once paired with its next neighbor;
- once paired with its previous neighbor.

Because `a ^ a = 0`, each pair cancels. Therefore any valid derived array must satisfy:

$$
d_0\oplus d_1\oplus\cdots\oplus d_{n-1}=0.
$$

This proves that total XOR zero is necessary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the condition is also sufficient

A necessary condition alone would not justify returning true. We must show that total XOR zero lets us construct an original array.

Choose `o_0 = 0`. For each non-final relation, define the next bit by:

$$
o_{i+1}=o_i\oplus d_i.
$$

Because both inputs are binary, every constructed value remains either zero or one. These definitions automatically satisfy the first $n-1$ adjacent equations.

After applying all $n$ derived values around the cycle, the value that should return to the starting position is:

$$
o_0\oplus d_0\oplus d_1\oplus\cdots\oplus d_{n-1}.
$$

When total derived XOR is zero, this equals `o_0`. The circular endpoint is consistent, so all equations, including the last one, are satisfied.

Thus total XOR zero is sufficient as well as necessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"derived": [1, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Reconstruct from initial zero:** Correct in $O(n)$ time but stores an array unnecessarily unless only the current bit is retained.
- **Try both initial bits:** Redundant because the two reconstructions are complements and pass or fail together.
- **Count ones and test even parity:** Equivalent for binary input, using `sum(derived) % 2 == 0`.
- **Nested equation solving:** Adds complexity without improving the one global consistency check.
- **Single zero:** Valid because a bit XOR itself is zero.
- **Single one:** Invalid because no bit XOR itself can be one.
- **All zeros:** Valid; a constant all-zero or all-one original works.
- **Odd number of ones:** Total XOR is one, so no original exists.
- **Even number of ones:** Total XOR is zero, so a construction exists.
- **Nonempty constraint:** Makes `reduce` without an initializer safe.
- **Binary constraint:** Ensures the constructive recurrence always produces binary values.
- **Input preservation:** Reduction only reads the array.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. `reduce` processes all $n$ elements once and performs one constant-time XOR per combination. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
