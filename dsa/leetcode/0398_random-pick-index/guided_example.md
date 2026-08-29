# Guided Example: Random Pick Index

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 3, 3], "targets": [3, 1, 3]}`
- **Required output:** `[2, 0, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` with possible **duplicates**, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

The objective is to compute `[2, 0, 4]` from `{"nums": [1, 2, 3, 3, 3], "targets": [3, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sample matching indices without storing them

The method must choose uniformly among all indices whose value equals `target`. It could first collect those indices and then choose one, but that allocates space proportional to the number of matches on every call. The exact solution instead applies reservoir sampling with reservoir size one while scanning the stored array.

The constructor simply retains the array as `nums`. During `pick(target)`:

- `n` counts how many matching indices have been seen so far;
- `ans` stores one candidate index selected uniformly from those matches.

Nonmatching elements are ignored. A match is allowed to replace the current candidate with probability $1/n$, where `n` is the updated number of matches.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 3, 3], "targets": [3, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process only the relevant population

The loop visits every `(i, v)` pair from `enumerate(nums)`. When `v != target`, the index does not belong to the sampling population, so neither `n` nor `ans` changes.

When `v == target`, `n += 1` gives this occurrence its one-based rank among matching indices. The code draws



uniformly from the inclusive integers `1` through `n`. It replaces `ans` with `i` exactly when `x == n`. Since one of the `n` equally likely results triggers replacement, the new matching index is selected with probability $1/n$.

The specific trigger could be `x == 1` instead; choosing the endpoint `n` has the same probability. What matters is one successful outcome among `n` uniform outcomes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first match always initializes a real answer

The method begins with `n = ans = 0`. Index zero is a legal array index and is not being used as a safely distinguishable sentinel. The target-exists guarantee makes that harmless.

At the first match, `n` becomes one. `random.randint(1, 1)` must return one, so `x == n` is true and `ans` is replaced by the actual matching index. From then onward, `ans` always refers to one of the matches seen so far.

If the target did not exist, the placeholder zero would be returned incorrectly. The problem explicitly rules out that call, so the implementation needs no absent-target behavior.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 0, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 3, 3], "targets": [3, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 0, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Preprocess value-to-indices lists:** In the constructor, append every index to a dictionary bucket for its value. Initialization takes $O(N)$ time and space, and each `pick` uses `random.choice` in $O(1)$. Across many calls this gives $O(N+Q)$ time, matching the manifest, but uses linear extra storage.
- **Collect matches on every call:** Build a temporary list of all qualifying indices and choose from it. This is $O(N)$ time and up to $O(N)$ temporary space per call; reservoir sampling achieves the same distribution with constant space.
- **Choose a random array index until it matches:** Rejection sampling is unbiased, but expected time can be very large when the target is rare and has no finite worst-case bound. A full reservoir scan has deterministic linear work.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the array length and $Q$ be the number of `pick` calls.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
