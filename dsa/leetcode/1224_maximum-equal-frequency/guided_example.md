# Guided Example: Maximum Equal Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 2, 1, 1, 5, 3, 3, 5]}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` of positive integers, return the longest possible length of an array prefix of `nums`, such that it is possible to remove **exactly one** element from this prefix so that every number that has appeared in it will have the same number of occurrences.

The objective is to compute `7` from `{"nums": [2, 2, 1, 1, 5, 3, 3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Evaluate every prefix without recounting it

For each prefix, the question is whether deleting exactly one occurrence can make all values that remain have the same positive frequency. Rebuilding a frequency table for every prefix would repeat almost all earlier work and could take quadratic time.

The solution processes `nums` once and maintains two related summaries:

- `cnt[v]` is the number of times value `v` appears in the current prefix.
- `ccnt[f]` is the number of distinct values whose current frequency is exactly `f`.

For example, if the prefix has counts `{2: 3, 5: 3, 8: 2}`, then `ccnt[3] == 2` and `ccnt[2] == 1`. This “frequency of frequencies” table makes it possible to recognize the few shapes that one deletion can repair.

The variable `mx` is the greatest value frequency in the current prefix. It never decreases as the prefix grows. The variable `ans` remembers the longest valid prefix length found so far. Because enumeration starts at one, `i` is the current prefix length rather than a zero-based index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 2, 1, 1, 5, 3, 3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Update both tables consistently

When a new `v` arrives, it moves from its old frequency bucket to the next bucket. If `v in cnt`, the old frequency is positive, so `ccnt[cnt[v]] -= 1` removes one distinct value from that bucket. Then `cnt[v] += 1` raises its occurrence count, `mx` is updated, and `ccnt[cnt[v]] += 1` places it in the new bucket.

Zero-valued entries may remain in the `Counter`, but they do not hurt the arithmetic. A missing key also reads as zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When a new `v` arrives, it moves from its old frequency buck... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: There are only three repairable frequency shapes

Deleting one occurrence changes the frequency of exactly one value by one. If that frequency was one, the value disappears entirely and is no longer among the values that “have appeared” after deletion. All other values keep their frequencies. Therefore, before deletion, a valid prefix must have one of three shapes.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 2, 1, 1, 5, 3, 3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recount every prefix:** Building a new frequen:** - **Recount every prefix:** Building a new frequency map and testing it after each extension can take \(O(n^2)\). Maintaining `cnt` and `ccnt` shares the work.
- **Track a set of frequencies only:** A set reveals which frequencies exist but not how many values occupy each one. The conditions require knowing whether the maximum or singleton bucket contains exactly one value.
- **All values distinct:** `mx == 1` makes every prefix valid, because one singleton can be removed and all remaining counts stay one.
- **All values equal:** Every prefix is valid. Deleting one occurrence leaves the single remaining value with any positive frequency, or leaves no values for a length-one prefix.
- **Exactly one singleton:** It is removable only when every other value has the same frequency. The weighted-total equation rules out hidden frequency levels.
- **Unique value one above the rest:** This is repairable by deleting one copy of that unique maximum. Two maximum values would require two deletions, so `ccnt[mx] == 1` is necessary.
- **Stale zero buckets:** Decrementing `ccnt` can leave keys with value zero. Weighted arithmetic and equality checks remain correct because those buckets contribute nothing.
- **Exactly one deletion:** The cases do not merely test whether frequencies are already equal. For equal frequencies greater than one across multiple values, deleting one creates inequality and the prefix is not automatically valid.
- **Positive input values:** Hash-map logic would also work for zero or negative values, but the given domain is positive.
- **Returning a prefix length:** The algorithm need not remember which occurrence to delete. The matching shape identifies that a deletion exists, which is sufficient for the requested length.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let \(n=\lvert\texttt{nums}\rvert\). Each element causes a constant expected number of hash-table operations and three constant-time shape checks, so expected time is \(O(n)\). As usual for Python hash tables, this is an expected bound; pathological collisions can degrade individual operations.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
