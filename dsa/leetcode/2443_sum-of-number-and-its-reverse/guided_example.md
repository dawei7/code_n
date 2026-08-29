# Guided Example: Sum of Number and Its Reverse

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 443}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **non-negative** integer `num`, return `true`* if *`num`* can be expressed as the sum of any **non-negative** integer and its reverse, or *`false`* otherwise.*

The objective is to compute `true` from `{"num": 443}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search every possible first addend

The task asks whether there exists a non-negative integer `k` such that

$$
k + \operatorname{reverse}(k) = \texttt{num}.
$$

Both terms on the left are non-negative. Therefore `k` cannot exceed `num`: if `k > num`, the sum is already greater than `num` even before adding its reversal. Every possible witness lies in the inclusive range from zero through `num`.

The exact solution enumerates that complete range with `range(num + 1)`. For each `k`, it computes `int(str(k)[::-1])` and tests whether the sum equals `num`. Python's `any` returns true as soon as one candidate succeeds; if the generator finishes without a match, it returns false.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 443}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Numeric reversal and leading zeros

Converting `k` to a string exposes its decimal digits, and `[::-1]` reverses their order. Converting back to `int` removes leading zeros from the reversed representation, which is precisely how numeric reversal is defined.

For `k=140`, the reversed string is `"041"`, and `int("041")` is 41. The sum `140+41=181` proves the third example true.

For `k=0`, the conversion sequence remains `"0"` and integer 0. This makes `num=0` work naturally: the first and only necessary candidate satisfies `0+0=0`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the range is both sufficient and necessary

If the method finds a candidate, the computed reversed integer is non-negative and the equality test directly proves that `num` has the required representation.

Conversely, suppose some non-negative witness `w` exists. Because `reverse(w) >= 0`, the equality implies `w <= num`. Thus `w` appears in the enumerated range. When the generator reaches it, the string reversal computes its numeric reverse and the equality becomes true. The method cannot miss any valid witness.

These two directions establish exact correctness. No mathematical characterization of reversible sums is needed because the constraint `num <= 10^5` makes complete enumeration practical.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 443}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Arithmetic digit reversal:** Compute the reverse with modulo and integer division rather than strings. It has the same asymptotic bounds and may avoid allocation.
- **Digit dynamic programming:** Model addition from both ends with carries to decide existence without enumerating every `k`. This can improve dependence on `num` but is considerably more complex for the small bound.
- **Precompute all sums:** For many queries, one could generate `k + reverse(k)` values once and store them in a set. For one call, that uses unnecessary memory.
- **`num=0`:** Candidate zero works, so the answer is true.
- **Single-digit target:** Reversing a single-digit `k` leaves it unchanged, so only even targets can be represented as `2k` within that range.
- **Trailing zeros in `k`:** They disappear as leading zeros after reversal, as in `140 -> 041 -> 41`.
- **false result:** `any` must exhaust the entire complete candidate range before returning false.
- **Multiple witnesses:** Only the first encountered match matters because the result is Boolean.
- **Upper search bound:** No `k > num` can work because both addends are non-negative.
- **String conversion:** The exact source uses decimal strings, so its temporary-space cost depends on digit count rather than being strictly constant for unbounded integers.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log(N+1)$. Let $N=\texttt{num}$ and let $D=O(\log(N+1))$ be its decimal digit count. There are at most $N+1$ candidates. Converting a candidate to a string, reversing it, and parsing it takes $O(D)$ worst-case time. Therefore worst-case time is $O(N\log(N+1))$, matching the manifest's `O(num log num)` intent while remaining well-defined at zero.
- **Auxiliary Space Complexity:** $O(\log(N+1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
