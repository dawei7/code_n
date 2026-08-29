# Guided Example: Jump Game III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [4, 2, 3, 0, 3, 1, 2], "start": 5}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to $i + \text{arr}[i]$ or $i - \text{arr}[i]$, check if you can reach **any** index with value 0.

The objective is to compute `true` from `{"arr": [4, 2, 3, 0, 3, 1, 2], "start": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normal processing of a first-time index

The queue starts with `start`. On a pop, the code first checks `arr[i] == 0`. If true, a legal sequence of earlier jumps reached this index, so returning `true` is correct.

For a positive unvisited value, `x = arr[i]` saves the jump distance. The line `arr[i] = -1` then uses an impossible input value as the visited sentinel because all original elements are nonnegative.

The loop tries `i + x` and `i - x`. It enqueues a destination only if it lies in `[0, len(arr))` and currently has a nonnegative value. The bounds check enforces the rule against leaving the array. The sign check is meant to exclude already visited destinations.

If every index were enqueued at most once, this would be a standard BFS or worklist traversal. Every reached index would be tested for zero, marked, and expanded through its two legal jumps.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [4, 2, 3, 0, 3, 1, 2], "start": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a visited state is required

The graph can contain cycles. For example, one index can jump to a second and the second can jump back. Without a visited marker, the queue could alternate forever.

In-place marking avoids allocating a separate Boolean array. It also mutates the caller's input, which is an important behavioral consequence.

For a correct mark-on-pop design, the pop logic must begin by skipping an already marked index. The editorial version does that with an `arr[node] < 0` guard. Alternatively, a mark-on-enqueue design can guarantee that no duplicate is ever placed in the queue.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The duplicate-enqueue defect in the exact source

The exact code checks whether a destination is unvisited before enqueueing it, but it does not mark that destination at enqueue time. Two already-popped parents can therefore both enqueue the same still-nonnegative child before the child is first popped.

When the first copy is popped, it is processed normally and its array entry becomes $-1$. When the duplicate copy is later popped, the code does not skip it. The zero test fails because the entry is now $-1$, then `x = arr[i]` assigns `x = -1`. The loop consequently explores `i - 1` and `i + 1` as though they were legal jumps. Those edges did not come from the original array value.

This is not just redundant work; it can reach a zero through an illegal adjacent move and return a false positive. Therefore, the exact source as written does not support a complete correctness proof for all valid inputs.

The smallest conceptual repair is either:

- mark a destination visited at the moment it is first enqueued while preserving its jump value elsewhere or using a separate visited set, or
- after popping, add a guard that immediately continues when `arr[i] < 0` before reading `x`.

The second form matches the local editorial's BFS structure. One must still save the positive jump value before replacing it with a negative sentinel.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [4, 2, 3, 0, 3, 1, 2], "start": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Visited set with BFS:** Store indices in a set when enqueuing them and never mutate `arr`. This cleanly prevents duplicate queue entries and preserves the input, at $O(n)$ extra space.
- **Guard marked pops:** Keeping the exact mark-on-pop style is valid only if `arr[i] < 0` causes an immediate skip before `x` is read. This is the minimal logical repair shown by the editorial.
- **Iterative DFS:** A stack can replace the queue because only reachability matters. It has the same $O(n)$ time and space bounds with correct visited handling.
- **Recursive DFS:** It is concise but can recurse through $O(n)$ indices and exceed Python's recursion limit near the maximum input size.
- **Start already at zero:** The first pop returns true before any mutation.
- **Jump outside the array:** The bounds condition rejects that destination without enqueuing it.
- **Two jumps to the same destination:** When `arr[i] = 0`, the goal returns before expansion. For positive values, `i + x` and `i - x` differ, but different parent indices can still target the same child, causing the exact duplicate bug.
- **Cycles:** Correct visited marking ensures a cycle does not cause infinite traversal.
- **Unreachable zero:** After all genuinely reachable indices are processed, a corrected queue empties and returns false.
- **In-place sentinel:** $-1$ is safe only because the contract guarantees every original value is at least zero.
- **Input mutation visible to callers:** Visited positive entries become $-1$. A caller needing the original data must copy it or use separate visited storage.
- **Exact-source limitation:** The approach artifact should not claim the submitted code is correct for all valid inputs until duplicate pops are skipped or duplicate enqueues are prevented.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For the intended corrected traversal, let $n$ be the array length. Each index is processed at most once, and each processing checks two possible edges. Time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
