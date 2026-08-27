# Guided Example: Combination Sum II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8}`
- **Required output:** `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

The objective is to compute `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]` from `{"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why sorting solves more than one problem

The input may contain repeated values, but each array position may be selected at most once. Those facts create two different obligations. The search must not reuse a position, and it must not return the same value combination multiple times merely because equal values came from different positions.

Sorting places equal values next to one another and gives every generated combination a non-decreasing value order. That makes duplicates visible at the exact decision level where they would arise. Sorting also makes the smallest available candidate easy to identify, which supports pruning when the remaining sum is too small.

The source sorts `candidates` in place. This changes the caller's list order, but order has no meaning in the requested result and the judge does not require the input list to be preserved.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of `dfs(i, s)`

The shared list `t` is the partial combination selected on the current recursion path. Parameter `s` is the amount still needed to reach the original target. Parameter `i` is the first input index that remains eligible.

At entry to `dfs(i, s)`, the following facts hold: the values in `t` come from distinct indices smaller than `i` or from earlier selections leading to this suffix; those selected indices strictly increase; the values sum to `target - s`; and any next selection must come from index `i` or later. The initial call `dfs(0, target)` satisfies these conditions with an empty path.

When a loop iteration selects index `j`, the child is `dfs(j + 1, s - candidates[j])`. Passing `j + 1` is the exact mechanism enforcing one-time use. Index `j` is outside the child's eligible suffix and can never be selected again on that path. Equal values can still both be used when they occupy distinct positions: after choosing the first `1`, the second `1` lies later in the array and remains available to the child.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The shared list `t` is the partial combination selected on t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Skipping duplicates at one recursion depth

The condition `if j > i and candidates[j] == candidates[j - 1]: continue` skips equal candidates only when they are alternative first choices in the same frame. Suppose sorted input begins `[1a, 1b, 2, ...]`, where the labels represent positions rather than different values. At the root, a complete combination beginning with `1a` has the same values as the corresponding combination beginning with `1b`; both children would see equivalent remaining suffix values for result purposes. Exploring only the first `1` avoids duplicate output.

The `j > i` part is critical. In a deeper call after `1a` has already been chosen, `i` may point at `1b`. Because `j == i` for that child's first iteration, the second `1` is not skipped. Thus `[1, 1, 6]` remains possible. The rule is not “never use the same value twice”; it is “do not start two sibling branches with the same value.”

This same-depth principle generalizes to any group of duplicates. The first occurrence at that depth represents choosing that value, and later identical occurrences would generate the same value sequences. At a deeper depth, another occurrence represents consuming an additional copy and is a different legitimate decision.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency-compressed search:** Convert each di:** - **Frequency-compressed search:** Convert each distinct value to `(value, count)` and choose that value zero through `count` times. This removes duplicate-index branches explicitly, but adds a second loop over multiplicities and a different state representation.
- **Set-based result deduplication:** Explore all index subsets and insert sorted tuples into a set. It is easier to get working initially, but wastes time generating duplicate value combinations and uses extra hashing memory.
- **Binary include/exclude recursion:** Decide whether to take each position. To remain duplicate-free, the exclude branch must skip the entire run of equal values; the loop formulation expresses that rule more directly.
- **Loop-level `break` when a value exceeds `s`:** Sorting makes this safe and avoids the selected source's immediately failing recursive calls. It is a constant-factor improvement, not a different algorithm.
- **Multiple equal values may be used:** Duplicate skipping is scoped to siblings. Separate copies at later indices can appear together in a result, such as `[1, 1, 6]`.
- **Each position only once:** Passing `j + 1` is non-negotiable. Passing `j` would incorrectly permit unlimited reuse as in the different Combination Sum problem.
- **Target smaller than the minimum candidate:** The initial pruning check returns `[]` without entering the loop.
- **Candidate exactly equals the remainder:** Its child receives zero, copies the completed path, and returns.
- **Positive-value assumption:** It makes overshoot pruning and termination valid. Zero or negative candidates would need different logic, but the contract excludes them.
- **Input mutation:** Sorting in place changes `candidates`. A caller that needs the original order would have to pass a copy or use `sorted(candidates)`.
- **Output order:** Results and their internal values happen to follow sorted depth-first order, but the contract requires uniqueness, not a particular presentation order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot 2^n)$. Let $n$ be the number of input positions. Ignoring pruning, each position can be excluded or included, so there are at most $2^n$ subsets. Visiting and copying paths of length up to $n$ gives the conservative $O(n \cdot 2^n)$ time bound in the manifest. Sorting adds $O(n \log n)$, which is dominated by the exponential enumeration bound. Duplicate skipping and target pruning can reduce the actual tree substantially but do not improve the worst-case class when values are distinct and many subsets remain plausible.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
