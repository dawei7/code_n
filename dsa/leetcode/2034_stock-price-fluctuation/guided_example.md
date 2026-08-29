# Guided Example: Stock Price Fluctuation 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"], "arguments": [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]}`
- **Required output:** `[null, null, null, 5, 10, null, 5, null, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a stream of **records** about a particular stock. Each record contains a **timestamp** and the corresponding **price** of the stock at that timestamp.

The objective is to compute `[null, null, null, 5, 10, null, 5, null, 2]` from `{"operations": ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"], "arguments": [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain two synchronized views of the records

The class must answer questions by timestamp and by price. One structure is not enough to make every operation efficient.

`d` is a dictionary mapping each timestamp to its current corrected price. It is authoritative for corrections and for looking up the price at the latest timestamp.

`ls` is a `SortedList` containing one price for every currently recorded timestamp. It is a multiset: equal prices may appear several times. Its first and last entries provide the current minimum and maximum prices.

`last` stores the greatest timestamp ever recorded. Together, these three pieces represent the same logical record set from complementary directions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"], "arguments": [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Insert a previously unseen timestamp

When `timestamp` is absent from the dictionary, `update` adds `timestamp -> price` to `d` and inserts `price` into the sorted multiset.

It then sets `last = max(last, timestamp)`. An out-of-order update with a smaller timestamp leaves the latest timestamp unchanged; an update with a larger timestamp makes it the new latest.

After these actions, the dictionary has one additional record and the sorted list has exactly one corresponding additional price.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Correct an existing timestamp without leaving a stale price

If the timestamp already exists, its old price must stop affecting minimum and maximum queries. The source retrieves `d[timestamp]` and removes one occurrence of that value from `ls` before storing the replacement.

Removing exactly one occurrence matters. Two different timestamps may legitimately share the same price. Correcting one of them must not remove both copies, because the other timestamp's price is still current.

After removal, the dictionary entry is overwritten and the new price is added to `ls`. The number of dictionary entries and multiset entries remains equal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, 5, 10, null, 5, null, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"], "arguments": [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, 5, 10, null, 5, null, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dictionary plus two heaps:** Push corrected prices lazily and discard stale heap tops during queries; updates are simple but heaps may retain obsolete entries.
- **Balanced map from price to frequency:** Maintain counts at sorted price keys; it provides the same multiset behavior.
- **Scan dictionary values:** Makes updates cheap but every minimum and maximum query costs $O(Q)$.
- **Repeated timestamp:** Remove its old price once before adding the corrected price.
- **Duplicate prices at different timestamps:** The multiset retains separate occurrences.
- **Correction to the same price:** One occurrence is removed and re-added, leaving the logical state unchanged.
- **Out-of-order older update:** It does not change `last`.
- **New greatest timestamp:** It becomes `last` even if its price is not an extreme.
- **Correction at the latest timestamp:** `current` immediately returns the replacement price.
- **Current versus last arrival:** `current` follows the largest timestamp, not call order.
- **Single record:** Its price is simultaneously current, minimum, and maximum.
- **Query before update:** Excluded by the contract, so empty-endpoint handling is unnecessary.
- **No deletion operation:** This is why `last` never needs to move backward.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log Q)$. Let $Q$ be the number of distinct recorded timestamps. Dictionary membership, lookup, and assignment are expected $O(1)$. `SortedList.add` and `SortedList.remove` take $O(\log Q)$ amortized time in the intended sorted-container implementation, so `update` is $O(\log Q)$.
- **Auxiliary Space Complexity:** $O(Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
