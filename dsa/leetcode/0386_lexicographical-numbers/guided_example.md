# Guided Example: Lexicographical Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 13}`
- **Required output:** `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return all the numbers in the range `[1, n]` sorted in lexicographical order.

The objective is to compute `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]` from `{"n": 13}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Lexicographical order is a traversal order

Lexicographical order compares the decimal representations as if they were words. It first compares the first character; only when those match does it compare the next character. This is why `10` comes immediately after `1` and before `2`.

The integers from `1` through `n` can be imagined as nodes in a decimal prefix tree:

- the roots are `1`, `2`, ..., `9` when they do not exceed `n`;
- a number `v` can have children `v * 10`, `v * 10 + 1`, ..., `v * 10 + 9` when those values are at most `n`.

For example, node `1` has descendants `10` through `19`; node `10` may have descendants `100` through `109`. A preorder depth-first traversal—visit a node, then visit its children from digit `0` to `9`—produces exactly lexicographical order.

A recursive DFS would make that model explicit, but its call stack uses space proportional to the number of digits. The exact solution simulates the traversal with one current integer `v`, so it meets the constant-extra-space requirement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 13}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate exactly one next number at a time

The result starts empty and `v` starts at `1`, the first positive integer lexicographically. The outer loop runs exactly `n` times because the range `[1, n]` contains exactly `n` values. At each iteration, it appends the current `v`, then computes the lexicographical successor for the next iteration.

There are two possible movements in the prefix tree:

1. descend to the smallest child if one exists;
2. otherwise, move to the next available sibling, climbing to ancestors first when necessary.

The two branches of the code implement precisely those movements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Descending to the smallest child

If `v * 10 <= n`, then appending digit zero produces a valid number. That child is the lexicographically smallest value whose decimal representation begins with the full representation of `v`. It must come immediately after `v`, before any sibling of `v`.

The solution therefore executes `v *= 10`. For example, after emitting `1` with `n = 130`, it moves to `10`; after emitting `10`, it moves to `100`. This is the iterative equivalent of making the first recursive DFS call.

It always tries digit zero first because children are ordered by their appended digit. If `v0` is not valid because it exceeds `n`, no larger child `v1` through `v9` can be valid either. In that case the subtree has no children, so the traversal must move sideways or upward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 13}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive decimal-tree DFS:** Visit roots `1` through `9` and recursively try children formed by appending digits `0` through `9`. This also runs in $O(n)$ time and is conceptually direct, but uses $O(\log n)$ call-stack space rather than the requested constant auxiliary space.
- **Convert to strings and sort:** Sorting `1` through `n` by their decimal strings is straightforward but takes $O(n\log n)$ time and $O(n)$ extra storage, failing both desired bounds.
- **Priority queue of next prefixes:** A heap can generate values in lexical order but introduces $O(\log n)$ work per removal and stores many candidates. Direct tree navigation is simpler and faster.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The outer loop appends exactly $n$ numbers. Most iterations perform constant work, but one iteration can execute the inner while loop several times while removing trailing digits.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
