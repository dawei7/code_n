# Guided Example: Construct the Minimum Bitwise Array I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 5, 7]}`
- **Required output:** `[-1, 1, 4, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` consisting of `n` prime integers.

The objective is to compute `[-1, 1, 4, 3]` from `{"nums": [2, 3, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

**Understand what increment does to binary bits.** When a nonnegative integer $a$ is incremented, all trailing one-bits become zero, and the first zero-bit immediately above them becomes one. Taking `a | (a + 1)` keeps the original trailing ones from $a$ and also keeps the newly set bit from $a+1$. All higher bits are unchanged. The result is therefore $a$ with its lowest zero-bit changed to one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

We are given the result $x$ and want the smallest $a$ producing it. Every odd prime has at least one trailing one-bit. Suppose the trailing run of ones in $x$ has length $t\ge1$: bits $0$ through $t-1$ are one, and bit $t$ is zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | We are given the result $x$ and want the smallest $a$ produc... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Any valid predecessor can be formed by clearing one bit among that trailing run. If bit $p<t$ is cleared, then it becomes the lowest zero in $a$. Incrementing $a$ sets it and clears the lower ones, while OR with the original $a$ restores those lower ones, reproducing $x$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-1, 1, 4, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-1, 1, 4, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Brute-force predecessors:** Test every $a<x$ a:** - **Brute-force predecessors:** Test every $a<x$ and stop at the first satisfying OR. It is easy under tiny limits but costs $O(nM)$ time.
- **Trailing-one loop with a mask:** Repeatedly test `x & d` while doubling `d`, retaining `x - d` as the latest candidate. This is the editorial's equivalent formulation.
- **Direct bit trick:** The boundary can be derived from low-bit operations, but the explicit scan is easier to reason about and already logarithmic.
- **Prime two:** It is the sole even prime and impossible because `a | (a + 1)` is always odd.
- **Prime three:** Binary `11` has first zero at bit two; clearing bit one produces one, and `1 | 2 = 3`.
- **Long trailing run:** Clearing the highest one in the run, not the lowest, produces the smallest predecessor.
- **A single trailing one:** For values such as five, first zero is bit one, so bit zero is cleared and the answer is four.
- **Operator precedence:** Parentheses would improve readability. The intended tests are `(((x >> i) & 1) ^ 1)` and `x ^ (1 << (i - 1))`.
- **Prime guarantee:** The explicit impossibility handling relies on all non-two values being odd. General even composite inputs would also be impossible and would need broader checking.
- **Input preservation:** Results are appended to a new list; `nums` is not modified.
- **Bit-range cap:** Thirty-one tested positions cover the version I limits comfortably. A truly unbounded Python-integer API should loop until a zero rather than hard-code 32.
- **Output order:** Each result is appended during the input scan, so it stays aligned with its original prime.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log M)$. For each of $n$ primes, the source inspects at most $O(\log M)$ bits until the first zero, where $M$ is the maximum value. Total time is $O(n\log M)$. In this exact implementation the loop is capped at 31 iterations, and version I has $M\le1000$, so it is also bounded by a small constant per number.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
