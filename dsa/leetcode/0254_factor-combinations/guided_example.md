# Guided Example: Factor Combinations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Numbers can be regarded as the product of their factors.

The objective is to compute `[]` from `{"n": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The remaining quotient is already a complete ending

At the beginning of every recursive call, if `t` is nonempty, the solution appends `t + [n]` to `ans`. This says: stop splitting now and use the entire remaining quotient as the final factor.

For example, after choosing `2` from `12`, the recursive state is `t = [2]`, `n = 6`, so `[2, 6]` is immediately a valid answer. The same call may continue splitting `6`, choosing another `2` and reaching `t = [2, 2]`, `n = 3`; that new state records `[2, 2, 3]`.

The top-level call has an empty `t`, so it deliberately does not append `[original_n]`. A one-element list containing `n` is excluded because factors must lie below `n`; the task asks for actual factorizations into at least two factors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Search only possible smaller factors

Within `dfs(n, i)`, candidate `j` begins at `i` and continues while `j * j <= n`. If `j` divides `n`, then `n // j` is its paired quotient. Limiting `j` to the square root ensures

$$
j\le \frac{n}{j}.
$$

So choosing `j` keeps it no larger than the remaining quotient that may eventually become the last factor. Trying divisors above the square root would merely rediscover the same pair in reversed order.

When divisibility holds, the algorithm:

1. appends `j` to `t`;
2. recurses on quotient `n // j` with new minimum `j`;
3. pops `j` to restore `t` before trying the next candidate.

Passing `j` rather than `j + 1` allows repeated factors, which are necessary for combinations such as `[2, 2, 3]` and `[4, 4]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Within `dfs(n, i)`, candidate `j` begins at `i` and continue... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the appended quotient respects ordering

At a recursive state, every value already in `t` is at most the current minimum `i`. The state was reached by choosing some factor `j` with `j * j <= previous_remainder`, so its quotient—the new remaining `n`—is at least `j`. Therefore, appending `n` to `t` yields a nondecreasing list. The solution never emits a list such as `[3, 2, 2]`.

More formally, each chosen factor becomes the lower bound for all subsequent choices, and every chosen divisor is no greater than its paired quotient. Both the continuing path and the stop-now output preserve sorted order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate ordered factor sequences:** Trying al:** - **Generate ordered factor sequences:** Trying all factor orders and deduplicating with a set wastes work on permutations. The nondecreasing lower bound prevents duplicates before they are created.
- **Iterative DFS:** Store states containing a factor path, remaining quotient, and minimum factor. It avoids recursion but copies more partial paths and can use substantially more working memory.
- **Prime input:** The root tests candidates through $\sqrt n$ but finds no divisor. Since `t` is empty, `[n]` is not emitted, and the answer is empty.
- **`n = 1`:** No candidate begins below or at its square root, and the top-level one-element form is excluded, so the result is `[]`.
- **Perfect square:** The condition `j * j <= n` includes the square-root divisor. This is necessary for combinations such as `[4, 4]` when `n = 16`.
- **Repeated factors:** Recursing with lower bound `j`, not `j + 1`, allows the same factor again.
- **Remaining quotient as a factor:** Recording `t + [n]` before further splits ensures shorter valid factorizations such as `[2, 6]` are not lost while exploring longer forms.
- **Backtracking restoration:** `t.pop()` must run after every recursive return so a candidate from one branch does not leak into the next branch.
- **Large prime near $10^7$:** There is no output, but the algorithm still performs roughly $\sqrt n$ divisibility tests; this is why the non-output root term matters.
- **Result ordering:** DFS produces a deterministic nondecreasing-factor order, but the outer ordering of combinations need not be sorted because any answer order is accepted.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W+P)$. The cost is output-sensitive and depends strongly on the divisor structure of `n`. Let $F$ be the number of returned combinations, $P$ the total number of integers across all returned lists, and let
- **Auxiliary Space Complexity:** $O(\log n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
