# Guided Example: Find Xor-Beauty of Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`.

The objective is to compute `5` from `{"nums": [1, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The enormous triplet XOR collapses bit by bit

There are $n^3$ ordered triplets, so direct enumeration is impossible for $n=10^5$.

Bitwise OR, AND, and XOR act independently at every bit position. Analyze one bit and determine whether it appears an odd number of times among all effective values. XOR sets that result bit exactly when the count is odd.

The analysis will show that this parity is the same as the parity of that bit among the input numbers. That means the complete answer is simply the XOR of all elements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count input ones at one bit

Fix a bit position. Let:

- $c$ be the number of array elements whose bit is one;
- $z=n-c$ be the number whose bit is zero.

For effective value

$$
(\texttt{nums}[i]\mathbin{|}\texttt{nums}[j])
\mathbin{\&}\texttt{nums}[k],
$$

the chosen bit is one under two requirements:

1. `nums[k]` has the bit, giving $c$ choices for `k`;
2. at least one of `nums[i]` or `nums[j]` has the bit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Fix a bit position.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count ordered `(i,j)` pairs whose OR bit is one

There are $n^2$ ordered pairs in total. Their OR bit is zero only when both selected elements have zero at that bit, giving $z^2$ pairs.

Thus the number whose OR bit is one is

$$
n^2-z^2
=(n-z)(n+z)
=c(2n-c).
$$

Multiplying by the $c$ valid choices of `k`, the result bit appears in

$$
c^2(2n-c)
$$

effective values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate triplets:** It costs $O(n^3)$ and is:** - **Enumerate triplets:** It costs $O(n^3)$ and is infeasible.
- **Explicit per-bit counting:** Count ones at each bit and apply the parity proof; it costs $O(nB)$ for bit width $B$ but is unnecessary once the identity is known.
- **Single element:** The sole effective triplet reduces to that element, matching its XOR.
- **Duplicate values:** XOR parity naturally cancels even multiplicities.
- **Repeated triplet indices:** They are included in the $n^3$ ordered domain.
- **All values equal with even `n`:** Their input XOR is zero, so xor-beauty is zero.
- **All values equal with odd `n`:** One copy remains under XOR.
- **Non-empty guarantee:** It makes `reduce` valid without an initializer.
- **Bit independence:** OR, AND, and XOR can be analyzed separately at every position.
- **Positive inputs:** No sign-extension behavior needs consideration.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. `reduce` visits all $n$ values once and performs one constant-time XOR per additional element. Time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
