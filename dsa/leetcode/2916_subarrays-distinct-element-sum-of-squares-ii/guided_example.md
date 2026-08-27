# Guided Example: Subarrays Distinct Element Sum of Squares II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1]}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed **integer array `nums`.

The objective is to compute `15` from `{"nums": [1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Which left endpoints change when a value arrives

Let `value = nums[r]`, and let $p$ be its most recent previous position, or $-1$ if it has not appeared.

- For $l\le p$, subarray `nums[l..r-1]` already contains `value` at position $p$. Appending another copy does not change its distinct count.
- For $p<l\le r$, the previous occurrence lies outside `nums[l..r-1]`. Appending `value` introduces a new distinct value, so $D_l$ increases by one.

Therefore the update is one range addition:

`add(last_position[value] + 1, r, 1)`.

Afterward, `last_position[value]` becomes $r$. This range rule is the crucial observation that turns $O(n)$ work for one right endpoint into $O(\log n)$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What each segment-tree node stores

For the left-endpoint interval represented by a node, `sums[node]` stores $\sum D_l$, and `square_sums[node]` stores $\sum D_l^2$. The root covers all indices $0$ through $n-1$.

Suppose every value in a node interval of length $q$ receives increment $c$. Algebra gives

$$
(D_l+c)^2=D_l^2+2cD_l+c^2.
$$

Summing over the interval produces

$$
\sum(D_l+c)^2
=
\sum D_l^2+2c\sum D_l+c^2q.
$$

That is the exact `apply` update:

`square_sums += 2 * increment * sums + increment * increment * length`,

followed by

`sums += increment * length`.

Both aggregates are reduced modulo $10^9+7$. The pending increment is accumulated in `lazy[node]` so a fully covered interval can be changed without immediately descending to every leaf.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For the left-endpoint interval represented by a node, `sums[... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why lazy propagation remains correct

When a later partial update needs a node's children, `push` applies the stored increment to each child and clears the parent tag. Each child's two aggregates are adjusted by the same algebraic identity. Thus the children become current before recursion continues.

After a partial update, the parent recomputes both aggregates as the modular sum of its children. A fully covered update calls `apply` and stops; a partial update pushes, recurses only into intersecting children, then merges.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all subarrays:** Maintaining a set w:** - **Enumerate all subarrays:** Maintaining a set while extending each left endpoint takes $O(n^2)$ time, which is appropriate for version I but not for this input size.
- **Rebuild distinct counts for every right endpoint:** Scanning all starts after each append is also $O(n^2)$. The previous-occurrence boundary proves all changing starts form one interval.
- **Segment tree stores both moments:** Keeping only $\sum D_l$ cannot recover $\sum D_l^2$. The square-update formula requires both the first and second moments.
- **First occurrence:** With previous position $-1$, update range $[0,r]$; the new value is absent from every subarray ending before $r$.
- **Consecutive duplicate:** If the previous position is $r-1$, only start $r$ changes. Every longer subarray already contains that value.
- **Positions after the current right endpoint:** Their leaves remain zero, so the full-root square sum is still exactly the contribution of valid starts.
- **Modulo arithmetic:** Addition and the polynomial range-update identity are compatible with taking residues, so reducing node aggregates cannot alter the final modular answer.
- **Empty array is irrelevant:** The contract guarantees at least one element, allowing the tree to be built over range $0..n-1$.
- **Source provenance:** The local editorial is unavailable; this explanation follows the exact checked-in segment-tree implementation and its update formulas.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. There is one segment-tree range update per array position. A lazy range update visits $O(\log n)$ nodes, and reading the root is $O(1)$. Dictionary lookup and update are expected $O(1)$. Total expected time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
