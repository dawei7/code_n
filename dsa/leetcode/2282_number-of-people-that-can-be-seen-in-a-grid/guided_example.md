# Guided Example: Number of People That Can Be Seen in a Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [[3, 1, 4, 2, 5]]}`
- **Required output:** `[[2, 1, 2, 1, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` **0-indexed** 2D array of positive integers `heights` where $\text{heights}[i][j]$ is the height of the person standing at position `(i, j)`.

The objective is to compute `[[2, 1, 2, 1, 0]]` from `{"heights": [[3, 1, 4, 2, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate rightward and downward visibility

A person may see only along the same row to the right or along the same column below. These two directions are independent: no person can be both strictly right and strictly below while sharing the required row or column.

The helper `f(nums)` solves the one-dimensional problem of how many people each position can see to its right. The main method applies it to every row, then applies it to every top-to-bottom column and adds the downward counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [[3, 1, 4, 2, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan a line from the far end

For a one-dimensional list, `f` processes indices from right to left. When position `i` is handled, every possible person to its right has already been summarized by a monotonic stack.

The stack contains a strictly decreasing sequence of representative heights from farther positions at the bottom to nearer relevant positions at the top. People already proven to be blocked for every future position are removed, so the stack is a visibility frontier rather than a copy of the suffix.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: See and remove every shorter frontier person

Let current height be `nums[i]`. While the nearest frontier height `stk[-1]` is strictly smaller, the current person can see that person, so `ans[i]` increases and the height is popped.

The popped person cannot block the current person's view because the current person is taller. Popping may expose another farther frontier person. That person is also visible if it is still shorter: all relevant people between them that could block have already been represented and removed in increasing visibility order.

Each popped height counts as one visible person. It is removed because the current, taller and nearer person will dominate it as a blocker for positions farther left.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[2, 1, 2, 1, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [[3, 1, 4, 2, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[2, 1, 2, 1, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan every person ahead:** Checking all rightward and downward pairs can take `O(mn(m+n))` time.
- **Nearest-greater arrays alone:** A person can see several shorter people before the first blocker, so only storing one greater neighbor is insufficient.
- **Monotonic stack without equal removal:** A future taller person could incorrectly count multiple equal-height people even though the nearer equal blocks the farther one.
- **Process rows only:** It omits all downward visibility.
- **Transpose the matrix:** It can reuse row logic for columns but requires another matrix-sized structure; direct column extraction is simpler.
- **One row:** Only rightward counts contribute.
- **One column:** Only downward counts contribute.
- **Single cell:** Both scans return zero for that person.
- **Strictly increasing line:** Each person sees only the immediate taller person to the right.
- **Strictly decreasing line:** A taller left person can see a chain of successively exposed shorter frontier people.
- **Equal adjacent heights:** The nearer equal is visible and blocks the farther suffix for that current person.
- **Several equal heights:** Duplicate collapse retains only the nearest representative for future observers.
- **First taller blocker:** It is counted once, then traversal stops beyond it.
- **Right and below overlap:** No distinct target position can satisfy both same-row-right and same-column-below, so counts add without duplication.
- **Input preservation:** Column lists and answer rows are new objects; `heights` remains unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the grid have `m` rows and `n` columns. In one call to `f`, each height is pushed once and popped at most once, including equal-removal pops. Its time is linear in the line length.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
