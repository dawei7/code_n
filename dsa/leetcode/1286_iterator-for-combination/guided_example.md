# Guided Example: Iterator for Combination

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"characters": "abc", "combinationLength": 2, "operations": [["next", []], ["hasNext", []], ["next", []], ["hasNext", []], ["next", []], ["hasNext", []]]}`
- **Required output:** `["ab", true, "ac", true, "bc", false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design the `CombinationIterator` class:

The objective is to compute `["ab", true, "ac", true, "bc", false]` from `{"characters": "abc", "combinationLength": 2, "operations": [["next", []], ["hasNext", []], ["next", []], ["hasNext", []], ["next", []], ["hasNext", []]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute combinations, then iterate by index

The exact class does all combinational work in its constructor. It generates strings of the required length in lexicographic order and stores them in `cs`. Method `next` then returns one stored string and advances an index, while `hasNext` compares that index with the list length.

This design favors extremely simple query operations at the cost of potentially large initialization time and persistent storage.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"characters": "abc", "combinationLength": 2, "operations": [["next", []], ["hasNext", []], ["next", []], ["hasNext", []], ["next", []], ["hasNext", []]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Backtracking decides include or exclude

Nested function `dfs(i)` considers character position `i`. List `t` contains the characters selected so far.

If `len(t) == combinationLength`, a complete combination has been formed. The code joins `t` into a string, appends it to `cs`, and returns immediately. Returning prevents longer selections.

If `i == n` before enough characters have been chosen, no positions remain and the branch returns without output.

Otherwise, the function first includes `characters[i]`: append it, recurse on `i + 1`, and then pop it to restore the previous prefix. It next excludes that character and recurses on `i + 1`. The append-recursion-pop sequence is standard backtracking and ensures sibling branches do not contaminate one another.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why generation order is lexicographic

The input characters are sorted and distinct. At the earliest position where two generated combinations differ, the branch that included the earlier character is explored before the branch that skipped it for a later character. Therefore all combinations beginning with a smaller possible character are completed before combinations beginning with a larger one.

The same include-first ordering applies recursively at every subsequent position. This produces lexicographic order directly, so neither `cs.sort()` nor reversal is needed.

For `"abc"` and length two, the traversal completes `"ab"`, then `"ac"`, then `"bc"`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["ab", true, "ac", true, "bc", false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"characters": "abc", "combinationLength": 2, "operations": [["next", []], ["hasNext", []], ["next", []], ["hasNext", []], ["next", []], ["hasNext", []]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["ab", true, "ac", true, "bc", false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Algorithm L on demand:** Store $k$ selected indices and advance to the next lexicographic combination in $O(k)$ time, using $O(k)$ space and no full output cache.
- **Pruned backtracking:** Stop when remaining positions cannot fill the combination. It avoids many doomed branches while retaining precomputation.
- **Bitmask enumeration:** Test all $2^n$ masks and retain those with $k$ bits. It is simple but also explores the full subset space.
- **Combination length one:** Results are the individual input characters in order.
- **Combination length equals input length:** Only the full string is output, though the exact unpruned DFS still explores many exclusion branches.
- **Repeated `hasNext` calls:** They do not advance `idx`.
- **Valid `next` guarantee:** The exact method would raise an index error after exhaustion, but the contract prohibits such a call.
- **Sorted distinct input:** Both lexicographic proof and duplicate freedom rely on this guarantee.
- **Precomputation latency:** Construction may be expensive even if the caller consumes only the first few combinations.
- **Persistent memory:** Returned strings remain stored after being consumed because `idx` advances without removing them.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^n+Bk)$. Joining each of the $B$ completed combinations costs $O(k)$, for $O(Bk)$ output-construction work. The include/exclude recursion visits at most $O(2^n)$ states. Exact initialization time is therefore $O(2^n+Bk)$.
- **Auxiliary Space Complexity:** $O(Bk+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
