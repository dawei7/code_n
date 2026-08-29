# Guided Example: Online Stock Span

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["next", 7], ["next", 2], ["next", 1], ["next", 2]]}`
- **Required output:** `[1, 1, 1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design an algorithm that collects daily price quotes for some stock and returns **the span** of that stock's price for the current day.

The objective is to compute `[1, 1, 1, 3]` from `{"operations": [["next", 7], ["next", 2], ["next", 1], ["next", 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

Today's span extends backward through consecutive prices less than or equal to today's price and stops immediately before the first greater price. A monotonic stack can skip whole already-summarized blocks instead of comparing today with every prior day individually.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["next", 7], ["next", 2], ["next", 1], ["next", 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Each stack entry is a pair `(price, span)`. Its span tells how many consecutive days ending at that stored day were less than or equal to that stored price and have already been compressed into the entry.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The stack's prices are strictly decreasing from bottom to top. When a new price arrives:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["next", 7], ["next", 2], ["next", 1], ["next", 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan stored prices backward per call:** This is simple but can cost $O(q^2)$ total on increasing sequences.
- **Store all prices with a previous-greater index:** It can also answer spans, but the monotonic stack is the direct compressed representation.
- **Segment tree:** Supports more general historical queries but is unnecessary for this one-sided online span and has logarithmic operation cost.
- **First price:** No stack entry exists, so its span is one.
- **Strictly increasing prices:** Each new call pops all remaining entries, and spans grow by one each day. Total work remains linear because popped entries never return.
- **Strictly decreasing prices:** Nothing is popped, every span is one, and stack space grows to $q$.
- **Equal prices:** They are popped and combined because equality is allowed in the span.
- **One very large price:** It may absorb many compressed blocks in one call.
- **Greater blocker:** Once encountered, it stops the consecutive span even if still earlier prices are small.
- **No explicit day indices:** The stored block sizes contain exactly the distance information needed for the result.
- **Positive price bounds:** Comparisons are ordinary integer comparisons; magnitude does not change the method.
- **Amortized versus worst case:** Claiming every call literally executes constant work is inaccurate; constant time is an amortized guarantee.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let $q$ be the number of `next` calls. A single call can pop $O(q)$ entries in the worst case, such as a large price after a long decreasing sequence. However, every entry is pushed once and popped at most once over the full operation history.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
