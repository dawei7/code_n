# Guided Example: Split Message Based on Limit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"message": "short message", "limit": 15}`
- **Required output:** `["short mess<1/2>", "age<2/2>"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string, `message`, and a positive integer, `limit`.

The objective is to compute `["short mess<1/2>", "age<2/2>"]` from `{"message": "short message", "limit": 15}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: For a chosen part count, suffix lengths determine total capacity

If the total number of parts is `k`, part `j` receives suffix `"<j/k>"`. Its suffix length is

$$
\operatorname{digits}(j)+\operatorname{digits}(k)+3,
$$

where the three fixed characters are `<`, `/`, and `>`.

Every non-final part must have total length exactly `limit`, so its payload capacity is `limit - suffix_length`. The last part may be shorter, which means the split is feasible when the combined payload capacity across all parts is at least the message length. Construction will fill earlier parts to capacity and leave any unused capacity only at the end.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"message": "short message", "limit": 15}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain numerator digit cost incrementally

The loop tests `k` from 1 through `n=len(message)`. There is no need for more than `n` parts because each meaningful part must carry message content and the message has only `n` characters.

`sa` accumulates

$$
\sum_{j=1}^{k}\operatorname{digits}(j).
$$

When `k` increases by one, adding `len(str(k))` updates this numerator-digit total in constant bounded work.

For the current `k`:

- `sb = len(str(k))*k` is the denominator digit count repeated in all $k$ suffixes.
- `sc = 3*k` counts the three punctuation characters per suffix.

Thus

`limit*k - (sa+sb+sc)`

is the total number of message-character slots available.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the first feasible count

The loop tests counts in increasing order. The first `k` whose total capacity is at least `n` is therefore the minimum number of parts that can hold the message under those suffixes.

Suffix length changes discontinuously when `k` gains a decimal digit. More parts do not always mean proportionally more capacity because every denominator becomes longer. Direct enumeration correctly handles those boundaries.

If no `k<=n` is feasible, the method returns an empty list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["short mess<1/2>", "age<2/2>"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"message": "short message", "limit": 15}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["short mess<1/2>", "age<2/2>"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Binary search the part count:** Feasibility is complicated by denominator digit jumps and is not simply monotone across every boundary, so ascending enumeration is safer.
- **Recompute numerator digits for each count:** Summing `digits(1..k)` from scratch would make the search quadratic. Incremental `sa` avoids that repetition.
- **Limit too small for suffixes:** No count gains usable total payload and the method returns an empty list.
- **One feasible part:** Suffix `"<1/1>"` is appended and the complete message fits before it.
- **Last part shorter:** Slicing stops at message end, which is explicitly allowed only for the final part.
- **Spaces in the message:** Slicing treats them as ordinary characters and preserves them exactly.
- **Digit boundary at 10, 100, or 1000 parts:** Denominator suffix cost increases for every part, and `sb` captures the jump.
- **Numerator digit variation:** `sa` counts each index's actual width rather than assuming all numerators match `k`.
- **Minimum count:** Returning immediately at the first feasible `k` is valid because enumeration is ascending.
- **Reconstruction:** Payloads are consecutive slices, so removing suffixes yields the original message without gaps or reordering.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. The feasibility loop performs at most $m$ iterations. Once a count is chosen, construction copies every message character once and creates $k\le m$ suffixes. Under bounded-width arithmetic and formatting, time is $O(m)$.
- **Auxiliary Space Complexity:** $O(m+k\log k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
