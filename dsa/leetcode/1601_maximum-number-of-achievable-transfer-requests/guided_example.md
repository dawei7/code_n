# Guided Example: Maximum Number of Achievable Transfer Requests

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "requests": [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We have `n` buildings numbered from `0` to $n - 1$. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

The objective is to compute `5` from `{"n": 5, "requests": [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every request is an accept-or-reject choice

There are at most 16 requests. That small bound allows enumeration of every subset. A bitmask with $M$ bits represents one choice:

- bit `i` equals one if request `i` is accepted;
- bit `i` equals zero if it is rejected.

Integers from zero through `(1 << M) - 1` cover all $2^M$ subsets exactly once.

The method tests whether each chosen subset leaves every building’s net employee change at zero and records the largest number of accepted requests among valid subsets.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "requests": [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing a subset’s balance

The helper `check(mask)` creates `cnt = [0] * n`. For an accepted transfer from building `f` to building `t`, it performs:

`cnt[f] -= 1`

`cnt[t] += 1`.

Thus `cnt[b]` equals employees entering building `b` minus employees leaving it across the selected requests. The sign convention could be reversed without changing the zero test, but the source consistently uses incoming as positive.

After scanning all requests, `all(v == 0 for v in cnt)` returns true exactly when every building has equal incoming and outgoing counts. That is the achievability condition.

A request from a building to itself subtracts and adds at the same index, for net zero. Such a request never harms feasibility and may increase the selected count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The helper `check(mask)` creates `cnt = [0] * n`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Counting selected requests

For each mask, `mask.bit_count()` returns the number of one bits, which is exactly the number of accepted requests in that subset.

The source calls `check(mask)` only when `ans < cnt`. If the subset selects no more requests than the best valid subset already found, it cannot improve the maximum, so validating its building balances would be wasted work.

The strict inequality is sufficient because only the maximum count is requested. Equal-size valid subsets do not change `ans`.

If a larger subset is balanced, `ans = cnt` records its size. Starting `ans` at zero is valid because the empty subset always has zero net change.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "requests": [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive backtracking:** Accept or reject eac:** - **Recursive backtracking:** Accept or reject each request while mutating one shared balance array, then undo accepted changes. It has the same exponential search and uses $O(N+M)$ space including recursion.
- **Meet in the middle:** Splitting requests into halves can combine balance vectors and may help for larger $M$, but the bound of 16 makes direct enumeration simpler.
- **Greedy acceptance:** Individual transfers do not reveal whether they participate in a balanced cycle, so local choices cannot ensure a maximum subset.
- **Check masks in descending bit count:** This can return after the first balanced size is found, though ordering or grouping masks adds complexity. The source uses a simple ascending numeric scan with size pruning.
- **Empty subset:** It is always balanced and justifies initializing `ans = 0`.
- **All requests achievable:** The all-ones mask passes and updates `ans` to $M$.
- **Self-transfer:** Its decrement and increment cancel, so it never changes feasibility and contributes one accepted request.
- **Duplicate requests:** Each is a distinct employee request and has its own bit. Multiplicity is handled correctly.
- **Disconnected cycles:** Each balanced component contributes zero net change independently, so their union passes.
- **One unmatched edge:** It creates two nonzero building balances and fails.
- **Buildings absent from every request:** Their counters remain zero and do not affect validity.
- **Subset-size pruning:** A mask with count equal to `ans` is skipped because it cannot improve the numerical answer.
- **Generator short-circuit:** `all` may stop at the first nonzero building, improving typical work without changing the worst-case bound.
- **Exact source space:** No recursion is used; only the current balance list grows with $N$.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n2^m)$. Let $N$ be the number of buildings and $M$ the number of requests.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
