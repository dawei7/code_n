# Guided Example: Minimum Deletions to Make Alternating Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ABA", "queries": [[2, 1, 2], [1, 1], [2, 0, 2]]}`
- **Required output:** `[0, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` of length `n` consisting only of the characters `'A'` and `'B'`.

The objective is to compute `[0, 2]` from `{"s": "ABA", "queries": [[2, 1, 2], [1, 1], [2, 0, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert deletions into equal-adjacent edge counts

Any binary string consists of maximal runs of equal characters. An alternating subsequence can keep at most one character from each run: keeping two from the same run with no different run between them would place equal characters consecutively.

Keeping one character from every run is achievable because neighboring runs contain opposite characters. Therefore the longest alternating subsequence has exactly one character per run.

For a substring of length $L$ with $R$ runs, minimum deletions are $L-R$. Each run of length $m$ contains $m-1$ equal-adjacent edges, and summing over runs gives

$$
\sum(m-1)=L-R.
$$

Thus the answer for `s[l..r]` is simply the number of indices `i` with `l<i<=r` and `s[i]==s[i-1]`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ABA", "queries": [[2, 1, 2], [1, 1], [2, 0, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store one indicator per edge ending position

The source creates `nums` of length `n`. For `i>=1`,

`nums[i] = int(s[i] == s[i-1])`.

Index `i` represents the edge between characters `i-1` and `i`. A one means that edge forces one deletion; a zero means it already alternates.

`nums[0]` is a sentinel because no edge ends at the first character. It begins at zero and is excluded from every range answer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain edge sums in a Fenwick tree

The Fenwick tree uses one-based positions, so source indicator `nums[i]` is stored at tree position `i+1`. Initialization inserts every one-valued real edge.

`update(x, delta)` adds `delta` to all Fenwick ranges containing position `x`. `query(x)` returns the sum of tree positions 1 through `x`. Both move by the lowest set bit and take $O(\log N)$ time.

For a type-two query `[2,l,r]`, relevant source indicators are `nums[l+1]` through `nums[r]`. Their tree positions are `l+2` through `r+1`. The prefix difference

`bit.query(r+1) - bit.query(l+1)`

keeps exactly that interval. It excludes the boundary edge ending at `l` because the character before `l` is outside the substring.

For a one-character range, `l=r` and the two prefix queries are equal, correctly returning zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ABA", "queries": [[2, 1, 2], [1, 1], [2, 0, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Segment tree:** It can maintain the same edge sums with $O(\log N)$ updates and queries, but a Fenwick tree is smaller for point updates plus range sums.
- **Recompute each substring:** Scanning every requested range can cost $O(NQ)$.
- **Maintain characters and recompare neighbors:** This is valid, but the binary toggle property lets the source update indicators directly.
- **Count equal pairs including edge `(l-1,l)`:** That edge crosses the substring boundary and must be excluded.
- **Assume answer is number of runs:** Minimum deletions are length minus runs, equivalently equal-edge count.
- **Flip at index zero:** The sentinel update cancels from every query; the real right edge is still toggled.
- **Flip at index `n-1`:** Only the left incident edge is real, so the guarded right update is skipped.
- **Single-character string:** There are no real edges, and every type-two answer is zero.
- **Already alternating range:** All internal indicators are zero, producing zero deletions.
- **All-equal range of length `L`:** It has `L-1` equal edges and needs `L-1` deletions.
- **Repeated flip of the same index:** Both affected equality indicators toggle back on the second flip.
- **Range after earlier flips:** The Fenwick state incorporates updates, so queries are correctly stateful.
- **Binary alphabet dependency:** XOR-toggling equality is guaranteed only because every character has exactly one opposite value.
- **Output order:** Answers are appended only for type-two queries and retain their relative query order.
- **Input string:** It remains immutable; `nums` is the maintained state representation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((N+Q)$. Initialization examines $N-1$ edges and performs a Fenwick update for every equal one, costing $O(N\log N)$ worst-case. It could be built in linear time, but that is not the exact source.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
