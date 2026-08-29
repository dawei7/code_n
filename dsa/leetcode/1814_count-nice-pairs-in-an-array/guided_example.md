# Guided Example: Count Nice Pairs in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [42, 11, 1, 97]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` that consists of non-negative integers. Let us define `rev(x)` as the reverse of the non-negative integer `x`. For example, $rev(123) = 321$, and $rev(120) = 21$. A pair of indices `(i, j)` is **nice** if it satisfies all of the following conditions:

The objective is to compute `2` from `{"nums": [42, 11, 1, 97]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rearrange the pair equation into one per-number signature

A pair $(i,j)$ is nice when

$$
\texttt{nums}[i]+\operatorname{rev}(\texttt{nums}[j])
=
\texttt{nums}[j]+\operatorname{rev}(\texttt{nums}[i]).
$$

Move each number's own reverse to the same side:

$$
\texttt{nums}[i]-\operatorname{rev}(\texttt{nums}[i])
=
\texttt{nums}[j]-\operatorname{rev}(\texttt{nums}[j]).
$$

Define the signature

$$
f(x)=x-\operatorname{rev}(x).
$$

Then a pair is nice exactly when both values have the same signature. The original two-index equation has become an equality-group counting problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [42, 11, 1, 97]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse a nonnegative integer numerically

Helper `rev(x)` starts `y = 0`. While `x` is nonzero:

1. `x % 10` extracts its final digit;
2. `y = y * 10 + digit` appends that digit to the reversed value;
3. `x //= 10` removes the processed digit.

For 120, the steps build 0, then 2, then 21. The leading zero that would appear in textual `"021"` contributes no numerical value, so returning 21 matches the definition.

For input zero, the loop runs zero times and returns zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count how many numbers share each signature

The generator `x - rev(x) for x in nums` computes one signature per array position. `Counter` maps every signature to its occurrence count.

Signatures may be negative. For example, a number whose reverse is larger produces a negative difference. Hash-map keys handle positive, zero, and negative integers uniformly.

Only signature equality matters; two different original values can and often do share one key.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [42, 11, 1, 97]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Streaming hash count:** Add the previous frequency before incrementing each signature. It avoids a separate final combination pass but has the same bounds.
- **Check every pair:** Direct equation testing costs $O(n^2)$ and is too slow.
- **Sort signatures:** Equal runs can be counted after $O(n\log n)$ sorting, slower than expected-linear hashing.
- **String reversal:** Converting to text is valid but numeric reversal makes dropped trailing zeros explicit.
- **Input zero:** Its reverse and signature are both zero.
- **Trailing zeros:** They disappear from the reversed numerical value, as required.
- **Palindromic number:** Its signature is zero and it pairs nicely with every other zero-signature value.
- **Negative signature:** It is a normal Counter key and needs no special handling.
- **All signatures distinct:** Every group size is one and contributes zero.
- **All signatures equal:** The answer before modulo is $n(n-1)/2$.
- **Duplicate input values:** They necessarily share a signature and their distinct indices form pairs.
- **Modulo timing:** Applying it once at the end is safe in Python.
- **Index order:** Each unordered combination corresponds to exactly one ordered condition $i<j$.
- **Input preservation:** The helper consumes only its local copy of each integer; `nums` is unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T+n)$. Let $n$ be the array length and let
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
