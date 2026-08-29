# Guided Example: Concatenate Non-Zero Digits and Multiply by Sum II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "10203004", "queries": [[0, 7], [1, 3], [4, 6]]}`
- **Required output:** `[12340, 4, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where $\text{queries}[i] = [l_{i}, r_{i}]$.

The objective is to compute `[12340, 4, 9]` from `{"s": "10203004", "queries": [[0, 7], [1, 3], [4, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build three prefix summaries

For every source prefix ending before index `i`:

- `sum_d[i]` is the sum of its decimal digits. Zeros contribute nothing, so this is also the sum of retained nonzero digits.
- `cnt_n0[i]` is the number of nonzero digits.
- `p[i]` is the integer formed by concatenating its nonzero digits, stored modulo `MOD`.

When digit `d` is nonzero, concatenation updates as `p*10+d` and the count rises. When `d` is zero, `p` and the count remain unchanged. The digit sum always adds `d`.

These invariants are built in one left-to-right pass.

Inductively, suppose `p[i]` is the filtered value of `s[:i]` modulo `MOD`. A zero leaves that sequence unchanged. A nonzero digit appends one decimal symbol, whose numeric recurrence is old value times ten plus the digit. Thus every prefix entry has the claimed meaning.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "10203004", "queries": [[0, 7], [1, 3], [4, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remove the filtered prefix before a query

For inclusive query `[l,r]`, let:

$$
n_0=\texttt{cnt\_n0}[r+1]-\texttt{cnt\_n0}[l]
$$

be the number of retained query digits, and

$$
sd=\texttt{sum\_d}[r+1]-\texttt{sum\_d}[l]
$$

be their sum.

Let `A` be the filtered nonzero-digit sequence before `l` and `B` the filtered sequence inside the query. The filtered prefix through `r` is their concatenation:

$$
A\Vert B=A\cdot10^{|B|}+B.
$$

Therefore

$$
B=p[r+1]-p[l]\cdot10^{n_0}\pmod{MOD}.
$$

The global `pow10` table supplies `10^{n_0} mod MOD` in constant time.

The code stores this residue as `x` and appends `x*sd mod MOD`.

For example, suppose the filtered prefix before `l` is 12 and the query's filtered digits form 34. Then the filtered prefix through `r` is `12*10²+34=1234`. Subtracting `12*10²` isolates 34. Zeros in the original substring never enter the exponent because `n0` counts only retained digits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why zeros need no special query correction

Zeros neither extend the filtered decimal value nor add to the digit sum or nonzero count. Prefix subtraction automatically ignores them wherever they appear.

If a query contains only zeros, `n0=0`, the two filtered prefix values are equal, `sd=0`, and the product is zero.

For `"10203004"` over the full range, the filtered prefix value is 1234 and digit sum ten. For substring `"020"`, removing the preceding filtered prefix with one decimal shift isolates two, and its digit sum is two.

Digit sums are stored without taking the modulus, but their maximum is only nine times the string length. Multiplying by the modular value and reducing at the end is equivalent to reducing the sum earlier.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[12340, 4, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "10203004", "queries": [[0, 7], [1, 3], [4, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[12340, 4, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan each query substring:** This can require $O(mq)$ total work. Prefix summaries make queries constant time.
- **Use ordinary source length in the power:** Removed zeros do not occupy digits in `B`; the exponent must be the nonzero count.
- **Prefix only digit sums:** The concatenated value requires its own modular prefix recurrence.
- **Construct enormous integers exactly:** Query values can have $10^5$ digits. Modular prefixes avoid materializing them.
- **All-zero query:** Both filtered value and sum are zero.
- **Single nonzero digit:** The result is its square.
- **Leading or trailing zeros in a query:** They disappear and do not change the exponent.
- **Negative intermediate `x`:** The final modulo normalizes it correctly.
- **Full-string query:** `p[0]=0`, so the prefix-removal formula returns the complete filtered value.
- **Module-level table cost:** It is one-time shared work, not recreated for every method call.
- **Independent queries:** Prefix arrays remain immutable; one query never changes indices for another.
- **Repeated nonzero digits:** Concatenation is positional, so duplicates are appended separately and `cnt_n0` counts both.
- **Digit-sum prefix:** Ordinary subtraction works because digit sums are additive, unlike concatenated values which require the power adjustment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `m=len(s)` and `q=len(queries)`. Per method call, building three prefix arrays takes $O(m)$ time, and each query takes $O(1)$, for $O(m+q)$ time.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
