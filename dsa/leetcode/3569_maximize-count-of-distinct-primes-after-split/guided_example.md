# Guided Example: Maximize Count of Distinct Primes After Split

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3, 1, 2], "queries": [[1, 2], [3, 3]]}`
- **Required output:** `[3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` having length `n` and a 2D integer array `queries` where $\text{queries}[i] = [idx, val]$.

The objective is to compute `[3, 4]` from `{"nums": [2, 1, 3, 1, 2], "queries": [[1, 2], [3, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turning one prime’s occurrences into a split interval

Index split positions by `s=0,\ldots,n-2`, where `s` means the prefix ends at index `s` and the suffix starts at `s+1`.

For a prime value `p`, let `first(p)` and `last(p)` be its smallest and largest current occurrence indices.

The prime appears in both parts exactly when

$$
first(p) \le s < last(p).
$$

So `p` contributes its extra one to every split in inclusive interval

`[first(p), last(p)-1]`.

If `p` occurs only once, first equals last and this interval is empty. The prime still contributes the global baseline one, but it can never be counted in both sides.

Adding one over every prime’s spanning interval creates an overlap count for each split. The best split has the maximum overlap.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3, 1, 2], "queries": [[1, 2], [3, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the answer formula is exact

Let `D` be the number of distinct prime values currently present. At a fixed split, take any such prime:

- occurrences only in the prefix give `1+0=1` across the two distinct-counts;
- occurrences only in the suffix give `0+1=1`;
- occurrences on both sides give `1+1=2`.

Starting with one for every present prime gives `D`. Exactly the spanning primes need one extra, and their count is the interval overlap at that split.

Therefore the maximum possible result is

`distinct_prime_count + maximum_overlap[1]`,

where segment-tree root `maximum_overlap[1]` stores the largest overlap over all split indices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let `D` be the number of distinct prime values currently pre... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Precomputing primality

The source first copies `nums` because query updates must persist locally without mutating the caller’s original list.

`value_limit` is the largest value appearing either initially or as a future query replacement. A sieve byte array marks all prime values through this limit. Zero and one are cleared. For each still-prime `value` up to `\sqrt{U}`, all multiples starting at `value^2` are cleared with a stepped slice.

Beginning at `value^2` is safe because smaller multiples already have a smaller prime factor and were handled earlier.

After the sieve, primality of any old or new query value is a constant-time array lookup.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3, 1, 2], "queries": [[1, 2], [3, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recompute every split after each query:** Coun:** - **Recompute every split after each query:** Counting distinct primes independently in every prefix and suffix would cost at least linear time per query and can become quadratic overall.
- **Fenwick tree alone:** Range addition and point query are easy, but the task needs the maximum across all split positions after each update. A lazy segment tree maintains that global maximum directly.
- **Balanced sorted occurrence sets:** They provide exact first and last indices with `O(\log n)` insertion and deletion. Python lacks a built-in balanced tree, so active sets plus lazy min/max heaps implement the required extremes.
- **One occurrence of a prime:** It raises `distinct_prime_count` by one but contributes no overlap interval, so it can be counted on only one side of any split.
- **Occurrences at both endpoints:** A prime at indices zero and `n-1` spans every legal split and adds one to the entire segment tree.
- **Removing an extreme:** Its old interval is subtracted before lazy heaps reveal the new first or last occurrence.
- **Removing the final occurrence:** The baseline distinct count decreases and no new interval is added.
- **Adding the first occurrence:** The baseline count increases, but its spanning interval remains empty.
- **Changing a value to itself:** The source skips all mutations and returns the unchanged maximum.
- **Composite and value one:** The sieve marks them nonprime, so they affect neither baseline nor overlap.
- **Persistent queries:** Updating the copied `nums` array ensures the next query observes all prior replacements.
- **Stale heap entries:** Membership in the active set distinguishes valid tops. Duplicate heap entries for an index can be harmless while that index is active and are eventually discarded after removal.
- **At least one split:** The constraint `n\ge2` guarantees `split_count=n-1\ge1`, so the segment-tree root represents a real split domain.
- **Why internal occurrences do not matter:** Any split between first and last automatically has at least one occurrence on each side; splits outside cannot be rescued by internal points.
- **Value limit selection:** Including all future query values ensures every replacement has a valid sieve lookup without extending the sieve online.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let `U` be the maximum numeric value in the initial array or any query, `n` the array length, and `q` the number of updates.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
