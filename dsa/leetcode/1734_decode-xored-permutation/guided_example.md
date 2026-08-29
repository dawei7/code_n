# Guided Example: Decode XORed Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"encoded": [3, 1]}`
- **Required output:** `[1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an integer array `perm` that is a permutation of the first `n` positive integers, where `n` is always **odd**.

The objective is to compute `[1, 2, 3]` from `{"encoded": [3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The adjacent XOR rule can decode once one endpoint is known

The encoding gives

$$
\texttt{encoded}[i]
=
\texttt{perm}[i]\mathbin{\mathrm{XOR}}\texttt{perm}[i+1].
$$

If either adjacent permutation value is known, the other is recovered by XORing the encoding again, because $x\mathbin{\mathrm{XOR}}x=0$.

Unlike the simpler decode problem, this method is not given the first value. It derives the last value from the facts that `perm` contains every integer from one through odd $n$ exactly once.

The hidden length itself is not separately supplied. Because adjacent encoding produces one fewer entry than the original sequence, `n = len(encoded) + 1` recovers it exactly and determines both the numeric permutation range and the output allocation size.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"encoded": [3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: XOR all values in the hidden permutation

`b` begins at zero. The loop from one through `n` computes

$$
b=1\mathbin{\mathrm{XOR}}2\mathbin{\mathrm{XOR}}\cdots
\mathbin{\mathrm{XOR}}n.
$$

Since `perm` is a permutation of those integers, $b$ is also the XOR of every hidden permutation element, regardless of order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use even encoded positions to cover every element except the last

Because $n$ is odd, `encoded` has even length $n-1$. The source XORs encoded indices zero, two, four, and so on:

`for i in range(0, n - 1, 2): a ^= encoded[i]`.

These entries expand to

$$
(\texttt{perm}[0]\mathbin{\mathrm{XOR}}\texttt{perm}[1])
\mathbin{\mathrm{XOR}}
(\texttt{perm}[2]\mathbin{\mathrm{XOR}}\texttt{perm}[3])
\mathbin{\mathrm{XOR}}\cdots.
$$

The pairs are disjoint and cover indices zero through `n-2`. The only hidden value not included is `perm[n-1]`.

Thus `a` is the XOR of every permutation element except the last.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"encoded": [3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Derive the first value instead:** XOR all permutation values with encoded entries at odd indices, then reconstruct forward. It is the symmetric common formulation.
- **Try every possible first value:** Validate each reconstruction as a permutation, but this adds unnecessary quadratic work.
- **Odd length:** It is essential for alternating encoded pairs to cover all but one permutation element.
- **Minimum `n=3`:** One even-indexed encoding pair covers the first two hidden values.
- **Last value equals an earlier numeric XOR result:** Cancellation still works bitwise; values themselves remain distinct by the permutation promise.
- **Encoded zero:** Adjacent permutation values would be equal, which cannot occur in a valid permutation, so valid inputs will not create that contradiction.
- **Backward direction:** The source derives the last value, so it must reconstruct from right to left.
- **Zero initialization:** Placeholder zeros are overwritten before return and are not permutation candidates.
- **Order independence:** XORing one through $n$ equals XORing the permuted sequence.
- **Input validity promise:** No explicit duplicate or range check is performed.
- **Output length:** It is exactly `len(encoded)+1`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the permutation length. XORing alternating encoded entries takes $O(n)$ time, XORing one through $n$ takes $O(n)$, and backward reconstruction takes $O(n)$. Their sum is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
