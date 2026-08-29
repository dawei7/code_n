# Guided Example: Next Greater Numerically Balanced Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1000}`
- **Required output:** `1333`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An integer `x` is **numerically balanced** if for every digit `d` in the number `x`, there are **exactly** `d` occurrences of that digit in `x`.

The objective is to compute `1333` from `{"n": 1000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search candidates in increasing numerical order

The source begins `count(n + 1)`, an unbounded iterator producing `n+1, n+2, n+3, ...`. Starting at `n+1` enforces the word “strictly”: even if `n` itself is numerically balanced, it cannot be returned.

Each candidate is tested independently. The first candidate passing the balance condition is immediately returned.

Because candidates are examined in increasing order with no gaps, no smaller valid number greater than `n` can have been skipped. This ordering provides the minimality proof directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count decimal digits without converting to a string

For candidate `x`, the source copies it into `y` and creates ten zero counts, one for each digit from zero through nine.

The loop

`y, v = divmod(y, 10)`

simultaneously obtains the remaining higher digits in `y` and the final decimal digit in `v`. It increments `cnt[v]` and repeats until no digits remain.

For example, processing 1333 extracts digits three, three, three, and one. The resulting counts have `cnt[1]=1` and `cnt[3]=3`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Translate the balance definition into one condition per digit

The final predicate is

`all(v == 0 or i == v for i, v in enumerate(cnt))`.

Here `i` is the digit and `v` is its occurrence count. A digit satisfies the condition in either of two cases:

- it is absent, so `v == 0`;
- it is present exactly `i` times, so `i == v`.

The `all` requires this for every digit class. This matches the definition exactly: only digits that occur impose their occurrence-number requirement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1333` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1333` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precomputed balanced-number table:** Store all relevant values and use `bisect_right` for logarithmic lookup in the table size.
- **Generate digit multisets and permutations:** Construct only balanced numbers, sort them, and select the next one.
- **String-based counting:** `Counter(str(x))` is concise but allocates a string and mapping per candidate.
- **`n` already balanced:** Enumeration starts at `n+1`, so it still returns a strictly greater value.
- **`n=0`:** Candidate one is balanced and is returned.
- **Digit zero:** Any occurrence makes a candidate invalid.
- **Repeated balanced layouts:** Numbers such as 1333 and 3133 share counts but are distinct candidates ordered numerically.
- **Absent digit:** It imposes no requirement beyond a zero count.
- **Digit nine:** If present, it would need nine occurrences.
- **First valid candidate:** Immediate return is safe because the search order is increasing.
- **No explicit loop bound:** Correctness relies on existence within the problem's bounded domain.
- **Manifest mismatch:** Exact work is sequential in the answer gap, not a literal constant number of operations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(G(D+10)$. Let $G$ be the gap between `n` and the returned answer, and let $D$ be the maximum number of decimal digits among tested candidates. Each test extracts $O(D)$ digits and scans the fixed ten-entry count array, so time is $O(G(D+10))$, usually written $O(GD)$ or, with the constrained digit count treated as constant, $O(G)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
