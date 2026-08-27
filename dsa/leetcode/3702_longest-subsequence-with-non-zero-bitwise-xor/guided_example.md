# Guided Example: Longest Subsequence With Non-Zero Bitwise XOR

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Computing the complete-array XOR

The loop begins with `xor = 0` and applies:

`xor ^= x`

for every element. Zero is the identity for XOR, so the final value is:

$$
\texttt{nums}[0]\mathbin{\mathrm{XOR}}\texttt{nums}[1]
\mathbin{\mathrm{XOR}}\cdots
\mathbin{\mathrm{XOR}}\texttt{nums}[n-1].
$$

At the same time:

`cnt0 += int(x == 0)`

adds one exactly for a zero element. The Boolean comparison is converted to integer one or zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Case one: the whole array already works

If the complete XOR is nonzero, the entire array is a valid subsequence. Its length is $n$, and no subsequence can be longer than the original array.

Therefore:

`if xor:`

`    return n`

is immediately optimal.

For `nums = [2, 3, 4]`, the full XOR is:

$$
2\mathbin{\mathrm{XOR}}3\mathbin{\mathrm{XOR}}4=5,
$$

so all three elements are kept.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the complete XOR is nonzero, the entire array is a valid ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case two: every element is zero

Suppose `xor == 0` and `cnt0 == n`. Every array value is zero.

The XOR of any nonempty subsequence of zeros is zero, and the empty subsequence also has XOR zero. No qualifying subsequence exists, so the required result is zero.

This is the only situation in which no nonzero-XOR subsequence exists. Any nonzero element by itself would form a valid length-one subsequence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming over reachable XORs:** Tra:** - **Dynamic programming over reachable XORs:** Tracking the best length for every XOR value is unnecessary and could use enormous time and space. The full-XOR removal identity yields a three-case solution.
- **Try removing every element:** Recomputing or testing $n$ candidate subsequences is avoidable. When total XOR is zero, removing any nonzero element is guaranteed to work.
- **Use only the complete XOR:** A zero total does not distinguish an all-zero array, where no answer exists, from arrays such as `[1,2,3]`, where length $n-1$ works. The zero count supplies that distinction.
- **One nonzero element:** Its full XOR is nonzero, so the answer is one.
- **One zero element:** Every subsequence has XOR zero, so the answer is zero.
- **All zeros:** The method returns zero rather than $n-1$ because removing a zero leaves XOR zero.
- **Total XOR zero with some zeros:** Remove a nonzero occurrence, not necessarily a zero; the remaining XOR equals that removed nonzero value.
- **Duplicate nonzero values:** The argument uses occurrences, and removing one occurrence still applies `T XOR x`.
- **Empty subsequence:** Its XOR is conventionally zero and does not qualify, so it cannot rescue the all-zero case.
- **Relative order:** Removing one element from the full array automatically preserves the order of every retained element.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
