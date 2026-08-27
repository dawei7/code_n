# Guided Example: Check if Array is Good

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. We consider an array **good **if it is a permutation of an array $\text{base}[n]$.

The objective is to compute `false` from `{"nums": [2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The input length determines the only possible base

`base[n]` has length `n + 1`. If the input length is `m`, a good input must therefore use

$$
n = m - 1.
$$

There is no need to guess `n` from the maximum value or try several candidates. The exact solution sets `n = len(nums) - 1` immediately.

The required multiset is then:

- one copy of every integer from 1 through `n - 1`;
- two copies of `n`.

Its total number of entries is `(n - 1) + 2 = n + 1`, exactly the input length.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count actual multiplicities

`cnt = Counter(nums)` builds a mapping from each value to its number of occurrences. Array order disappears, which is appropriate because being a permutation depends only on multiplicities.

The return expression checks:

`cnt[n] == 2`

and

`all(cnt[i] for i in range(1, n))`.

The first condition requires exactly two copies of the largest required value. The second visits every required lower value and requires a nonzero count. A missing key in a Counter evaluates as count zero, so no special membership check is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `cnt = Counter(nums)` builds a mapping from each value to it... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why “present” is enough for lower values

At first glance, `all(cnt[i] ...)` appears weaker than requiring `cnt[i] == 1`. It accepts any positive count for a required lower number. The fixed input length makes the weaker-looking test sufficient.

There are `n - 1` lower required values. If each appears at least once, they consume at least `n - 1` array positions. The exact two copies of `n` consume two more. Together they consume at least

$$
(n - 1) + 2 = n + 1
$$

positions, which is the entire array.

There is no remaining slot for an extra copy of a lower value or for an unexpected value. Therefore every lower count must in fact be exactly one, and no other key can occur.

This is a useful counting proof: the code does not omit duplicate validation; it derives it from required presence plus exact total length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort and compare positions:** Sorting lets the:** - **Sort and compare positions:** Sorting lets the first `n` entries be checked against `1..n` and the last against `n`, but costs `O(m log m)` time and may mutate input.
- **Fixed frequency array:** Since values are bounded, an indexed count list also gives linear time. Counter avoids choosing an allocation bound.
- **Use the maximum as `n`:** Length is the decisive constraint. An unexpected large value must cause rejection, not redefine a base of incompatible length.
- **Check lower counts only for presence:** This is safe because those presences plus two copies of `n` exactly fill the array.
- **Missing lower value:** Its Counter lookup is zero, causing `all` to fail.
- **Duplicate lower value:** It consumes a slot needed by some required value, so either a required presence or the exact two-`n` condition must fail.
- **Unexpected value:** It likewise displaces a required occurrence and cannot pass all conditions.
- **Too many copies of `n`:** The exact equality `== 2` rejects them.
- **`base[1]`:** The empty lower-value range makes two copies of one the sole requirement.
- **Arbitrary order:** Counter comparison ignores order, as permutation testing requires.
- **Positive-value constraint:** Zero and negative values are excluded, though either would necessarily displace a requirement and be rejected.
- **Input preservation:** Counter reads the sequence without modifying it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let `m = len(nums)`. Building the Counter takes `O(m)` expected time and `O(u)` space for `u` distinct values. The `all` generator checks `n - 1 = m - 2` possible lower values, taking `O(m)` expected time through Counter lookups. Total expected time is `O(m)`.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
