# Guided Example: Factorial Generator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5}`
- **Required output:** `[1, 2, 6, 24, 120]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a generator function that takes an integer `n` as an argument and returns a generator object which yields the **factorial sequence**.

The objective is to compute `[1, 2, 6, 24, 120]` from `{"n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

**What the generator must yield.** For a positive input `n`, successive calls to the returned generator should produce $1!, 2!, \ldots, n!$. For `n = 0`, it should produce the single conventional value $0! = 1$. A generator is important here: values are delivered lazily through `next()` rather than collected and returned in an array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Keep the product accumulated so far.** The variable `product` begins at one, the multiplicative identity. The loop variable `value` begins at one and rises by one on each iteration. Before yielding during iteration $v$, the method executes `product *= value`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

At the start of iteration $v$, `product` equals $(v-1)!$. Multiplying by $v$ changes it to $v!$, which is then yielded. This is the loop invariant that explains both correctness and efficiency: each factorial reuses the previous factorial instead of recomputing the full product from one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 6, 24, 120]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 6, 24, 120]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recompute every factorial independently:** For each $i$, multiply one through $i$. This performs $1+2+\cdots+n=O(n^2)$ multiplications and throws away useful previous work.
- **Return an array:** An eager loop can fill and return all factorials in $O(n)$ time, but it always performs all work and stores $O(n)$ values even if the caller needs only a prefix.
- **Recursive generator:** Recursion can produce the sequence, but it adds call-stack state and is less direct than retaining one running product.
- **Use `BigInt`:** This is required if the supported range extends beyond safe Number factorials. Every operand and expected output would then need consistent BigInt semantics.
- **Input zero:** `Math.max(0, 1)` causes exactly one yield of one, satisfying $0! = 1$.
- **Input one:** The loop also yields exactly one value, one. Although zero and one produce equal sequences of values, both contracts are correct.
- **Maximum input eighteen:** All produced factorials remain exact safe integers, including the final $18!$.
- **Partial consumption:** If the caller stops requesting values, no later multiplications occur. This is the principal benefit of the generator form.
- **Repeated `next()` after completion:** The generator remains completed and returns no new values.
- **Independent iterators:** Two calls to `factorial(n)` do not share `product`; each generator maintains its own progress.
- **Invalid negative input outside the contract:** `Math.max(n, 1)` would still yield one, which is not a defined negative factorial sequence. The constraints are what make the compact bound valid.
- **Non-integer input outside the contract:** The loop would yield factorial-like prefix products through the last integer not exceeding the bound, not a gamma-function value. Only integer `n` is supported.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. For one call to `next()` that reaches a yield, the generator performs one multiplication, one loop comparison, and constant state updates. Under the bounded Number representation, this is $O(1)$ time per emitted value. This is the perspective captured by the manifest's constant-time claim.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
