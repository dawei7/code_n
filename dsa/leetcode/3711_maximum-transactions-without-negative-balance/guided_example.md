# Guided Example: Maximum Transactions Without Negative Balance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"transactions": [2, -5, 3, -1, -2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `transactions`, where $\text{transactions}[i]$ represents the amount of the $i^{\text{th}}$ transaction:

The objective is to compute `4` from `{"transactions": [2, -5, 3, -1, -2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Tentatively selecting every transaction

For current amount `x`, the source performs:

`s += x`

`st.add(x)`.

This preserves the original order conceptually: the current transaction is appended after every previously retained index. `st` sorts only the **values used for choosing a removal**; it does not reorder the actual subsequence.

If `s >= 0`, the selected sequence remains feasible through the current position. Keeping `x` increases its cardinality by one, so there is no reason to skip it.

Positive receipts and zero transactions can never cause the first violation. A negative outgoing transaction may.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"transactions": [2, -5, 3, -1, -2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Repairing a negative balance

When `s < 0`, at least one currently selected amount is negative. The source removes:

`y = st.pop(0)`,

the smallest value. Among all possible single removals, deleting the minimum increases the remaining sum the most.

It updates:

`s -= y`.

Because `y` is negative, subtracting it raises the balance.

The source uses a `while` loop, but after one newly added transaction causes a previously feasible selection to go negative, one removal is enough. Let the prior nonnegative balance be $S$ and current amount be $x$. The minimum selected value satisfies $y\le x$, so:

$$
S+x-y\ge S\ge0.
$$

The loop nevertheless expresses the general requirement directly and remains correct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why removing an earlier negative preserves prefix feasibility

The removed minimum may be an earlier transaction rather than the current one.

If the current transaction is removed, the selected sequence returns to the previously feasible sequence.

If an earlier negative amount is removed, all selected-prefix balances before that transaction remain unchanged. Every balance at or after its old position increases by `-y`. Thus no earlier feasible prefix becomes negative, and the repaired final balance is nonnegative.

The remaining indices still appear in original order, so they form a legal subsequence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"transactions": [2, -5, 3, -1, -2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Min-heap:** A standard heap supports insertion and removal of the minimum in $O(\log n)$ and is sufficient because no other sorted operation is needed.
- **Skip every transaction that immediately fails:** Rejecting only the current value can be suboptimal when an earlier, more negative transaction should be exchanged out instead.
- **Dynamic programming by balance:** Balances span an enormous range, making a value-indexed DP infeasible.
- **All negative transactions:** Each tentative selection is repaired by removing a negative value, and the final answer is zero.
- **All transactions feasible:** No removal occurs and the method returns $n$.
- **Zero transaction:** It neither helps nor hurts balance but increases cardinality, so it should always be kept.
- **Repeated amounts:** `SortedList` preserves multiplicity; each occurrence represents a distinct transaction index.
- **Removing an earlier item:** Deleting a negative earlier transaction only raises later prefix balances and preserves relative order of all retained indices.
- **Several severe negatives:** The loop formulation can remove as many minima as needed, while each stored occurrence is popped at most once overall.
- **Negative final total of all transactions:** A large feasible subsequence may still exist after discarding the most damaging negative amounts.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $n$ be the number of transactions.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
