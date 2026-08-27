# Guided Example: Single Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 2, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

The objective is to compute `1` from `{"nums": [2, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the frequency guarantee, not a frequency table

The array has a very strong structure: exactly one value occurs once, and every other value occurs exactly twice. The required constant extra space rules out storing counts or a set proportional to the input.

Bitwise exclusive OR, written XOR, is designed for this cancellation pattern. For one bit, its result is one exactly when the two input bits differ:

| First bit | Second bit | XOR |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Applying that operation independently to every bit gives several useful integer identities:

$$
x \mathbin{\oplus} x = 0
$$

$$
x \mathbin{\oplus} 0 = x
$$

XOR is also associative and commutative. Associativity allows parentheses to move, and commutativity allows operands to be reordered. Therefore, equal values can be brought together conceptually even when their occurrences are far apart in the array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `reduce(xor, nums)` computes

`reduce` takes the first two elements, combines them with `xor`, combines that result with the third element, and continues until one accumulator remains. For `[4, 1, 2, 1, 2]`, the effective expression is:

$$
4 \mathbin{\oplus} 1 \mathbin{\oplus} 2
\mathbin{\oplus} 1 \mathbin{\oplus} 2.
$$

By reordering and regrouping for reasoning, this equals:

$$
4 \mathbin{\oplus}
(1 \mathbin{\oplus} 1)
\mathbin{\oplus}
(2 \mathbin{\oplus} 2).
$$

Each pair becomes zero, leaving:

$$
4 \mathbin{\oplus} 0 \mathbin{\oplus} 0 = 4.
$$

The actual implementation does not sort or rearrange the array. Those algebraic properties merely prove that the left-to-right reduction has the same result as the pair-grouped expression.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `reduce` takes the first two elements, combines them with `x... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the remaining value is exactly the answer

Let the unique value be $u$, and let the repeated values be $p_1,p_2,\ldots,p_k$. The reduction contains:

$$
u
\mathbin{\oplus}
p_1 \mathbin{\oplus} p_1
\mathbin{\oplus}\cdots\mathbin{\oplus}
p_k \mathbin{\oplus} p_k.
$$

Every repeated pair contributes zero. XORing any number of zeros with $u$ leaves $u$. Thus the returned accumulator is the value that appears once.

This is not merely detecting oddness of the array length. The result follows from the exact multiplicity guarantee. If another value occurred three times, two copies would cancel and one would remain in the XOR too, so the method would no longer identify a uniquely specified element.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Hash set toggling:** Add an unseen value and r:** - **Hash set toggling:** Add an unseen value and remove a seen value. The final set contains the answer, but it requires $O(n)$ extra space.
- **Frequency dictionary:** Count occurrences and return the key with count one. It is linear expected time but violates the constant-space requirement.
- **Sort then scan pairs:** Equal values become adjacent, making the singleton easy to find. It costs $O(n\log n)$ time and may use extra sorting memory or mutate the input.
- **Arithmetic with a set:** Compute twice the sum of distinct values minus the full sum. It uses $O(n)$ set space and can overflow in fixed-width languages.
- **One element:** `reduce` returns that element without calling `xor`.
- **Unique value is zero:** All duplicate pairs cancel to zero, and the remaining zero is correctly returned.
- **Negative values:** Identical negative integers cancel exactly under bitwise XOR.
- **Arbitrary ordering:** Pair occurrences need not be adjacent because XOR is associative and commutative.
- **Malformed multiplicities:** The proof depends on every non-answer appearing exactly twice; the function does not validate that promise.
- **Runtime dependencies:** The selected source uses `List`, `reduce`, and `xor` without imports. Standalone Python needs `from typing import List`, `from functools import reduce`, and `from operator import xor`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
