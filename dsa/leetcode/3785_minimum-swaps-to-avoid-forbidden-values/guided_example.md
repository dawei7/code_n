# Guided Example: Minimum Swaps to Avoid Forbidden Values

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3], "forbidden": [3, 2, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays, `nums` and `forbidden`, each of length `n`.

The objective is to compute `1` from `{"nums": [1, 2, 3], "forbidden": [3, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate global feasibility from current conflicts

Swaps preserve the multiset of `nums`. Before minimizing swaps, the source asks whether any permutation can avoid all forbidden values.

Let $M_v$ be the number of occurrences of value $v$ in `nums`, and let $F_v$ be the number of positions whose forbidden value is $v$. An occurrence of $v$ may be placed only in the other $N-F_v$ positions. Therefore feasibility requires

$$
M_v\le N-F_v,
$$

or equivalently $M_v+F_v\le N$, for every value appearing in `nums`.

The two `Counter` objects store $M_v$ and $F_v$. If any source value violates the inequality, the method returns `-1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3], "forbidden": [3, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why that feasibility condition is also sufficient

Think of each value occurrence as an item and each array index as a destination. An item of value $v$ connects to every destination except those with forbidden value $v$.

For a set of items all having one value $v$, the condition above guarantees enough allowed destinations. If a set contains at least two different values, its combined allowed destinations include every index: an index forbids only one value, so it cannot simultaneously forbid both distinct values.

These are exactly the restrictive cases of the matching condition. Thus the per-value inequalities guarantee a complete assignment of all occurrences to legal positions, not merely a necessary count check.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Focus swap counting on currently bad positions

An index is bad when `nums[i] == forbidden[i]`. The source counts bad indices by their shared offending value in `bad_count`.

Let

$$
B=\sum_v B_v
$$

be the total number of bad positions and

$$
M=\max_v B_v
$$

be the largest same-value bad group. The source computes both, using a default of zero when no bad position exists.

Good positions need not be changed unless they serve as temporary helpers. The two quantities $B$ and $M$ completely determine the minimum once global feasibility is known.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3], "forbidden": [3, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Construct a target permutation then count cycles:** This can recover an explicit swap plan but requires a careful matching choice; the counting formula avoids unnecessary construction.
- **Greedily swap arbitrary bad pairs:** Equal offending values do not fix each other, and careless helper choices can create new conflicts.
- **Check only `nums` frequencies:** Feasibility depends on how many destinations forbid each value, so `forbidden_count` is essential.
- **Use only $\lceil B/2\rceil$:** A dominant same-value group may require more because one swap fixes at most one of its members.
- **Use only $M$:** When bad values are balanced, the two-bad-per-swap limit may be larger.
- **No bad indices:** Both $B$ and $M$ are zero, so the answer is zero.
- **One bad index:** It needs one compatible helper swap if the instance is feasible.
- **All bad indices share one value:** Feasibility may fail; if it holds through other positions, each bad member needs its own swap.
- **Odd number of balanced bad positions:** The ceiling accounts for the final repair requiring two-swap handling rather than a fractional pair.
- **Values absent from `nums`:** They need no feasibility iteration because no item of that value must be placed.
- **Large arbitrary values:** Counters avoid dependence on the numeric range.
- **Input preservation:** No actual swaps are performed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Building the source and forbidden counters takes $O(N)$ expected time. The feasibility scan visits at most $N$ distinct source values. Building `bad_count` and summing it are also linear.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
