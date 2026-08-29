# Guided Example: Two Sum III - Data structure design

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["TwoSum", "add", "add", "find"], "arguments": [[], [3], [3], [6]]}`
- **Required output:** `[null, null, null, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

The objective is to compute `[null, null, null, true]` from `{"operations": ["TwoSum", "add", "add", "find"], "arguments": [[], [3], [3], [6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store counts for a growing stream

The class must support many interleaved `add` and `find` calls. A frequency map
is a natural persistent representation: `cnt[x]` is the number of times
value `x` has been added and not otherwise removed. There is no removal method,
so counts only increase.

`defaultdict(int)` supplies zero as the initial count for a missing key.
`add(number)` can therefore increment one entry directly without an explicit
existence branch.

Keeping counts rather than a set is essential. A set can say whether value
three exists, but it cannot distinguish one copy from two copies. That
distinction determines whether three may pair with another three to satisfy
`find(6)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["TwoSum", "add", "add", "find"], "arguments": [[], [3], [3], [6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Search complements among distinct values

For a query `value`, the source iterates over `(x, v)` entries in the map.
For each stored value `x`, its only possible partner is:

`y = value - x`.

If `y` is absent, no pair beginning with `x` reaches the target. If it is
present and differs from `x`, one occurrence of each key is enough and the
method returns true.

If `x == y`, the equation asks to use the same numeric value twice. The problem
allows two equal integers but still requires two stored elements. The condition
`v > 1` verifies that at least two copies were added.

If no key finds a valid complement, the loop finishes and returns false.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the sample operations

Construction creates an empty frequency map. Adding one, three, and five gives
counts `{1:1, 3:1, 5:1}`.

For `find(4)`, when the loop examines one, it computes complement three.
Three is present and different from one, so the query returns true.

For `find(7)`, complements six, four, and two are all absent. The full scan
ends and returns false.

Suppose another three is added. `find(6)` may examine `x = 3`, compute the same
value as its complement, and see count two. It returns true. With only one
three, the `v > 1` test would correctly reject using that single occurrence
twice.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["TwoSum", "add", "add", "find"], "arguments": [[], [3], [3], [6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sorted list with lazy sorting:** Append in $O(1)$, sort after changes, then use two pointers for queries. A query after an add can cost $O(n\log n)$.
- **Maintain a sorted list on every add:** Enables linear two-pointer queries but insertion can cost $O(n)$.
- **Precompute pair sums:** Makes `find` expected $O(1)$ but can require $O(n^2)$ update work and storage.
- **Set only:** Insufficient because it cannot validate two equal operands.
- **Empty structure:** The loop is empty and `find` returns false.
- **One stored value:** It cannot pair with itself unless added again.
- **Negative values:** Complement subtraction and hash lookup work unchanged.
- **Large query target:** An absent complement is simply rejected; no overflow occurs in Python.
- **Repeated additions:** They increment one count without increasing distinct-key space.
- **Missing import:** `defaultdict` must be imported before construction.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $u$ be the number of distinct stored values and $n$ the total number of
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
