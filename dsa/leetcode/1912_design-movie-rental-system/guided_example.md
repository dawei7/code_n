# Guided Example: Design Movie Rental System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["MovieRentingSystem", "search"], "arguments": [[1, [[0, 1, 1]]], [9999]]}`
- **Required output:** `[null, []]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a movie renting company consisting of `n` shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

The objective is to compute `[null, []]` from `{"operations": ["MovieRentingSystem", "search"], "arguments": [[1, [[0, 1, 1]]], [9999]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Maintain the order needed by each read operation.** `search(movie)` needs available copies of one movie ordered by price then shop. `report()` needs all rented copies ordered by price, shop, then movie. The system keeps two ordered indexes matching these two query shapes so neither operation must sort the entire inventory on demand.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["MovieRentingSystem", "search"], "arguments": [[1, [[0, 1, 1]]], [9999]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Store immutable prices separately.** `price_map` maps a combined shop/movie key to the fixed rental price. Method `f(shop, movie)` computes `shop << 30 | movie`. Shifting reserves 30 low bits for movie; constraints keep movie far below $2^{30}$, so different permitted pairs cannot collide. Rent and drop can recover price in constant expected map time without searching an ordered collection.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The constructor parameter `n` is not otherwise needed because entries explicitly describe every carried copy and shops are already validated by the contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, []]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["MovieRentingSystem", "search"], "arguments": [[1, [[0, 1, 1]]], [9999]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, []]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Heaps with lazy deletion:** Per-movie and global heaps can return cheapest entries, but rent/drop state changes require stale-entry filtering and careful synchronization.
- **Sort on every search/report:** Correct but can repeatedly cost $O(E\log E)$ rather than maintaining order incrementally.
- **Ordinary sets:** Support membership changes but not cheapest-five ordering.
- **Fewer than five matches:** Slicing naturally returns the available count without padding.
- **No available or rented copies:** Empty sorted-list slices produce empty results.
- **Equal prices:** Tuple fields apply the exact shop and then movie tie breakers.
- **Repeated state changes:** A dropped copy re-enters with its original price and correct sorted position.
- **Search for unknown movie:** The default dictionary returns an empty list but also stores that empty key, explaining possible $O(Q)$ extra space.
- **Composite-key safety:** The low 30 bits are sufficient for every allowed movie ID; changing constraints beyond that range would require tuple keys or a wider reservation.
- **Valid-operation guarantee:** The source uses strict `remove` rather than defensive discard. Invalid rent/drop calls would raise, but tests exclude them.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E\log E)$. Let $E$ be the number of entries and $Q$ the number of calls. Each constructor insertion into a movie's ordered list costs logarithmic time in that list's size, giving $O(E\log E)$ as a broad bound. Each rent or drop performs ordered removal and insertion in $O(\log E)$ plus expected $O(1)$ price lookup.
- **Auxiliary Space Complexity:** $O(E+Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
