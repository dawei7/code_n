# Guided Example: Minimum Moves to Make Array Complementary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 4, 3], "limit": 4}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of **even** length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive.

The objective is to compute `1` from `{"nums": [1, 2, 4, 3], "limit": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat mirrored positions as independent pairs

Because `n` is even, the array contains exactly `n / 2` mirrored pairs:

`(nums[i], nums[n - 1 - i])`.

For the final array to be complementary, every pair must have one common target sum `S`. Since each value after replacement must lie from one through `limit`, every possible target lies in

$$
2 \le S \le 2\cdot\texttt{limit}.
$$

For a fixed target, different pairs can be changed independently. The total number of moves is the sum of each pair’s minimum cost. The challenge is to evaluate all target sums without examining every pair for every target.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 4, 3], "limit": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand one pair’s piecewise cost

Take one pair and reorder its values so `x <= y`. Its current sum is `x + y`.

With zero moves, the pair can reach only `x + y`.

With one move, keep one value and replace the other:

- keeping `x` permits sums from `x + 1` through `x + limit`;
- keeping `y` permits sums from `y + 1` through `y + limit`.

Because `x <= y <= limit`, these ranges overlap or touch and their union is the continuous interval

$$
[x+1,\ y+\texttt{limit}].
$$

Therefore the minimum pair cost is:

- two moves for `2 <= S < x + 1`;
- one move for `x + 1 <= S < x + y`;
- zero moves at `S = x + y`;
- one move for `x + y < S <= y + limit`;
- two moves for larger valid `S`.

This step pattern changes only at a few known boundaries, which makes a difference array appropriate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Take one pair and reorder its values so `x <= y`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Encode the step pattern with boundary changes

The array `d` does not store costs directly. It stores how the cost changes when the target advances to an index. Prefix-accumulating `d` later reconstructs the actual total.

For each pair, the source performs these conceptual updates:

- `d[2] += 2` starts the pair at cost two for the smallest target;
- at `x + 1`, cost drops from two to one, a net change of `-1`;
- at `x + y`, cost drops from one to zero, another `-1`;
- at `x + y + 1`, cost rises from zero to one, a change of `+1`;
- at `y + limit + 1`, cost rises from one to two, another `+1`.

The source writes the first net `-1` as consecutive `-= 2` and `+= 1` operations. It writes the last net `+1` as `-= 1` followed by `+= 2`. Those pairs look redundant but algebraically encode exactly the boundary changes above.

All mirrored pairs update the same `d`. Difference arrays are additive, so at any target the reconstructed prefix sum equals the sum of all pair costs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 4, 3], "limit": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Brute force every target and pair:** This foll:** - **Brute force every target and pair:** This follows the definition but costs $O(nL)$, repeating the same piecewise-cost reasoning for every target.
- **Binary-search counting:** Sort smaller and larger pair members and count zero-, one-, and two-move cases for every target with binary searches. It is correct but slower by logarithmic factors and uses more involved statistics.
- **Combine redundant updates:** The two operations at `x+1` can be written as `d[x+1] -= 1`, and those at `y+L+1` as `d[y+L+1] += 1`. The exact source leaves their derivational components separate.
- **Pair values already equal the chosen target:** The update at `x+y` makes that pair contribute zero.
- **Target at two:** Only `[1,1]` is unchanged; other pairs require one or two changes according to the same boundaries.
- **Target at `2L`:** Only `[L,L]` is unchanged, and the allocated sentinel safely records changes just beyond this valid endpoint.
- **`x == y`:** The one-change intervals still form `[x+1, x+L]`, and the zero-cost point `2x` lies within it.
- **Minimum array length two:** There is one pair, so the result is zero because choosing its current sum already makes all pairs agree.
- **Repeated mirrored pairs:** Their identical difference updates simply add, correctly multiplying their contribution.
- **Even-length guarantee:** Every element belongs to exactly one pair. An unpaired center in an odd-length array would need separate treatment.
- **Replacement bounds:** The interval endpoints `x+1` and `y+L` come directly from keeping one value and choosing the other in `[1,L]`; overlooking these bounds gives incorrect one-move ranges.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + L)$. Let `n` be the array length and `L = limit`. Processing `n/2` mirrored pairs takes $O(n)$ time, with constant work per pair. The difference array has $2L + 2$ positions, and accumulating its slice takes $O(L)$ time. Total time is $O(n + L)$.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
